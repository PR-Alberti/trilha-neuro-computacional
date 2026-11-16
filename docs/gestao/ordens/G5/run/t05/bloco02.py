
import numpy as np
import torch
import torch.nn.functional as F

rng = np.random.default_rng(0)
Q = rng.standard_normal((4, 8))
K = rng.standard_normal((4, 8))
V = rng.standard_normal((4, 8))

scores = (Q @ K.T) / np.sqrt(Q.shape[-1])
scores_est = scores - np.max(scores, axis=-1, keepdims=True)
exp_scores = np.exp(scores_est)
pesos = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
saida_np = pesos @ V

saida_pt = F.scaled_dot_product_attention(
    torch.tensor(Q, dtype=torch.float32).unsqueeze(0),
    torch.tensor(K, dtype=torch.float32).unsqueeze(0),
    torch.tensor(V, dtype=torch.float32).unsqueeze(0),
).squeeze(0).numpy()

print("Pesos >= 0?", bool(np.all(pesos >= 0)))                  # True
print("Linhas somam 1?", bool(np.allclose(pesos.sum(-1), 1)))   # True
print("Coincide com PyTorch?", bool(np.allclose(saida_np, saida_pt, atol=1e-6)))  # True
          