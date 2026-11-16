
import numpy as np
from sklearn.linear_model import RidgeCV

rng = np.random.default_rng(0)
n_trs, d, n_voxels = 600, 20, 50

# Embeddings semânticos aleatórios (um vetor por TR)
X = rng.standard_normal((n_trs, d))

# BOLD simulado: combinação linear das características de 2 TRs atrás + ruído
W_verd = rng.standard_normal((d, n_voxels)) / np.sqrt(d)
ruido = 0.5 * rng.standard_normal((n_trs, n_voxels))
Y = np.zeros((n_trs, n_voxels))
Y[2:] = X[:-2] @ W_verd + ruido[2:]
Y[:2] = ruido[:2]

# Alinha alvo para t = 3..599 (597 TRs) com atrasos de 1, 2 e 3 TRs
Y_alvo = Y[3:]
X_sem_atraso = X[3:]
X_com_atraso = np.hstack([X[2:-1], X[1:-2], X[:-3]])

# Divisão contígua (sem embaralhar TRs!)
corte = 450
alphas = np.logspace(-1, 3, 9)


def corr_media(y_real, y_pred):
    return float(np.mean([np.corrcoef(y_real[:, j], y_pred[:, j])[0, 1] for j in range(y_real.shape[1])]))


m_sem = RidgeCV(alphas=alphas).fit(X_sem_atraso[:corte], Y_alvo[:corte])
m_com = RidgeCV(alphas=alphas).fit(X_com_atraso[:corte], Y_alvo[:corte])

r_sem = corr_media(Y_alvo[corte:], m_sem.predict(X_sem_atraso[corte:]))
r_com = corr_media(Y_alvo[corte:], m_com.predict(X_com_atraso[corte:]))

print(f"Correlação média (sem atraso) ≈ {r_sem:.3f}")
print(f"Correlação média (atrasos 1-3 TRs) ≈ {r_com:.3f}")
# Saída esperada (valores aproximados; podem variar levemente):
# Correlação média (sem atraso) ≈ 0.00
# Correlação média (atrasos 1-3 TRs) ≈ 0.87
      