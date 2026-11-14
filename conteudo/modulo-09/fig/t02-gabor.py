from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def filtro_gabor(
    tamanho: int = 81,
    limite: float = 10.0,
    theta_graus: float = 0.0,
    lambd: float = 6.0,
    sigma: float = 3.0,
    psi: float = 0.0,
    gamma: float = 1.0,
) -> np.ndarray:
    eixo = np.linspace(-limite, limite, tamanho)
    x, y = np.meshgrid(eixo, eixo)
    theta = np.deg2rad(theta_graus)
    x_linha = x * np.cos(theta) + y * np.sin(theta)
    y_linha = -x * np.sin(theta) + y * np.cos(theta)
    envelope = np.exp(-(x_linha**2 + (gamma * y_linha) ** 2) / (2.0 * sigma**2))
    onda = np.cos(2.0 * np.pi * x_linha / lambd + psi)
    return envelope * onda


def main() -> None:
    cor_texto = "#475569"
    cor_borda = "#94A3B8"
    orientacoes = [
        (0, r"$\theta = 0^\circ$ (vertical)"),
        (45, r"$\theta = 45^\circ$"),
        (90, r"$\theta = 90^\circ$ (horizontal)"),
        (135, r"$\theta = 135^\circ$"),
    ]

    fig, axes = plt.subplots(1, 4, figsize=(10.6, 3.1), constrained_layout=True)
    fig.patch.set_alpha(0.0)

    imagem = None
    for ax, (ang, titulo) in zip(axes, orientacoes):
        g = filtro_gabor(theta_graus=ang)
        imagem = ax.imshow(
            g,
            cmap="RdBu_r",
            vmin=-1.0,
            vmax=1.0,
            origin="lower",
            extent=[-10, 10, -10, 10],
        )
        ax.axhline(0, color=cor_texto, linestyle="--", linewidth=0.6, alpha=0.35)
        ax.axvline(0, color=cor_texto, linestyle="--", linewidth=0.6, alpha=0.35)
        ax.set_title(titulo, fontsize=10.5, fontweight="bold", color=cor_texto, pad=8)
        ax.set_xticks([-8, 0, 8])
        ax.set_yticks([-8, 0, 8])
        ax.tick_params(colors=cor_texto, labelsize=8.5)
        for spine in ax.spines.values():
            spine.set_color(cor_borda)
            spine.set_linewidth(0.8)

    axes[0].set_ylabel("Posição $y$ (pixels)", fontsize=9.5, color=cor_texto)
    fig.supxlabel("Posição $x$ (pixels)", fontsize=9.5, color=cor_texto)

    cbar = fig.colorbar(imagem, ax=axes, shrink=0.82, pad=0.02)
    cbar.set_label("Peso (ON > 0, OFF < 0)", fontsize=9, color=cor_texto)
    cbar.ax.tick_params(colors=cor_texto, labelsize=8.5)
    cbar.outline.set_edgecolor(cor_borda)

    fig.suptitle(
        r"Filtros de Gabor em 4 orientações ($\lambda = 6$, $\sigma = 3$, $\psi = 0$)",
        fontsize=12,
        fontweight="bold",
        color=cor_texto,
    )

    destino = Path(__file__).resolve().parent / "t02-gabor.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
