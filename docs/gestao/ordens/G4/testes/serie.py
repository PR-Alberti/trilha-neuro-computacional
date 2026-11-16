import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold, cross_val_score
rng = np.random.default_rng(0)
janela = np.ones(10) / 10.0
bruto_X = rng.normal(0.0, 1.0, size=(309, 5))
X = np.column_stack([np.convolve(bruto_X[:, j], janela, mode="valid") for j in range(5)])
bruto_y = rng.normal(0.0, 1.0, size=309)
y = np.convolve(bruto_y, janela, mode="valid")
modelo = KNeighborsRegressor(n_neighbors=5)
r2_embaralhado = cross_val_score(modelo, X, y, cv=KFold(n_splits=5, shuffle=True, random_state=0), scoring="r2").mean()
r2_blocos = cross_val_score(modelo, X, y, cv=KFold(n_splits=5, shuffle=False), scoring="r2").mean()
print(f"R² com KFold(shuffle=True) : {r2_embaralhado:.3f}")
print(f"R² com blocos contíguos    : {r2_blocos:.3f}")
