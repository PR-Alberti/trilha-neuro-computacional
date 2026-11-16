
import numpy as np

# Grafo de 4 nós (arestas: 0-1, 0-2, 1-2, 2-3) e atributos 4x2
A = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
], dtype=float)
H = np.array([
    [2.0, 1.0],
    [4.0, 0.0],
    [0.0, 3.0],
    [6.0, -1.0],
], dtype=float)

def agregar_media(A_mat, H_mat):
    graus = A_mat.sum(axis=1)
    D_inv = np.diag(1.0 / graus)
    return D_inv @ A_mat @ H_mat

saida_orig = agregar_media(A, H)

# Permutação que reordena os nós como [2, 0, 3, 1]
perm = [2, 0, 3, 1]
P = np.eye(4)[perm]
A_perm = P @ A @ P.T
H_perm = P @ H
saida_perm = agregar_media(A_perm, H_perm)

erro = np.max(np.abs(saida_perm - P @ saida_orig))
print("Saída original:\n", saida_orig)
print("Equivariante (erro < 1e-12)?", bool(erro < 1e-12))

# Saída esperada:
# Saída original:
#  [[2.  1.5]
#   [1.  2. ]
#   [4.  0. ]
#   [0.  3. ]]
# Equivariante (erro < 1e-12)? True
      