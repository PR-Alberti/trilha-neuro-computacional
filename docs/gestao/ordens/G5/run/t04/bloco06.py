
import numpy as np
import torch
import torch.nn as nn
from scipy.stats import spearmanr
from sklearn.datasets import load_digits

torch.manual_seed(0)
digits = load_digits()
X_np = (digits.data / 16.0).astype(np.float32)
prototipos_px = np.array([X_np[digits.target == d].mean(axis=0) for d in range(10)])

camada = nn.Sequential(nn.Linear(64, 32), nn.ReLU())
with torch.no_grad():
    prototipos_aleat = camada(torch.from_numpy(prototipos_px)).numpy()

rdm_px = 1.0 - np.corrcoef(prototipos_px)
rdm_aleat = 1.0 - np.corrcoef(prototipos_aleat)
idx = np.triu_indices(10, k=1)

rho_ok, _ = spearmanr(rdm_px[idx], rdm_aleat[idx])
rho_err, _ = spearmanr(rdm_px.ravel(), rdm_aleat.ravel())

print(f"Spearman correto (45 pares): {rho_ok:.3f}")   # ≈ 0.50 a 0.70 (varia entre versões)
print(f"Spearman com diagonal (100): {rho_err:.3f}")  # maior que rho_ok devido aos 10 zeros
          