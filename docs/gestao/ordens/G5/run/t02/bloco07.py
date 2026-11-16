
import numpy as np
import torch
import torch.nn.functional as F
from sklearn.datasets import load_digits
from sklearn.linear_model import RidgeCV
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(0)
torch.manual_seed(0)

X_img = torch.from_numpy((load_digits().images / 16.0).astype(np.float32)).unsqueeze(1)
w1 = torch.randn(8, 1, 3, 3) * 0.4
w2 = torch.randn(16, 8, 3, 3) * 0.3

with torch.no_grad():
    h1 = F.max_pool2d(F.relu(F.conv2d(X_img, w1, padding=1)), 2)  # (N, 8, 4, 4)
    h2 = F.max_pool2d(F.relu(F.conv2d(h1, w2, padding=1)), 2)     # (N, 16, 2, 2)
    A1 = h1.flatten(start_dim=1).numpy()  # 128 características iniciais
    A2 = h2.flatten(start_dim=1).numpy()  # 64 características profundas

y_v1 = A1 @ rng.normal(0.0, 0.25, size=A1.shape[1]) + rng.normal(0.0, 0.3, size=len(A1))
y_it = A2 @ rng.normal(0.0, 0.35, size=A2.shape[1]) + rng.normal(0.0, 0.25, size=len(A2))

idx = np.arange(len(A1))
idx_tr, idx_te = train_test_split(idx, test_size=0.2, random_state=0)
alphas = [0.1, 1.0, 10.0, 50.0]

for nome_neuronio, y_alvo in [("V1 simulado", y_v1), ("IT simulado", y_it)]:
    for nome_camada, A in [("conv1", A1), ("conv2", A2)]:
        reg = RidgeCV(alphas=alphas).fit(A[idx_tr[:200]], y_alvo[idx_tr[:200]])
        r2 = r2_score(y_alvo[idx_te], reg.predict(A[idx_te]))
        print(f"{nome_neuronio} <- {nome_camada}: R² = {r2:.3f}")

# Tendência esperada:
# V1 simulado <- conv1 tem R² maior que conv2
# IT simulado <- conv2 tem R² maior que conv1
          