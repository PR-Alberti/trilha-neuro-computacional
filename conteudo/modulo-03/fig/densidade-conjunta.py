import math
from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    grade = np.linspace(-3.0, 3.0, 240)
    x_grid, y_grid = np.meshgrid(grade, grade)
    densidade = (1.0 / (2.0 * np.pi)) * np.exp(-0.5 * (x_grid**2 + y_grid**2))

    prob_ret = (math.erf(1.0 / math.sqrt(2.0))) ** 2
    prob_r1 = 1.0 - math.exp(-0.5)
    prob_r2 = 1.0 - math.exp(-2.0)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_indigo = "#4F46E5"
    cor_teal = "#0D9488"

    fig, (ax_ret, ax_circ) = plt.subplots(1, 2, figsize=(9.8, 4.5))
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: integração em um retângulo [-1, 1] x [-1, 1]
    ax_ret.contourf(x_grid, y_grid, densidade, levels=12, cmap="PuBu", alpha=0.85)
    retangulo = patches.Rectangle(
        (-1.0, -1.0),
        2.0,
        2.0,
        fill=False,
        edgecolor=cor_indigo,
        linewidth=2.4,
        zorder=4,
    )
    ax_ret.add_patch(retangulo)
    ax_ret.text(
        0.0,
        0.0,
        f"$P([-1, 1]^2) \\approx {prob_ret * 100:.1f}\\%$".replace(".", ","),
        color=cor_indigo,
        fontsize=9.5,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=5,
        bbox=dict(boxstyle="round,pad=0.28", facecolor="white", edgecolor=cor_indigo, linewidth=0.9, alpha=0.88),
    )
    ax_ret.set_title(
        "Região retangular $[-1, 1]^2$",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    # Painel direito: integração em discos de raio 1 e 2 (em unidades de sigma)
    ax_circ.contourf(x_grid, y_grid, densidade, levels=12, cmap="PuBu", alpha=0.85)
    circulo_1 = patches.Circle(
        (0.0, 0.0),
        1.0,
        fill=False,
        edgecolor=cor_teal,
        linewidth=2.2,
        zorder=4,
    )
    circulo_2 = patches.Circle(
        (0.0, 0.0),
        2.0,
        fill=False,
        edgecolor=cor_indigo,
        linewidth=2.2,
        linestyle="--",
        zorder=4,
    )
    ax_circ.add_patch(circulo_1)
    ax_circ.add_patch(circulo_2)

    ax_circ.text(
        0.0,
        0.0,
        f"$r \\leq 1\\sigma$: $\\approx {prob_r1 * 100:.1f}\\%$".replace(".", ","),
        color=cor_teal,
        fontsize=9.2,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=5,
        bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=cor_teal, linewidth=0.9, alpha=0.88),
    )
    ax_circ.text(
        0.0,
        -2.38,
        f"$r \\leq 2\\sigma$: $\\approx {prob_r2 * 100:.1f}\\%$".replace(".", ","),
        color=cor_indigo,
        fontsize=9.2,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=5,
        bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=cor_indigo, linewidth=0.9, alpha=0.88),
    )
    ax_circ.set_title(
        "Discos polares ($r \\leq \\sigma$ e $r \\leq 2\\sigma$)",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    for ax in (ax_ret, ax_circ):
        ax.set_aspect("equal")
        ax.set_xlim(-3.0, 3.0)
        ax.set_ylim(-3.0, 3.0)
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([-2, -1, 0, 1, 2])
        ax.set_xlabel("$x$ (unidades de $\\sigma$)", fontsize=10, color=cor_texto)
        ax.set_ylabel("$y$ (unidades de $\\sigma$)", fontsize=10, color=cor_texto)
        ax.patch.set_alpha(0.0)
        ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    fig.suptitle(
        "Densidade gaussiana circular padrão: $p(x, y) = \\frac{1}{2\\pi} e^{-(x^2 + y^2)/2}$",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        y=1.02,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "densidade-conjunta.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
