
import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset

rng = np.random.default_rng(0)
torch.manual_seed(0)

n_por_classe = 200
imagens = np.zeros((2 * n_por_classe, 8, 8), dtype=np.float32)
rotulos = np.zeros(2 * n_por_classe, dtype=np.int64)

for i in range(n_por_classe):
    linha = rng.integers(2, 6)
    imagens[i, linha : linha + 2, 1:7] = 1.0  # classe 0: dendrito horizontal
    col = rng.integers(2, 6)
    imagens[n_por_classe + i, 1:7, col : col + 2] = 1.0  # classe 1: vertical
    rotulos[n_por_classe + i] = 1

imagens += rng.normal(0.0, 0.25, size=imagens.shape).astype(np.float32)

X_tr, X_te, y_tr, y_te = train_test_split(imagens, rotulos, test_size=0.25, random_state=0)
X_tr_t = torch.from_numpy(X_tr).unsqueeze(1)
X_te_t = torch.from_numpy(X_te).unsqueeze(1)

modelo = nn.Sequential(
    nn.Conv2d(1, 8, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(2, 2),
    nn.Conv2d(8, 16, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.Flatten(),
    nn.Linear(16 * 4 * 4, 2),
)

criterio = nn.CrossEntropyLoss()
otimizador = torch.optim.Adam(modelo.parameters(), lr=0.005)
loader = DataLoader(TensorDataset(X_tr_t, torch.from_numpy(y_tr)), batch_size=32, shuffle=True)

for _ in range(20):
    for xb, yb in loader:
        otimizador.zero_grad()
        criterio(modelo(xb), yb).backward()
        otimizador.step()

modelo.eval()
with torch.no_grad():
    acuracia = (modelo(X_te_t).argmax(dim=1).numpy() == y_te).mean()
print(f"Acurácia de teste: {100 * acuracia:.1f}%")
# Acurácia de teste ≈ 100% (a tarefa sintética é fácil)
          