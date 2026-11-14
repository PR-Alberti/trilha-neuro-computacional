from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    r_max = 80.0
    i_50 = 0.5
    s = 0.1

    corrente = np.linspace(0.0, 1.0, 300)
    taxa = r_max / (1.0 + np.exp(-(corrente - i_50) / s))

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_curva = "#4F46E5"
    cor_destaque = "#0D9488"

    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    # Curva sigmoide f-I
    ax.plot(corrente, taxa, color=cor_curva, linewidth=2.4, label="Curva $f$-$I$: $r(I)$")

    # Assintota horizontal r_max
    ax.axhline(
        r_max,
        color=cor_destaque,
        linestyle="--",
        linewidth=1.5,
        label="Assíntota: $r_{\\mathrm{max}} = 80$ Hz",
    )

    # Ponto de meia resposta (I_50, r_max / 2)
    r_meio = r_max / 2.0
    ax.plot([i_50, i_50], [0.0, r_meio], color=cor_grade, linestyle=":", linewidth=1.3)
    ax.plot([0.0, i_50], [r_meio, r_meio], color=cor_grade, linestyle=":", linewidth=1.3)
    ax.scatter([i_50], [r_meio], color=cor_destaque, s=46, zorder=4)

    ax.annotate(
        "Meia resposta\n$(I_{50},\\ r_{\\mathrm{max}}/2) = (0{,}5\\ \\mathrm{nA},\\ 40\\ \\mathrm{Hz})$",
        xy=(i_50, r_meio),
        xytext=(0.57, 25.0),
        fontsize=8.8,
        color=cor_texto,
        arrowprops={"arrowstyle": "->", "color": cor_texto, "lw": 1.0},
    )

    ax.text(
        0.03,
        r_max + 2.2,
        "Saturação ($r_{\\mathrm{max}} = 80$ Hz)",
        fontsize=8.8,
        color=cor_destaque,
        fontweight="bold",
    )

    ax.set_title(
        "Curva $f$-$I$ sigmoide logística",
        fontsize=12,
        fontweight="bold",
        color=cor_texto,
        pad=12,
    )
    ax.set_xlabel("Corrente injetada $I$ (nA)", fontsize=10, color=cor_texto)
    ax.set_ylabel("Taxa de disparo $r(I)$ (Hz)", fontsize=10, color=cor_texto)

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 92.0)
    ax.set_xticks([0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0])
    ax.set_yticks([0, 20, 40, 60, 80])
    ax.xaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{x:.1f}".replace(".", ","))
    )

    ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(loc="lower right", frameon=False, fontsize=8.8, labelcolor=cor_texto)

    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "sigmoide.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
