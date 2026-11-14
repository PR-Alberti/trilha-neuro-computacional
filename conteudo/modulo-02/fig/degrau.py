from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    v_lim = -55.0
    v_esq = np.linspace(-80.0, v_lim, 100)
    v_dir = np.linspace(v_lim, -30.0, 100)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_curva = "#4F46E5"
    cor_limiar = "#0D9488"

    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    # Ramos da função degrau H(V - V_lim) com H(0) = 1
    ax.plot(v_esq, np.zeros_like(v_esq), color=cor_curva, linewidth=2.6)
    ax.plot(v_dir, np.ones_like(v_dir), color=cor_curva, linewidth=2.6)

    # Linha vertical no limiar
    ax.axvline(v_lim, color=cor_limiar, linestyle="--", linewidth=1.3, alpha=0.85)

    # Bolinha vazia em (-55, 0) e bolinha cheia em (-55, 1)
    ax.scatter([v_lim], [0.0], s=60, facecolor="white", edgecolor=cor_curva, linewidth=2.2, zorder=4)
    ax.scatter([v_lim], [1.0], s=60, facecolor=cor_curva, edgecolor=cor_curva, linewidth=2.2, zorder=4)

    ax.annotate(
        "Limite à esquerda $= 0$",
        xy=(-56.2, 0.04),
        xytext=(-76.0, 0.24),
        fontsize=9.2,
        color=cor_texto,
        arrowprops=dict(arrowstyle="->", color=cor_texto, lw=1.0),
    )
    ax.annotate(
        "Limite à direita $= 1$\ne $H(0) = 1$",
        xy=(-53.8, 0.96),
        xytext=(-44.5, 0.72),
        fontsize=9.2,
        color=cor_texto,
        arrowprops=dict(arrowstyle="->", color=cor_texto, lw=1.0),
    )

    ax.set_xlim(-80.0, -30.0)
    ax.set_ylim(-0.18, 1.22)
    ax.set_xticks([-80, -70, -55, -40, -30])
    ax.set_xticklabels(["-80", "-70\n(repouso)", "-55\n($V_{\\mathrm{lim}}$)", "-40", "-30"])
    ax.set_yticks([0.0, 0.5, 1.0])
    ax.set_yticklabels(["0", "0,5", "1"])

    ax.set_xlabel("Potencial de membrana $V$ (mV)", fontsize=10, color=cor_texto)
    ax.set_ylabel("Resposta $H(V - V_{\\mathrm{lim}})$", fontsize=10, color=cor_texto)
    ax.set_title(
        "Disparo tudo-ou-nada como função degrau de Heaviside",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "degrau.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
