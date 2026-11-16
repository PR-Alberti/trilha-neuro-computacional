
import numpy as np
import torch
import torch.nn.functional as F

rng = np.random.default_rng(0)
n = 100
rotulos = np.array([0] * 50 + [1] * 50)
A = np.zeros((n, n), dtype=np.float32)
for i in range(n):
    for j in range(i + 1, n):
        p = 0.10 if rotulos[i] == rotulos[j] else 0.01
        if rng.random() < p:
            A[i, j] = 1.0
            A[j, i] = 1.0

A_til = A + np.eye(n, dtype=np.float32)
d_inv_sqrt = 1.0 / np.sqrt(A_til.sum(axis=1))
A_norm = torch.from_numpy((d_inv_sqrt[:, None] * A_til) * d_inv_sqrt[None, :])

sinal = np.where(rotulos[:, None] == 0, -0.25, 0.25).astype(np.float32)
H = torch.from_numpy(sinal + rng.normal(0.0, 1.0, size=(n, 8)).astype(np.float32))

for k in range(17):
    if k in (0, 1, 2, 4, 16):
        H_unit = F.normalize(H, p=2, dim=1)
        dispersao = H_unit.std(dim=0).mean().item()
        print(f"k = {k:2d} | dispersão entre nós: {dispersao:.4f}")
    H = A_norm @ H

# Saída esperada aproximada (pode variar levemente entre versões/máquinas):
# k =  0 | dispersão entre nós: ≈ 0.34
# k =  1 | dispersão entre nós: ≈ 0.26
# k =  2 | dispersão entre nós: ≈ 0.20
# k =  4 | dispersão entre nós: ≈ 0.13
# k = 16 | dispersão entre nós: ≈ 0.04
          