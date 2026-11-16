
import torch
import torch.nn as nn

torch.manual_seed(0)

# Simula um extrator pré-treinado (camadas congeladas)
extrator = nn.Sequential(
    nn.Linear(16, 32),
    nn.ReLU(),
    nn.Linear(32, 32),
    nn.ReLU(),
)
for p in extrator.parameters():
    p.requires_grad = False

cabeca = nn.Linear(32, 2)  # Única parte treinável

total = sum(p.numel() for p in extrator.parameters()) + sum(p.numel() for p in cabeca.parameters())
treinaveis = sum(p.numel() for p in list(extrator.parameters()) + list(cabeca.parameters()) if p.requires_grad)
print(f"Parâmetros totais: {total} | Treináveis: {treinaveis} ({100 * treinaveis / total:.2f}%)")

# Tarefa sintética de classificação binária
X = torch.randn(120, 16)
y = (X[:, 0] + X[:, 1] > 0).long()

with torch.no_grad():
    H = extrator(X)  # Extrai embeddings sem acumular gradientes

otim = torch.optim.Adam(cabeca.parameters(), lr=0.05)
criterio = nn.CrossEntropyLoss()
for _ in range(100):
    perda = criterio(cabeca(H), y)
    otim.zero_grad()
    perda.backward()
    otim.step()

acc = (cabeca(H).argmax(dim=1) == y).float().mean().item()
print(f"Acurácia no treino ≈ {acc:.2f}")
# Saída esperada:
# Parâmetros totais: 1666 | Treináveis: 66 (3.96%)
# Acurácia no treino ≈ 0.90 (valor aproximado; pode variar entre versões)
      