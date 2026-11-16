
import numpy as np
import torch
import torch.nn as nn
from sklearn.decomposition import PCA

rng = np.random.default_rng(0)
torch.manual_seed(0)

def gerar_com_atraso(n_amostras, t_stim=15, t_atraso=10, drift=0.3, sigma=0.8):
    y = rng.integers(0, 2, size=n_amostras)
    sinais = np.where(y == 1, drift, -drift)[:, None]
    stim = sinais + rng.normal(0.0, sigma, size=(n_amostras, t_stim))
    silencio = np.zeros((n_amostras, t_atraso))
    X = np.concatenate([stim, silencio], axis=1)
    return (
        torch.tensor(X[:, :, None], dtype=torch.float32),
        torch.tensor(y, dtype=torch.float32),
    )

X_tr, y_tr = gerar_com_atraso(800)
X_te, y_te = gerar_com_atraso(400)

gru = nn.GRU(1, 16, batch_first=True)
leitura = nn.Linear(16, 1)
otim = torch.optim.Adam(list(gru.parameters()) + list(leitura.parameters()), lr=0.01)
criterio = nn.BCEWithLogitsLoss()

for _ in range(70):
    otim.zero_grad()
    est, _ = gru(X_tr)
    loss = criterio(leitura(est[:, -1, :]).squeeze(-1), y_tr)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(list(gru.parameters()) + list(leitura.parameters()), 1.0)
    otim.step()

with torch.no_grad():
    est_te, _ = gru(X_te)
    acc = ((leitura(est_te[:, -1, :]).squeeze(-1) > 0).float() == y_te).float().mean().item()

H = est_te.numpy()
proj = PCA(n_components=1).fit_transform(H.reshape(-1, 16)).reshape(400, 25)
pos = proj[y_te.numpy() == 1].mean(axis=0)
neg = proj[y_te.numpy() == 0].mean(axis=0)
if pos[-1] < neg[-1]:
    pos, neg = -pos, -neg

print(f"Acuracia apos atraso: {acc:.3f}")  # ≈ 0.93
print("PC1 (+) em t=1,15,25:", [round(float(pos[i]), 2) for i in (0, 14, 24)])
# ≈ [-0.3, 1.63, 1.4]
print("PC1 (-) em t=1,15,25:", [round(float(neg[i]), 2) for i in (0, 14, 24)])
# ≈ [-0.27, -1.6, -2.31]
          