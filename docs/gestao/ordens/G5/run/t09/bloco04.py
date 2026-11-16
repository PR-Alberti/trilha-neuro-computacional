
import numpy as np

rng = np.random.default_rng(0)
acoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
setas = ["↑", "↓", "←", "→"]

Q = np.zeros((4, 4, 4))
alpha, gamma, eps = 0.5, 0.9, 0.1

for _ in range(500):
    linha, col = 0, 0
    for _ in range(200):
        if rng.random() < eps:
            a = int(rng.integers(4))
        else:
            q_vals = Q[linha, col]
            melhores = np.flatnonzero(q_vals == q_vals.max())
            a = int(rng.choice(melhores))

        dl, dc = acoes[a]
        nl = min(max(linha + dl, 0), 3)
        nc = min(max(col + dc, 0), 3)
        terminou = (nl == 3 and nc == 3)
        r = 1.0 if terminou else 0.0

        alvo = r if terminou else r + gamma * Q[nl, nc].max()
        Q[linha, col, a] += alpha * (alvo - Q[linha, col, a])
        linha, col = nl, nc
        if terminou:
            break

print(f"Q*(início, melhor ação) ≈ {Q[0, 0].max():.3f} (teórico: {gamma**5:.3f})")

for i in range(4):
    linha_str = ["G" if (i == 3 and j == 3) else setas[int(np.argmax(Q[i, j]))] for j in range(4)]
    print(" ".join(linha_str))

linha, col, passos = 0, 0, 0
while not (linha == 3 and col == 3) and passos < 20:
    a = int(np.argmax(Q[linha, col]))
    dl, dc = acoes[a]
    linha = min(max(linha + dl, 0), 3)
    col = min(max(col + dc, 0), 3)
    passos += 1
print(f"Passos do caminho guloso: {passos}")

# Q*(início, melhor ação) ≈ 0.590 (teórico: 0.590)
# (Grade 4x4 com setas → e ↓ apontando até G; células fora do caminho ótimo variam conforme os empates)
# Passos do caminho guloso: 6
        