
import numpy as np
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset

np.random.seed(0)
torch.manual_seed(0)

# Imagens 8x8 com valores em [0, 16], normalizadas para [0, 1]
digitos = load_digits()
X = digitos.data.astype(np.float32) / 16.0
y = digitos.target.astype(np.int64)

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=0, stratify=y
)

ds_treino = TensorDataset(torch.from_numpy(X_treino), torch.from_numpy(y_treino))
loader_treino = DataLoader(ds_treino, batch_size=64, shuffle=True)
X_teste_t, y_teste_t = torch.from_numpy(X_teste), torch.from_numpy(y_teste)

modelo = nn.Sequential(
    nn.Linear(64, 32),
    nn.ReLU(),
    nn.Linear(32, 10),
)

criterio = nn.CrossEntropyLoss()  # Recebe logits brutos
otimizador = torch.optim.Adam(modelo.parameters(), lr=0.01, weight_decay=1e-4)

for epoca in range(1, 41):
    modelo.train()
    perda_acum = 0.0
    for xb, yb in loader_treino:
        otimizador.zero_grad()          # 1. Zera gradientes acumulados
        logits = modelo(xb)             # 2. Passagem direta (logits)
        perda = criterio(logits, yb)    # 3. Entropia cruzada
        perda.backward()                # 4. Backpropagation
        otimizador.step()               # 5. Atualiza pesos com Adam
        perda_acum += perda.item() * len(xb)

    if epoca in (1, 10, 20, 40):
        perda_media = perda_acum / len(ds_treino)
        modelo.eval()
        with torch.no_grad():
            acc = (modelo(X_teste_t).argmax(dim=1) == y_teste_t).float().mean().item()
        print(f"Época {epoca:2d} | Perda treino: {perda_media:.3f} | Acurácia teste: {acc:.3f}")

# Saída esperada aproximada (varia um pouco conforme versão/máquina):
# Época  1 | Perda treino: ≈ 1.754 | Acurácia teste: ≈ 0.831
# Época 10 | Perda treino: ≈ 0.092 | Acurácia teste: ≈ 0.961
# Época 20 | Perda treino: ≈ 0.043 | Acurácia teste: ≈ 0.967
# Época 40 | Perda treino: ≈ 0.017 | Acurácia teste: ≈ 0.967
      