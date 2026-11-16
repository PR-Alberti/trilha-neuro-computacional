
import numpy as np

X = np.array([
    [10.0, 30.0, 20.0,  0.0],  # A
    [20.0, 60.0, 40.0,  0.0],  # B (= 2 * A)
    [20.0, 40.0, 30.0, 10.0],  # C (= A + 10)
    [ 0.0, 10.0, 20.0, 30.0],  # D (perfil invertido)
])

X_norm = X / np.linalg.norm(X, axis=1, keepdims=True)
S_cos = X_norm @ X_norm.T
R_pearson = np.corrcoef(X)

print("Similaridade de cossenos:\n", np.round(S_cos, 4))
# [[1.     1.     0.9759 0.5   ]
#  [1.     1.     0.9759 0.5   ]
#  [0.9759 0.9759 1.     0.6343]
#  [0.5    0.5    0.6343 1.    ]]

print("\nCorrelacao de Pearson:\n", np.round(R_pearson, 4))
# [[ 1.   1.   1.  -0.4]
#  [ 1.   1.   1.  -0.4]
#  [ 1.   1.   1.  -0.4]
#  [-0.4 -0.4 -0.4  1. ]]
      