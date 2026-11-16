
import numpy as np

# Grafo da figura (índices 0..5 correspondem aos nós 1..6)
arestas = [(0, 1), (0, 5), (1, 2), (1, 5), (2, 3), (2, 4), (3, 4), (4, 5)]
A = np.zeros((6, 6), dtype=float)
for i, j in arestas:
    A[i, j] = 1.0
    A[j, i] = 1.0

graus = A.sum(axis=1)
D = np.diag(graus)
L = D - A
autovalores = np.linalg.eigvalsh(L)

print("Graus:", graus.astype(int))
print("Menor autovalor ≈ 0?", bool(np.isclose(autovalores[0], 0.0)))
print("Todos autovalores >= 0?", bool(np.all(autovalores >= -1e-10)))

# Saída esperada:
# Graus: [2 3 3 2 3 3]
# Menor autovalor ≈ 0? True
# Todos autovalores >= 0? True
          