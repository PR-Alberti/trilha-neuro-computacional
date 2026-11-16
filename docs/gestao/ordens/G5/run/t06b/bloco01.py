
import numpy as np

# Grafo não direcionado de 4 nós (índices 0, 1, 2, 3 representando nós 1, 2, 3, 4)
# Arestas: (0,1), (0,2), (1,2), (2,3)
A = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
], dtype=int)

graus = A.sum(axis=1)
D = np.diag(graus)
A2 = A @ A

print("Graus:", graus)
print("Matriz D:\n", D)
print("Matriz A^2:\n", A2)
print("Caminhos de comprimento 2 entre nó 1 (idx 0) e nó 4 (idx 3):", A2[0, 3])

# Saída esperada:
# Graus: [2 2 3 1]
# Matriz D:
#  [[2 0 0 0]
#   [0 2 0 0]
#   [0 0 3 0]
#   [0 0 0 1]]
# Matriz A^2:
#  [[2 1 1 1]
#   [1 2 1 1]
#   [1 1 3 0]
#   [1 1 0 1]]
# Caminhos de comprimento 2 entre nó 1 (idx 0) e nó 4 (idx 3): 1
      