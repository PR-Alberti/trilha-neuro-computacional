
import numpy as np

E = np.array([
    [ 1.0,  2.0,  0.0],
    [-1.0, -2.0,  0.0],
    [ 2.0,  4.0,  0.0],
    [ 0.0,  0.0,  3.0],
])
E_norm = E / np.linalg.norm(E, axis=1, keepdims=True)
D_cos = 1.0 - (E_norm @ E_norm.T)
D_busca = D_cos.copy()
np.fill_diagonal(D_busca, np.inf)

print("Distancias do item 0:", np.round(D_cos[0], 3))      # [0. 2. 0. 1.]
print("Vizinho mais proximo:", int(np.argmin(D_busca[0])))  # 2
          