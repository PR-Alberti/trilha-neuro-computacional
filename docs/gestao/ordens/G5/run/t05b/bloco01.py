
import numpy as np
import torch
import torch.nn.functional as F


def atencao(Q, K, V):
    d_k = Q.shape[-1]
    scores = (Q @ K.T) / np.sqrt(d_k)
    # Subtrai o máximo de cada linha para evitar overflow em exp()
    scores_est = scores - np.max(scores, axis=-1, keepdims=True)
    exp_scores = np.exp(scores_est)
    pesos = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
    return pesos @ V, pesos


Q = np.array([[1.0, 0.0], [0.0, 2.0], [1.0, 1.0]])
K = np.array([[1.0, 1.0], [0.0, 1.0], [2.0, 0.0]])
V = np.array([[1.0, 0.0], [0.0, 2.0], [3.0, 1.0]])

saida_np, pesos_np = atencao(Q, K, V)

Q_t = torch.tensor(Q, dtype=torch.float32).unsqueeze(0)
K_t = torch.tensor(K, dtype=torch.float32).unsqueeze(0)
V_t = torch.tensor(V, dtype=torch.float32).unsqueeze(0)
saida_torch = F.scaled_dot_product_attention(Q_t, K_t, V_t).squeeze(0).numpy()

diff_max = np.max(np.abs(saida_np - saida_torch))
print("Pesos de atenção (NumPy):\n", np.round(pesos_np, 3))
# [[0.284 0.14  0.576]
#  [0.446 0.446 0.108]
#  [0.401 0.198 0.401]]
print("Saída (NumPy):\n", np.round(saida_np, 3))
# [[2.012 0.856]
#  [0.771 1.   ]
#  [1.604 0.797]]
print("Bate com PyTorch (atol=1e-6)?", bool(np.allclose(saida_np, saida_torch, atol=1e-6)))
# True
print(f"Diferença máxima: {diff_max:.2e}")
# Diferença máxima: ≈ 5e-08 (precisão float64 vs float32)
      