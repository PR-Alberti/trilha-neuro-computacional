
import numpy as np
import torch
import torch.nn as nn
from scipy.stats import spearmanr
from sklearn.datasets import load_digits

torch.manual_seed(0)
rng = np.random.default_rng(0)

digits = load_digits()
X_np = (digits.data / 16.0).astype(np.float32)
y_np = digits.target
prototipos_px = np.array([X_np[y_np == d].mean(axis=0) for d in range(10)])

X_t = torch.from_numpy(X_np)
y_t = torch.from_numpy(y_np).long()
oculta = nn.Sequential(nn.Linear(64, 32), nn.ReLU())
modelo = nn.Sequential(oculta, nn.Linear(32, 10))
otim = torch.optim.Adam(modelo.parameters(), lr=0.02)
criterio = nn.CrossEntropyLoss()

for _ in range(150):
    otim.zero_grad()
    loss = criterio(modelo(X_t), y_t)
    loss.backward()
    otim.step()

with torch.no_grad():
    acc = (modelo(X_t).argmax(dim=1) == y_t).float().mean().item()
    prototipos_mlp = oculta(torch.from_numpy(prototipos_px)).numpy()

rdm_px = 1.0 - np.corrcoef(prototipos_px)
rdm_mlp = 1.0 - np.corrcoef(prototipos_mlp)

idx = np.triu_indices(10, k=1)  # K*(K-1)/2 = 45 pares sem a diagonal
tri_px, tri_mlp = rdm_px[idx], rdm_mlp[idx]
rho, _ = spearmanr(tri_px, tri_mlp)

n_perm = 500
contagem = 0
for _ in range(n_perm):
    perm = rng.permutation(10)
    rho_perm, _ = spearmanr(tri_px, rdm_mlp[np.ix_(perm, perm)][idx])
    if rho_perm >= rho:
        contagem += 1
p_perm = (contagem + 1) / (n_perm + 1)

print(f"Acuracia MLP:             {acc:.3f}")       # ≈ 0.99
print(f"Pares unicos:             {len(tri_px)}")  # 45
print(f"Spearman pixels vs. MLP:  {rho:.3f}")       # ≈ 0.55 a 0.75 (varia entre versões/máquinas)
print(f"p-valor permutacao:       {p_perm:.4f}")   # ≈ 0.002 (< 0.01)
      