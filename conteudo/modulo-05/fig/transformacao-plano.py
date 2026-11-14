from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def desenhar_painel(
    ax: plt.Axes,
    A: np.ndarray,
    titulo: str,
    prefixo: str,
    cor_area: str,
) -> None:
    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_e1 = "#4F46E5"  # índigo para e_1 e sua imagem
    cor_e2 = "#0D9488"  # verde-azulado para e_2 e sua imagem

    ax.patch.set_alpha(0.0)
    ax.set_aspect("equal")
    ax.set_xlim(-2.1, 2.5)
    ax.set_ylim(-2.1, 2.5)
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_yticks([-2, -1, 0, 1, 2])

    # Eixos originais discretos ao fundo
    ax.axhline(0, color=cor_grade, linewidth=0.9, linestyle="--", alpha=0.55, zorder=1)
    ax.axvline(0, color=cor_grade, linewidth=0.9, linestyle="--", alpha=0.55, zorder=1)

    # Grade unitária transformada pela matriz A
    valores_grade = np.arange(-4, 5)
    t = np.linspace(-4.5, 4.5, 2)
    for k in valores_grade:
        # Retas originalmente verticais (x = k)
        pts_v = A @ np.vstack([np.full_like(t, k), t])
        ax.plot(
            pts_v[0],
            pts_v[1],
            color=cor_grade,
            linewidth=0.75,
            alpha=0.45,
            zorder=1,
        )
        # Retas originalmente horizontais (y = k)
        pts_h = A @ np.vstack([t, np.full_like(t, k)])
        ax.plot(
            pts_h[0],
            pts_h[1],
            color=cor_grade,
            linewidth=0.75,
            alpha=0.45,
            zorder=1,
        )

    # Imagens dos vetores da base canônica e do quadrado unitário
    v1 = A @ np.array([1.0, 0.0])
    v2 = A @ np.array([0.0, 1.0])
    v12 = v1 + v2

    vertices = np.array([[0.0, 0.0], v1, v12, v2])
    poligono_preenchido = patches.Polygon(
        vertices,
        closed=True,
        facecolor=cor_area,
        edgecolor="none",
        alpha=0.18,
        zorder=2,
    )
    poligono_borda = patches.Polygon(
        vertices,
        closed=True,
        facecolor="none",
        edgecolor=cor_area,
        linewidth=1.3,
        linestyle="-",
        alpha=0.75,
        zorder=3,
    )
    ax.add_patch(poligono_preenchido)
    ax.add_patch(poligono_borda)

    # Setas de e_1 e e_2 transformados
    ax.quiver(
        0,
        0,
        v1[0],
        v1[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color=cor_e1,
        width=0.016,
        headwidth=4.2,
        headlength=5.2,
        zorder=5,
    )
    ax.quiver(
        0,
        0,
        v2[0],
        v2[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color=cor_e2,
        width=0.016,
        headwidth=4.2,
        headlength=5.2,
        zorder=5,
    )

    # Rótulos próximos às pontas dos vetores
    rotulo_1 = "$\\mathbf{e}_1$" if prefixo == "" else f"${prefixo}\\mathbf{{e}}_1$"
    rotulo_2 = "$\\mathbf{e}_2$" if prefixo == "" else f"${prefixo}\\mathbf{{e}}_2$"

    desloc_1 = np.array([0.12, -0.22]) if v1[1] >= 0 else np.array([0.12, -0.24])
    desloc_2 = np.array([-0.55, 0.14]) if v2[0] <= 0 else np.array([0.10, 0.14])
    if prefixo == "\\mathbf{M}":
        desloc_1 = np.array([0.10, 0.12])
        desloc_2 = np.array([0.10, -0.24])
    elif prefixo == "\\mathbf{C}":
        desloc_1 = np.array([0.08, -0.26])
        desloc_2 = np.array([-0.15, 0.16])

    ax.text(
        v1[0] + desloc_1[0],
        v1[1] + desloc_1[1],
        rotulo_1,
        color=cor_e1,
        fontsize=10,
        fontweight="bold",
        zorder=6,
    )
    ax.text(
        v2[0] + desloc_2[0],
        v2[1] + desloc_2[1],
        rotulo_2,
        color=cor_e2,
        fontsize=10,
        fontweight="bold",
        zorder=6,
    )

    ax.set_title(titulo, fontsize=10.5, fontweight="bold", color=cor_texto, pad=10)
    ax.set_xlabel("$x$", fontsize=9.5, color=cor_texto)
    ax.set_ylabel("$y$", fontsize=9.5, color=cor_texto)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=8.5)


def main() -> None:
    cor_texto = "#475569"
    cor_pos = "#4F46E5"   # índigo para det > 0 (mantém orientação)
    cor_neg = "#D97706"   # âmbar para det < 0 (inverte orientação)

    I = np.array([[1.0, 0.0], [0.0, 1.0]])
    ang = np.deg2rad(45.0)
    R = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
    C = np.array([[1.0, 1.0], [0.0, 1.0]])
    M = np.array([[1.0, 1.0], [1.0, -1.0]])

    paineis = [
        (
            I,
            "Original (identidade)\nI = [[1, 0], [0, 1]]  |  det = 1",
            "",
            cor_pos,
        ),
        (
            R,
            "Rotação de 45°\nR ≈ [[0,71, −0,71], [0,71, 0,71]]  |  det = 1",
            "\\mathbf{R}",
            cor_pos,
        ),
        (
            C,
            "Cisalhamento horizontal\nC = [[1, 1], [0, 1]]  |  det = 1",
            "\\mathbf{C}",
            cor_pos,
        ),
        (
            M,
            "Soma e diferença (inverte orientação)\nM = [[1, 1], [1, −1]]  |  det = −2",
            "\\mathbf{M}",
            cor_neg,
        ),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(9.2, 8.4))
    fig.patch.set_alpha(0.0)

    for ax, (A, titulo, prefixo, cor_area) in zip(axes.ravel(), paineis):
        desenhar_painel(ax, A, titulo, prefixo, cor_area)

    fig.suptitle(
        "Matrizes 2×2 como transformações do plano: colunas = imagens de $\\mathbf{e}_1$ e $\\mathbf{e}_2$",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        y=0.99,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    destino = Path(__file__).resolve().parent / "transformacao-plano.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
