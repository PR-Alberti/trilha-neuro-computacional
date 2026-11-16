
import numpy as np
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset

# Sementes fixas para reprodutibilidade
np.random.seed(0)
torch.manual_seed(0)

# 1. Dados: 1797 imagens 8x8 normalizadas para [0, 1]
digitos = load_digits()
X = (digitos.images / 16.0).astype(np.float32)
y = digitos.target.astype(np.int64)

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0)

# Adiciona o eixo de canal C=1 -> (N, 1, 8, 8)
X_tr_t = torch.from_numpy(X_tr).unsqueeze(1)
X_te_t = torch.from_numpy(X_te).unsqueeze(1)
y_tr_t = torch.from_numpy(y_tr)
y_te_t = torch.from_numpy(y_te)

loader_tr = DataLoader(TensorDataset(X_tr_t, y_tr_t), batch_size=64, shuffle=True)


# 2. Arquitetura: conv -> ReLU -> pool -> conv -> ReLU -> flatten -> linear
class PequenaCNN(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(16 * 4 * 4, 10)

    def forward(self, x: torch.Tensor, mostrar_formas: bool = False) -> torch.Tensor:
        if mostrar_formas:
            print("Entrada:        ", tuple(x.shape))
        x = self.relu(self.conv1(x))
        if mostrar_formas:
            print("Após conv1+ReLU:", tuple(x.shape))
        x = self.pool(x)
        if mostrar_formas:
            print("Após pool:      ", tuple(x.shape))
        x = self.relu(self.conv2(x))
        if mostrar_formas:
            print("Após conv2+ReLU:", tuple(x.shape))
        x = self.flatten(x)
        if mostrar_formas:
            print("Após flatten:   ", tuple(x.shape))
        x = self.fc(x)
        if mostrar_formas:
            print("Saída linear:   ", tuple(x.shape))
        return x


modelo = PequenaCNN()

with torch.no_grad():
    _ = modelo(X_tr_t[:1], mostrar_formas=True)

# Saída exata das formas:
# Entrada:         (1, 1, 8, 8)
# Após conv1+ReLU: (1, 8, 8, 8)
# Após pool:       (1, 8, 4, 4)
# Após conv2+ReLU: (1, 16, 4, 4)
# Após flatten:    (1, 256)
# Saída linear:    (1, 10)

n_params = sum(p.numel() for p in modelo.parameters())
print(f"Total de parâmetros: {n_params}")  # Total de parâmetros: 3818

# 3. Treinamento rápido em CPU com Adam
criterio = nn.CrossEntropyLoss()
otimizador = torch.optim.Adam(modelo.parameters(), lr=0.005)

for epoca in range(1, 26):
    modelo.train()
    for xb, yb in loader_tr:
        otimizador.zero_grad()
        logits = modelo(xb)
        perda = criterio(logits, yb)
        perda.backward()
        otimizador.step()

# 4. Avaliação no conjunto de teste (valores aproximados; variam conforme versão/CPU)
modelo.eval()
with torch.no_grad():
    logits_te = modelo(X_te_t)
    perda_te = criterio(logits_te, y_te_t).item()
    acuracia_te = (logits_te.argmax(dim=1) == y_te_t).float().mean().item()

print(f"Perda de teste: {perda_te:.3f} | Acurácia de teste: {100 * acuracia_te:.1f}%")
# Perda de teste ≈ 0.12 | Acurácia de teste ≈ 96% (pode variar um pouco)

# 5. Inspecionando dois filtros 3x3 aprendidos pela primeira camada
filtros = modelo.conv1.weight.data[:, 0].numpy()
for idx in range(2):
    print(f"\nFiltro {idx} aprendido (3x3):")
    print(np.round(filtros[idx], 2))
      