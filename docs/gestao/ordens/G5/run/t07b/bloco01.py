
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.datasets import load_digits
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(0)
np.random.seed(0)

digits = load_digits()
X = torch.tensor(digits.data / 16.0, dtype=torch.float32)  # (1797, 64) em [0, 1]
loader = DataLoader(TensorDataset(X), batch_size=64, shuffle=True)


class VAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(64, 32), nn.ReLU())
        self.fc_mu = nn.Linear(32, 2)
        self.fc_logvar = nn.Linear(32, 2)
        self.dec = nn.Sequential(
            nn.Linear(2, 32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.Sigmoid(),
        )

    def encode(self, x):
        h = self.enc(x)
        return self.fc_mu(h), self.fc_logvar(h)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + std * eps

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        return self.dec(z), mu, logvar


modelo = VAE()
opt = torch.optim.Adam(modelo.parameters(), lr=1e-3)

for epoca in range(40):
    soma_rec, soma_kl = 0.0, 0.0
    for (lote,) in loader:
        x_hat, mu, logvar = modelo(lote)
        rec = F.binary_cross_entropy(x_hat, lote, reduction="sum")
        kl = -0.5 * torch.sum(1.0 + logvar - mu.pow(2) - logvar.exp())
        perda = rec + kl
        opt.zero_grad()
        perda.backward()
        opt.step()
        soma_rec += rec.item()
        soma_kl += kl.item()

n_dados = len(X)
# Valores aproximados; podem variar levemente entre versões e máquinas
print(f"Reconstrucao media ≈ {soma_rec / n_dados:.2f} | KL medio ≈ {soma_kl / n_dados:.2f}")
# Reconstrucao media ≈ 24.23 | KL medio ≈ 1.49

with torch.no_grad():
    z_novos = torch.randn(5, 2)
    amostras = modelo.dec(z_novos)
print("Forma das amostras:", tuple(amostras.shape))  # Forma das amostras: (5, 64)
print(f"Faixa de valores ≈ [{amostras.min():.3f}, {amostras.max():.3f}]")
# Faixa de valores ≈ [0.000, 0.883]
      