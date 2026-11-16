
import numpy as np
import torch
import torch.nn.functional as F
from sklearn.datasets import load_digits
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(0)
torch.manual_seed(0)

# 1. Extrai características convolucionais (12 filtros 3x3 + ReLU + MaxPool 2x2)
digitos = load_digits()
X_img = torch.from_numpy((digitos.images / 16.0).astype(np.float32)).unsqueeze(1)
filtros = torch.randn(12, 1, 3, 3) * 0.3

with torch.no_grad():
    ativacoes = F.max_pool2d(F.relu(F.conv2d(X_img, filtros, padding=1)), kernel_size=2)
    A = ativacoes.flatten(start_dim=1).numpy()  # (1797, 192)

print("Formato da matriz de ativações:", A.shape)  # (1797, 192)

# 2. Simula 5 neurônios corticais com ruído biológico
n_neuronios = 5
W_verdadeiro = rng.normal(0.0, 0.2, size=(A.shape[1], n_neuronios))
Y_limpo = 10.0 + A @ W_verdadeiro
Y_observado = Y_limpo + rng.normal(0.0, 0.4, size=Y_limpo.shape)

# 3. Divide em treino e teste; simula experimento real com poucos estímulos (n=150 < d=192)
A_tr, A_te, Y_tr, Y_te, _, Y_te_limpo = train_test_split(
    A, Y_observado, Y_limpo, test_size=0.2, random_state=0
)
A_fit, Y_fit = A_tr[:150], Y_tr[:150]

# Sem regularização: tende a sobreajustar fortemente quando n < d
ols = LinearRegression().fit(A_fit, Y_fit)
r2_ols = r2_score(Y_te, ols.predict(A_te), multioutput="raw_values")

# Com regressão ridge e escolha de alpha por validação cruzada
ridge = RidgeCV(alphas=[0.1, 1.0, 10.0, 50.0, 100.0]).fit(A_fit, Y_fit)
r2_ridge = r2_score(Y_te, ridge.predict(A_te), multioutput="raw_values")
teto_ruido = r2_score(Y_te, Y_te_limpo, multioutput="raw_values")

print(f"R² médio de teste (LinearRegression): {r2_ols.mean():.3f}")
print(f"R² médio de teste (RidgeCV, alpha={ridge.alpha_}): {r2_ridge.mean():.3f}")
print(f"Teto de ruído empírico médio: {teto_ruido.mean():.3f}")
# Resultados esperados aproximados (variam um pouco entre versões/máquinas):
# R² médio de teste (LinearRegression) ≈ bem abaixo do teto (frequentemente < 0 ou baixo)
# R² médio de teste (RidgeCV) ≈ próximo de 0.70–0.85, perto do teto de ruído empírico
      