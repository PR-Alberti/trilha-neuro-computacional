
import numpy as np

# 1. Limiar em matriz de correlação funcional 4x4
R = np.array([
    [ 1.00,  0.62, -0.45,  0.18],
    [ 0.62,  1.00,  0.25, -0.35],
    [-0.45,  0.25,  1.00,  0.51],
    [ 0.18, -0.35,  0.51,  1.00],
])
sem_diagonal = ~np.eye(4, dtype=bool)
A_03 = ((np.abs(R) > 0.3) & sem_diagonal).astype(int)
A_04 = ((np.abs(R) > 0.4) & sem_diagonal).astype(int)

print("Graus com |r| > 0.3:", A_03.sum(axis=1))
print("Graus com |r| > 0.4:", A_04.sum(axis=1))

# 2. Pooling global: média vs. soma
H_G1 = np.array([[1.0, 3.0], [2.0, 1.0], [0.0, 2.0]])
H_G2 = np.array([[1.0, 2.0], [1.0, 2.0], [1.0, 2.0], [1.0, 2.0]])

print("G1 média:", H_G1.mean(axis=0), "| soma:", H_G1.sum(axis=0))
print("G2 média:", H_G2.mean(axis=0), "| soma:", H_G2.sum(axis=0))

# Saída esperada:
# Graus com |r| > 0.3: [2 2 2 2]
# Graus com |r| > 0.4: [2 1 2 1]
# G1 média: [1. 2.] | soma: [3. 6.]
# G2 média: [1. 2.] | soma: [4. 8.]
      