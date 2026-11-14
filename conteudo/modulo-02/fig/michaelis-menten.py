from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    v_max = 120.0
    k_m = 2.0

    s = np.linspace(0.0, 20.0, 300)
    v = (v_max * s) / (k_m + s)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_curva = "#4F46E5"
    cor_assintota = "#0D9488"

    fig, ax = plt.subplots(figsize=(6.8, 4.3))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.plot(s, v, color=cor_curva, linewidth=2.5, label=r"$v([S]) = \frac{120\,[S]}{2{,}0 + [S]}$")
    ax.axhline(
        v_max,
        color=cor_assintota,
        linestyle="--",
        linewidth=1.6,
        label=r"Assíntota horizontal: $V_{\max} = 120$",
    )

    # Ponto (K_m, V_max / 2)
    ax.plot([k_m, k_m], [0.0, v_max / 2.0], linestyle=":", linewidth=1.2, color=cor_texto)
    ax.plot([0.0, k_m], [v_max / 2.0, v_max / 2.0], linestyle=":", linewidth=1.2, color=cor_texto)
    ax.scatter([k_m], [v_max / 2.0], color=cor_assintota, s=48, zorder=4)
    ax.annotate(
        r"$(K_m,\, V_{\max}/2) = (2{,}0;\; 60)$",
        xy=(k_m, v_max / 2.0),
        xytext=(5.2, 46.0),
        fontsize=9.5,
        color=cor_texto,
        arrowprops=dict(arrowstyle="->", color=cor_texto, lw=1.1),
    )

    ax.set_xlim(0.0, 20.0)
    ax.set_ylim(0.0, 136.0)
    ax.set_xticks([0, 2, 5, 10, 15, 20])
    ax.set_xticklabels(["0", "2,0\n($K_m$)", "5", "10", "15", "20"])
    ax.set_yticks([0, 30, 60, 90, 120])

    ax.set_xlabel("Concentração de substrato $[S]$ (mmol/L)", fontsize=10, color=cor_texto)
    ax.set_ylabel(r"Velocidade $v([S])$ ($\mu$mol/(L$\cdot$min))", fontsize=10, color=cor_texto)
    ax.set_title(
        "Cinética de Michaelis–Menten e saturação enzimática",
        fontsize=12,
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
    ax.legend(loc="lower right", frameon=True, framealpha=0.85, fontsize=9)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "michaelis-menten.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
