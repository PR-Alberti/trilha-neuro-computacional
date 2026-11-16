
import numpy as np

def amostrar_top_k(logits, k, temperatura=1.0, rng=None):
    if rng is None:
        rng = np.random.default_rng(0)
    z = logits / temperatura
    top_idx = np.argsort(z)[-k:]
    mascara = np.full_like(z, -np.inf, dtype=float)
    mascara[top_idx] = z[top_idx]
    exp_z = np.exp(mascara - np.max(mascara))
    probs = exp_z / np.sum(exp_z)
    return int(rng.choice(len(logits), p=probs)), probs

rng = np.random.default_rng(0)
idx, p = amostrar_top_k(np.array([2.0, 1.0, 0.5, -1.0]), k=2, temperatura=1.0, rng=rng)
print("Probs top-2:", np.round(p, 4), "| sorteado:", idx)
# Probs top-2: [0.7311 0.2689 0.     0.    ] | sorteado: 0
          