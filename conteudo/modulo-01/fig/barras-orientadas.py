from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def desenhar_campo(
    ax: plt.Axes,
    angulo_barra: float,
    titulo: str,
    rotulo_diff: str,
    eh_preferida: bool = False,
) -> None:
    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_pref = "#4F46E5"
    cor_teste = "#0D9488"

    # Campo receptivo circular
    circulo = patches.Circle(
        (0, 0),
        1.0,
        facecolor=(0.95, 0.97, 0.99, 0.12),
        edgecolor=cor_grade,
        linestyle="--",
        linewidth=1.3,
        zorder=1,
    )
    ax.add_patch(circulo)

    # Eixo horizontal de referencia (0 grau)
    ax.plot([-1.08, 1.08], [0, 0], color=cor_grade, linestyle=":", linewidth=0.9, zorder=2)
    ax.text(1.12, 0.0, "0°", fontsize=8.5, color=cor_grade, va="center", ha="left")

    # Eixo da orientacao preferida (45 graus) como referencia nos paineis de teste
    rad_pref = np.deg2rad(45.0)
    px, py = 0.92 * np.cos(rad_pref), 0.92 * np.sin(rad_pref)
    if not eh_preferida:
        ax.plot(
            [-px, px],
            [-py, py],
            color=cor_pref,
            linestyle="--",
            linewidth=1.3,
            alpha=0.65,
            zorder=2,
        )

    # Barra luminosa de estimulo
    rad = np.deg2rad(angulo_barra)
    bx, by = 0.76 * np.cos(rad), 0.76 * np.sin(rad)
    cor_barra = cor_pref if eh_preferida else cor_teste
    ax.plot(
        [-bx, bx],
        [-by, by],
        color=cor_barra,
        linewidth=6.0,
        solid_capstyle="round",
        zorder=4,
    )

    # Arcos e rotulos angulares
    if eh_preferida:
        arco = patches.Arc(
            (0, 0),
            0.84,
            0.84,
            angle=0,
            theta1=0,
            theta2=45,
            color=cor_pref,
            linewidth=1.4,
            zorder=3,
        )
        ax.add_patch(arco)
        ang_mid = np.deg2rad(22.5)
        ax.text(
            0.60 * np.cos(ang_mid),
            0.60 * np.sin(ang_mid),
            "45°",
            fontsize=9.5,
            fontweight="bold",
            color=cor_pref,
            ha="center",
            va="center",
        )
    elif angulo_barra == 90.0:
        arco = patches.Arc(
            (0, 0),
            0.84,
            0.84,
            angle=0,
            theta1=45,
            theta2=90,
            color=cor_teste,
            linewidth=1.4,
            zorder=3,
        )
        ax.add_patch(arco)
        ang_mid = np.deg2rad(67.5)
        ax.text(
            0.62 * np.cos(ang_mid),
            0.62 * np.sin(ang_mid),
            "45°",
            fontsize=9.5,
            fontweight="bold",
            color=cor_teste,
            ha="center",
            va="center",
        )
    elif angulo_barra == 135.0:
        # Simbolo de angulo reto entre 45 e 135 graus
        s = 0.22
        u1 = np.array([np.cos(np.deg2rad(45.0)), np.sin(np.deg2rad(45.0))])
        u2 = np.array([np.cos(np.deg2rad(135.0)), np.sin(np.deg2rad(135.0))])
        p1 = s * u1
        p2 = s * u1 + s * u2
        p3 = s * u2
        ax.plot(
            [p1[0], p2[0], p3[0]],
            [p1[1], p2[1], p3[1]],
            color=cor_teste,
            linewidth=1.3,
            zorder=3,
        )
        ax.text(
            0.0,
            0.52,
            "90°",
            fontsize=9.5,
            fontweight="bold",
            color=cor_teste,
            ha="center",
            va="center",
        )
    elif angulo_barra == 0.0:
        arco = patches.Arc(
            (0, 0),
            0.84,
            0.84,
            angle=0,
            theta1=0,
            theta2=45,
            color=cor_teste,
            linewidth=1.4,
            zorder=3,
        )
        ax.add_patch(arco)
        ang_mid = np.deg2rad(22.5)
        ax.text(
            0.62 * np.cos(ang_mid),
            0.62 * np.sin(ang_mid),
            "45°",
            fontsize=9.5,
            fontweight="bold",
            color=cor_teste,
            ha="center",
            va="center",
        )

    ax.set_title(titulo, fontsize=10.5, fontweight="bold", color=cor_texto, pad=6)
    ax.text(
        0.0,
        -1.26,
        rotulo_diff,
        fontsize=9.5,
        color=cor_pref if eh_preferida else cor_texto,
        fontweight="bold" if eh_preferida else "normal",
        ha="center",
        va="center",
    )

    ax.set_aspect("equal")
    ax.set_xlim(-1.25, 1.35)
    ax.set_ylim(-1.42, 1.18)
    ax.axis("off")


def main() -> None:
    cor_texto = "#475569"

    fig, axes = plt.subplots(1, 4, figsize=(10.4, 3.3))
    fig.patch.set_alpha(0.0)

    configuracoes = [
        (45.0, "Barra a 45° (preferida)", "$\\Delta\\theta = 0^\\circ$ (máxima)", True),
        (90.0, "Barra a 90°", "$\\Delta\\theta = 45^\\circ$", False),
        (135.0, "Barra a 135°", "$\\Delta\\theta = 90^\\circ$ (perpendicular)", False),
        (0.0, "Barra a 0°", "$\\Delta\\theta = 45^\\circ$", False),
    ]

    for ax, (ang, titulo, rotulo, pref) in zip(axes, configuracoes):
        ax.patch.set_alpha(0.0)
        desenhar_campo(ax, ang, titulo, rotulo, eh_preferida=pref)

    fig.suptitle(
        "Campo receptivo em V1 com orientação preferida de 45° (linha tracejada)",
        fontsize=12,
        fontweight="bold",
        color=cor_texto,
        y=1.02,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "barras-orientadas.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
