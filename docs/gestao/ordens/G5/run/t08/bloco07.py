
import numpy as np
from sklearn.linear_model import RidgeCV

rng = np.random.default_rng(0)
n_trs, d, n_voxels = 400, 10, 20
X = rng.standard_normal((n_trs, d))
W = rng.standard_normal((d, n_voxels)) / np.sqrt(d)
Y = np.zeros((n_trs, n_voxels))
Y[3:] = X[:-3] @ W + 0.5 * rng.standard_normal((n_trs - 3, n_voxels))

Y_alvo = Y[4:]
corte = 300
for k in range(5):
    Xk = X[4 - k : n_trs - k]
    modelo = RidgeCV(alphas=np.logspace(-1, 3, 9)).fit(Xk[:corte], Y_alvo[:corte])
    pred = modelo.predict(Xk[corte:])
    r = np.mean([np.corrcoef(Y_alvo[corte:, j], pred[:, j])[0, 1] for j in range(n_voxels)])
    print(f"Atraso k={k}: r ≈ {r:.3f}")
# O pico aparece claramente em k=3 (r ≈ 0.88), enquanto k != 3 fica perto de 0.00.
          