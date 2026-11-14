from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def simular_tentativa(
    V: np.ndarray,
    recompensa: np.ndarray,
    t_estimulo: int,
    gamma: float,
    alpha: float,
    atualizar: bool = True,
) -> np.ndarray:
    T = len(recompensa)
    delta = np.zeros(T)
    for t in range(1, T):
        delta[t] = recompensa[t] + gamma * V[t] - V[t - 1]
        if atualizar and (t - 1) >= t_estimulo:
            V[t - 1] += alpha * delta[t]
    return delta


def main() -> None:
    T = 20
    t_estimulo = 5
    t_recompensa = 15
    gamma = 1.0
    alpha = 0.1
    n_tentativas = 200

    recompensa_padrao = np.zeros(T)
    recompensa_padrao[t_recompensa] = 1.0
    recompensa_omissao = np.zeros(T)

    V = np.zeros(T)
    delta_t1 = np.zeros(T)
    delta_t200 = np.zeros(T)

    for tentativa in range(1, n_tentativas + 1):
        delta = simular_tentativa(V, recompensa_padrao, t_estimulo, gamma, alpha, atualizar=True)
        if tentativa == 1:
            delta_t1 = delta
        elif tentativa == n_tentativas:
            delta_t200 = delta

    delta_omissao = simular_tentativa(V, recompensa_omissao, t_estimulo, gamma, alpha, atualizar=False)

    tempos = np.arange(T)
    paineis = [
        ("Antes do aprendizado (Tentativa 1)", delta_t1, "#4F46E5", "Recompensa"),
        ("Após o aprendizado (Tentativa 200)", delta_t200, "#0D9488", "Recompensa"),
        ("Recompensa omitida (Tentativa 201)", delta_omissao, "#DC2626", "Omissão"),
    ]

    cor_texto = "#475569"
    cor_grade = "#94A3B8"

    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6), sharey=True)
    fig.patch.set_alpha(0.0)

    for ax, (titulo, delta, cor, rotulo_rec) in zip(axes, paineis):
        ax.axhline(0.0, color=cor_grade, linewidth=1.0, zorder=1)
        ax.axvline(t_estimulo, color=cor_grade, linestyle=":", linewidth=1.1, zorder=1)
        ax.axvline(t_recompensa, color=cor_grade, linestyle=":", linewidth=1.1, zorder=1)
        ax.plot(tempos, delta, color=cor, linewidth=2.2, marker="o", markersize=4, zorder=3)

        ax.text(t_estimulo + 0.3, 1.12, "Estímulo", fontsize=8.5, color=cor_texto)
        ax.text(t_recompensa - 0.3, -1.16, rotulo_rec, fontsize=8.5, color=cor_texto, ha="right")

        ax.set_title(titulo, fontsize=10, fontweight="bold", color=cor_texto, pad=10)
        ax.set_xlabel("Instante $t$", fontsize=9.5, color=cor_texto)
        ax.set_xticks([0, 5, 10, 15, 19])
        ax.set_ylim(-1.25, 1.25)

        ax.patch.set_alpha(0.0)
        ax.grid(True, axis="y", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=8.5)

    axes[0].set_ylabel("Erro TD ($\\delta_t$)", fontsize=9.5, color=cor_texto)

    fig.suptitle(
        "Erro de predição de recompensa (TD) como análogo da resposta dopaminérgica",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        y=1.03,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "t09-dopamina-td.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
