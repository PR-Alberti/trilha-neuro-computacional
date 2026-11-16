
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

rng = np.random.default_rng(0)
torch.manual_seed(0)

def gerar_grafo(n, p, rng):
    A = np.zeros((n, n), dtype=np.float32)
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                A[i, j] = 1.0
                A[j, i] = 1.0
    graus = A.sum(axis=1, keepdims=True)
    A_til = A + np.eye(n, dtype=np.float32)
    d_inv_sqrt = 1.0 / np.sqrt(A_til.sum(axis=1))
    A_norm = (d_inv_sqrt[:, None] * A_til) * d_inv_sqrt[None, :]
    return torch.from_numpy(A_norm), torch.from_numpy(graus)

dados = []
for _ in range(20):
    dados.append((*gerar_grafo(8, 0.20, rng), 0))
for _ in range(20):
    dados.append((*gerar_grafo(8, 0.60, rng), 1))

ordem = rng.permutation(len(dados))
treino = [dados[i] for i in ordem[:28]]
teste = [dados[i] for i in ordem[28:]]

class ClassificadorGrafos(nn.Module):
    def __init__(self, d_oculta):
        super().__init__()
        self.fc_no = nn.Linear(1, d_oculta)
        self.fc_grafo = nn.Linear(d_oculta, 2)

    def forward(self, A_norm, X):
        H = F.relu(A_norm @ self.fc_no(X))
        h_G = H.sum(dim=0, keepdim=True)  # pooling global por soma
        return self.fc_grafo(h_G)

modelo = ClassificadorGrafos(8)
otim = torch.optim.Adam(modelo.parameters(), lr=0.05)

for _ in range(120):
    modelo.train()
    otim.zero_grad()
    perda_total = 0.0
    for A_norm, X, classe in treino:
        logits = modelo(A_norm, X)
        alvo = torch.tensor([classe], dtype=torch.long)
        perda_total = perda_total + F.cross_entropy(logits, alvo)
    (perda_total / len(treino)).backward()
    otim.step()

modelo.eval()
acertos = 0
with torch.no_grad():
    for A_norm, X, classe in teste:
        pred = modelo(A_norm, X).argmax(dim=1).item()
        acertos += int(pred == classe)

print(f"Acurácia no teste (12 grafos): {acertos / len(teste):.1%}")

# Saída esperada aproximada (pode variar levemente entre versões/máquinas):
# Acurácia no teste (12 grafos): ≈ 83% a 100%
          