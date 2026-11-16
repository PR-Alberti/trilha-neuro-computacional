
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

rng = np.random.default_rng(0)
torch.manual_seed(0)

# 1. Grafo sintético: 2 comunidades de 50 nós (100 nós no total)
n_por_grupo = 50
n = 2 * n_por_grupo
rotulos = np.array([0] * n_por_grupo + [1] * n_por_grupo)

A = np.zeros((n, n), dtype=np.float32)
for i in range(n):
    for j in range(i + 1, n):
        p = 0.10 if rotulos[i] == rotulos[j] else 0.01
        if rng.random() < p:
            A[i, j] = 1.0
            A[j, i] = 1.0

# Normalização simétrica da GCN: D_til^(-1/2) (A + I) D_til^(-1/2)
A_til = A + np.eye(n, dtype=np.float32)
graus_til = A_til.sum(axis=1)
d_inv_sqrt = 1.0 / np.sqrt(graus_til)
A_norm_np = (d_inv_sqrt[:, None] * A_til) * d_inv_sqrt[None, :]

# Atributos ruidosos (sinal sutil +/- 0.25 com ruído N(0, 1))
sinal = np.where(rotulos[:, None] == 0, -0.25, 0.25).astype(np.float32)
X_np = sinal + rng.normal(0.0, 1.0, size=(n, 8)).astype(np.float32)

# Apenas 10% dos rótulos conhecidos no treino (5 de cada comunidade)
idx_treino = np.concatenate([
    rng.choice(np.arange(0, 50), size=5, replace=False),
    rng.choice(np.arange(50, 100), size=5, replace=False),
])
mask_treino = np.zeros(n, dtype=bool)
mask_treino[idx_treino] = True
mask_teste = ~mask_treino

X = torch.from_numpy(X_np)
A_norm = torch.from_numpy(A_norm_np)
y = torch.from_numpy(rotulos).long()
m_tr = torch.from_numpy(mask_treino)
m_te = torch.from_numpy(mask_teste)

# 2. Definição da camada GCN e dos modelos (GCN vs. MLP)
class CamadaGCN(nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()
        self.linear = nn.Linear(d_in, d_out)

    def forward(self, H, A_norm):
        return A_norm @ self.linear(H)

class RedeGCN(nn.Module):
    def __init__(self, d_in, d_oculta, n_classes):
        super().__init__()
        self.gcn1 = CamadaGCN(d_in, d_oculta)
        self.gcn2 = CamadaGCN(d_oculta, n_classes)

    def forward(self, X, A_norm):
        H = F.relu(self.gcn1(X, A_norm))
        return self.gcn2(H, A_norm)

class RedeMLP(nn.Module):
    def __init__(self, d_in, d_oculta, n_classes):
        super().__init__()
        self.fc1 = nn.Linear(d_in, d_oculta)
        self.fc2 = nn.Linear(d_oculta, n_classes)

    def forward(self, X):
        H = F.relu(self.fc1(X))
        return self.fc2(H)

def treinar_e_avaliar(modelo, usa_grafo=True, epocas=200):
    otim = torch.optim.Adam(modelo.parameters(), lr=0.02, weight_decay=5e-4)
    for _ in range(epocas):
        modelo.train()
        otim.zero_grad()
        logits = modelo(X, A_norm) if usa_grafo else modelo(X)
        perda = F.cross_entropy(logits[m_tr], y[m_tr])
        perda.backward()
        otim.step()
    modelo.eval()
    with torch.no_grad():
        logits = modelo(X, A_norm) if usa_grafo else modelo(X)
        preds = logits.argmax(dim=1)
        return (preds[m_te] == y[m_te]).float().mean().item()

torch.manual_seed(0)
acc_gcn = treinar_e_avaliar(RedeGCN(8, 16, 2), usa_grafo=True)
torch.manual_seed(0)
acc_mlp = treinar_e_avaliar(RedeMLP(8, 16, 2), usa_grafo=False)

print(f"Acurácia no teste (MLP, sem grafo): {acc_mlp:.1%}")
print(f"Acurácia no teste (GCN, com grafo): {acc_gcn:.1%}")

# Saída esperada aproximada (pode variar levemente entre versões e máquinas):
# Acurácia no teste (MLP, sem grafo): ≈ 60% a 72%
# Acurácia no teste (GCN, com grafo): ≈ 88% a 96%
      