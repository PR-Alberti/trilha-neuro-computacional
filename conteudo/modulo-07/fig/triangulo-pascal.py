from math import comb
from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    max_n = 8
    cor_texto = "#475569"
    cor_escuro = "#1E293B"
    cor_borda = "#CBD5E1"
    cor_fundo_padrao = "#F8FAFC"
    cor_stifel_pai = "#4F46E5"
    cor_stifel_filho = "#0D9488"

    fig, ax = plt.subplots(figsize=(9.6, 5.4))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    dx = 1.05
    dy = 0.92

    # Coordenadas dos nós (linha n, coluna k)
    posicoes: dict[tuple[int, int], tuple[float, float]] = {}
    for n in range(max_n + 1):
        y = (max_n - n) * dy
        for k in range(n + 1):
            x = (k - n / 2.0) * dx
            posicoes[(n, k)] = (x, y)

    # Setas discretas destacando a relação de Stifel: C(6,2) + C(6,3) = C(7,3)
    destaque_pais = {(6, 2), (6, 3)}
    destaque_filho = (7, 3)

    for pai in destaque_pais:
        x0, y0 = posicoes[pai]
        x1, y1 = posicoes[destaque_filho]
        ax.annotate(
            "",
            xy=(x1, y1 + 0.25),
            xytext=(x0, y0 - 0.25),
            arrowprops=dict(
                arrowstyle="->",
                color=cor_stifel_filho,
                lw=1.8,
                shrinkA=2,
                shrinkB=2,
            ),
            zorder=2,
        )

    # Desenho das células do triângulo
    for n in range(max_n + 1):
        y_linha = (max_n - n) * dy
        ax.text(
            -(max_n / 2.0 + 0.95) * dx,
            y_linha,
            f"n = {n}",
            ha="right",
            va="center",
            fontsize=9.5,
            fontweight="bold",
            color=cor_texto,
        )
        ax.text(
            (max_n / 2.0 + 0.95) * dx,
            y_linha,
            f"soma = {2**n}",
            ha="left",
            va="center",
            fontsize=9.0,
            color=cor_texto,
        )

        for k in range(n + 1):
            x, y = posicoes[(n, k)]
            valor = comb(n, k)

            if (n, k) in destaque_pais:
                fundo = "#EEF2FF"
                borda = cor_stifel_pai
                texto_cor = cor_stifel_pai
                lw = 1.8
            elif (n, k) == destaque_filho:
                fundo = "#CCFBF1"
                borda = cor_stifel_filho
                texto_cor = "#0F766E"
                lw = 1.8
            else:
                fundo = cor_fundo_padrao
                borda = cor_borda
                texto_cor = cor_escuro
                lw = 1.0

            caixa = patches.FancyBboxPatch(
                (x - 0.36, y - 0.24),
                0.72,
                0.48,
                boxstyle="round,pad=0.04,rounding_size=0.12",
                facecolor=fundo,
                edgecolor=borda,
                linewidth=lw,
                zorder=3,
            )
            ax.add_patch(caixa)
            ax.text(
                x,
                y,
                str(valor),
                ha="center",
                va="center",
                fontsize=10,
                fontweight="bold" if (n, k) in destaque_pais or (n, k) == destaque_filho else "normal",
                color=texto_cor,
                zorder=4,
            )

    # Anotação explicativa da relação de Stifel
    ax.text(
        0.0,
        -0.78,
        "Relação de Stifel destacada: C(6, 2) + C(6, 3) = 15 + 20 = 35 = C(7, 3)",
        ha="center",
        va="center",
        fontsize=9.8,
        fontweight="bold",
        color="#0F766E",
    )

    ax.set_xlim(-(max_n / 2.0 + 2.1) * dx, (max_n / 2.0 + 2.4) * dx)
    ax.set_ylim(-1.15, max_n * dy + 0.65)
    ax.axis("off")

    ax.set_title(
        "Triângulo de Pascal (linhas n = 0 até n = 8)",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        pad=8,
    )

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "triangulo-pascal.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
