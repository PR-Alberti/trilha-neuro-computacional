from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def ativacao(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return 4.0 * np.exp(-((x - 2.0) ** 2 + (y - 1.0) ** 2) / 8.0)


def gradiente(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    z = ativacao(x, y)
    zx = ((2.0 - x) / 4.0) * z
    zy = ((1.0 - y) / 4.0) * z
    return zx, zy


def main() -> None:
    x_contorno = np.linspace(-2.0, 6.0, 220)
    y_contorno = np.linspace(-3.0, 5.0, 220)
    xc, yc = np.meshgrid(x_contorno, y_contorno)
    zc = ativacao(xc, yc)

    x_grade = np.linspace(-1.5, 5.5, 8)
    y_grade = np.linspace(-2.5, 4.5, 8)
    xg, yg = np.meshgrid(x_grade, y_grade)
    gx, gy = gradiente(xg, yg)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_contorno = "#4F46E5"
    cor_seta = "#0D9488"
    cor_pico = "#E11D48"

    fig, ax = plt.subplots(figsize=(5.8, 5.4))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    niveis = [0.8, 1.6, 2.4, 3.2]
    cs = ax.contour(xc, yc, zc, levels=niveis, colors=cor_contorno, linewidths=1.5, zorder=2)
    ax.clabel(cs, inline=True, fontsize=8.5, fmt="%.1f")

    ax.quiver(
        xg,
        yg,
        gx,
        gy,
        angles="xy",
        scale_units="xy",
        scale=1.6,
        color=cor_seta,
        width=0.0055,
        headwidth=3.8,
        headlength=4.6,
        zorder=4,
        label="Gradiente $\\nabla Z(x, y)$",
    )

    ax.scatter(
        [2.0],
        [1.0],
        color=cor_pico,
        marker="X",
        s=75,
        zorder=5,
        label="Pico de ativação $(2, 1)$",
    )

    ax.set_title(
        "Mapa de ativação cortical $Z(x, y)$ e campo gradiente",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax.set_xlabel("x (mm)", fontsize=10, color=cor_texto)
    ax.set_ylabel("y (mm)", fontsize=10, color=cor_texto)
    ax.set_xlim(-2.0, 6.0)
    ax.set_ylim(-3.0, 5.0)
    ax.set_xticks(np.arange(-2, 7, 1))
    ax.set_yticks(np.arange(-3, 6, 1))
    ax.set_aspect("equal")

    ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left")

    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "gradiente-ativacao.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
