from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    x = np.linspace(-2.0, 2.0, 250)
    y = np.linspace(-2.0, 2.0, 250)
    X, Y = np.meshgrid(x, y)

    Z_min = X**2 + Y**2
    Z_sela = X**2 - Y**2

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_pos = "#0D9488"
    cor_neg = "#4F46E5"
    cor_zero = "#64748B"
    cor_ponto = "#E11D48"

    fig, (ax_min, ax_sela) = plt.subplots(1, 2, figsize=(9.8, 4.4))
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: mínimo em (0, 0) para f(x, y) = x^2 + y^2
    niveis_min = [0.5, 1.0, 2.0, 3.0, 4.0, 6.0]
    cs_min = ax_min.contour(
        X, Y, Z_min, levels=niveis_min, colors=cor_pos, linewidths=1.3, linestyles="solid"
    )
    ax_min.clabel(cs_min, inline=True, fontsize=8, fmt="%.1f")
    ax_min.scatter([0.0], [0.0], color=cor_ponto, s=65, zorder=5)
    ax_min.annotate(
        "mínimo",
        xy=(0.0, 0.0),
        xytext=(0.45, 1.20),
        color=cor_ponto,
        fontsize=9.5,
        fontweight="bold",
        arrowprops={"arrowstyle": "->", "color": cor_ponto, "lw": 1.2},
        zorder=6,
    )
    ax_min.set_title(
        "Mínimo: $f(x, y) = x^2 + y^2$",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    # Painel direito: ponto de sela em (0, 0) para f(x, y) = x^2 - y^2
    niveis_neg = [-3.0, -2.0, -1.0, -0.5]
    niveis_pos = [0.5, 1.0, 2.0, 3.0]
    cs_neg = ax_sela.contour(
        X, Y, Z_sela, levels=niveis_neg, colors=cor_neg, linewidths=1.3, linestyles="dashed"
    )
    ax_sela.clabel(cs_neg, inline=True, fontsize=8, fmt="%.1f")
    ax_sela.contour(
        X, Y, Z_sela, levels=[0.0], colors=cor_zero, linewidths=1.1, linestyles="dotted"
    )
    cs_pos = ax_sela.contour(
        X, Y, Z_sela, levels=niveis_pos, colors=cor_pos, linewidths=1.3, linestyles="solid"
    )
    ax_sela.clabel(cs_pos, inline=True, fontsize=8, fmt="%.1f")
    ax_sela.scatter([0.0], [0.0], color=cor_ponto, s=65, zorder=5)
    ax_sela.annotate(
        "ponto de sela",
        xy=(0.0, 0.0),
        xytext=(0.45, 1.20),
        color=cor_ponto,
        fontsize=9.5,
        fontweight="bold",
        arrowprops={"arrowstyle": "->", "color": cor_ponto, "lw": 1.2},
        zorder=6,
    )
    ax_sela.set_title(
        "Ponto de sela: $f(x, y) = x^2 - y^2$",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    # Estilo compartilhado
    for ax in (ax_min, ax_sela):
        ax.patch.set_alpha(0.0)
        ax.set_aspect("equal")
        ax.set_xlim(-2.0, 2.0)
        ax.set_ylim(-2.0, 2.0)
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([-2, -1, 0, 1, 2])
        ax.set_xlabel("$x$", fontsize=10, color=cor_texto)
        ax.set_ylabel("$y$", fontsize=10, color=cor_texto)
        ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "minimo-sela.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
