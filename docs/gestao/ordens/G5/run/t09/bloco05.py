
import numpy as np

rng = np.random.default_rng(0)
acoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Q = np.zeros((4, 4, 4))
alpha, gamma, eps = 0.5, 0.9, 0.1

for _ in range(500):
    linha, col = 0, 0
    for _ in range(200):
        if rng.random() < eps:
            a = int(rng.integers(4))
        else:
            q_vals = Q[linha, col]
            a = int(rng.choice(np.flatnonzero(q_vals == q_vals.max())))

        dl, dc = acoes[a]
        nl = min(max(linha + dl, 0), 3)
        nc = min(max(col + dc, 0), 3)
        objetivo = (nl == 3 and nc == 3)
        armadilha = (nl == 1 and nc == 1)
        terminou = objetivo or armadilha
        r = 1.0 if objetivo else (-1.0 if armadilha else 0.0)

        alvo = r if terminou else r + gamma * Q[nl, nc].max()
        Q[linha, col, a] += alpha * (alvo - Q[linha, col, a])
        linha, col = nl, nc
        if terminou:
            break

linha, col, passos = 0, 0, 0
while not (linha == 3 and col == 3) and passos < 20:
    dl, dc = acoes[int(np.argmax(Q[linha, col]))]
    linha = min(max(linha + dl, 0), 3)
    col = min(max(col + dc, 0), 3)
    passos += 1
print(f"Q*(início) ≈ {Q[0, 0].max():.3f}, Passos: {passos}")  # Q*(início) ≈ 0.590, Passos: 6
          