
import numpy as np

def simular_tentativa(V, recompensa, t_est=5, gamma=1.0, alpha=0.1, atualizar=True):
    delta = np.zeros_like(recompensa)
    for t in range(1, len(recompensa)):
        delta[t] = recompensa[t] + gamma * V[t] - V[t - 1]
        if atualizar and (t - 1) >= t_est:
            V[t - 1] += alpha * delta[t]
    return delta

T, t_est, t_rec = 20, 5, 15
rec = np.zeros(T); rec[t_rec] = 1.0
V = np.zeros(T)

for tentativa in range(1, 201):
    d = simular_tentativa(V, rec, t_est=t_est, gamma=1.0, alpha=0.1, atualizar=True)
    if tentativa in (1, 200):
        print(f"Tentativa {tentativa:3d} -> delta_est={d[t_est]:.3f}, delta_rec={d[t_rec]:.3f}")

d_om = simular_tentativa(V, np.zeros(T), t_est=t_est, gamma=1.0, alpha=0.1, atualizar=False)
print(f"Omissão (201) -> delta_est={d_om[t_est]:.3f}, delta_rec={d_om[t_rec]:.3f}")

# Tentativa   1 -> delta_est=0.000, delta_rec=1.000
# Tentativa 200 -> delta_est≈0.996, delta_rec≈0.000
# Omissão (201) -> delta_est≈0.996, delta_rec=-1.000
        