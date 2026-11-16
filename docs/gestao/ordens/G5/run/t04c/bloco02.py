
import numpy as np
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

torch.manual_seed(0)
digits = load_digits()
X_np = (digits.data / 16.0).astype(np.float32)

pca = PCA(n_components=2, random_state=0)
X_rec_pca = pca.inverse_transform(pca.fit_transform(X_np))
mse_pca = float(np.mean((X_np - X_rec_pca) ** 2))

X_t = torch.from_numpy(X_np)
autoencoder = nn.Sequential(
    nn.Linear(64, 16),
    nn.ReLU(),
    nn.Linear(16, 2),
    nn.Linear(2, 16),
    nn.ReLU(),
    nn.Linear(16, 64),
)
otim = torch.optim.Adam(autoencoder.parameters(), lr=0.01)
criterio = nn.MSELoss()

for _ in range(400):
    otim.zero_grad()
    loss = criterio(autoencoder(X_t), X_t)
    loss.backward()
    otim.step()

with torch.no_grad():
    mse_ae = float(criterio(autoencoder(X_t), X_t).item())

print(f"MSE PCA (2 comp.):       {mse_pca:.4f}")  # ≈ 0.052 (varia pouco)
print(f"MSE Autoencoder (d=2):   {mse_ae:.4f}")   # ≈ 0.04 (menor que o PCA; varia entre versões/máquinas)
      