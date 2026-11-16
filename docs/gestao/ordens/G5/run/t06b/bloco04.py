
import numpy as np

def camada_mp(A, H, W_self, W_neigh):
    graus = A.sum(axis=1)
    graus_seguros = np.where(graus > 0, graus, 1.0)
    media_viz = (A @ H) / graus_seguros[:, None]
    pre_ativ = H @ W_self + media_viz @ W_neigh
    return np.maximum(0.0, pre_ativ)

A = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
], dtype=float)
H = np.array([
    [2.0, 0.0],
    [4.0, 2.0],
    [0.0, 4.0],
    [3.0, -1.0],
])
W_self = np.eye(2)
W_neigh = 0.5 * np.eye(2)

saida = camada_mp(A, H, W_self, W_neigh)
print("Saída:\n", saida)

# Saída esperada:
# Saída:
#  [[4.  1. ]
#   [4.5 3. ]
#   [2.  5. ]
#   [3.  0. ]]
          