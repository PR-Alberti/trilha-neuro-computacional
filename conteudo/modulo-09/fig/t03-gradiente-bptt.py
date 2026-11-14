from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    passos = np.arange(0, 21)
    taxas = [
        (1.5, r"$|w| = 1{,}5$ (explode)", "#DC2626", "-"),
        (1.0, r"$|w| = 1{,}0$ (estável)", "#475569", "--"),
        (0.8, r"$|w| = 0{,}8$ (atenua)", "#0D9488", "-"),
        (0.5, r"$|w| = 0{,}5$ (some rápido)", "#4F46E5", "-"),
    ]

    cor_texto = "#475569"
    cor_grade = "#94A3B8"

    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    for w, rotulo, cor, estilo in taxas:
        valores = w ** passos
        ax.plot(
            passos,
            valores,
            label=rotulo,
            color=cor,
            linestyle=estilo,
            linewidth=2.2,
        )
        if w != 1.0:
            ax.scatter([20], [valores[-1]], color=cor, s=30, zorder=4)

    ax.annotate(
        r"$1{,}5^{20} \approx 3\,325$",
        xy=(20, 1.5 ** 20),
        xytext=(15.4, 1.5 ** 20 * 1.4),
        fontsize=9.5,
        color="#DC2626",
        fontweight="bold",
    )
    ax.annotate(
        r"$0{,}5^{20} \approx 9{,}5 \times 10^{-7}$",
        xy=(20, 0.5 ** 20),
        xytext=(14.0, 0.5 ** 20 * 2.4),
        fontsize=9.5,
        color="#4F46E5",
        fontweight="bold",
    )

    ax.set_yscale("log")
    ax.set_ylim(2e-7, 2e4)
    ax.set_xlim(0, 20.6)
    ax.set_xticks(np.arange(0, 21, 2))
    ax.set_xlabel("Número de passos no tempo ($T$)", fontsize=10, color=cor_texto)
    ax.set_ylabel(r"Fator $|w|^T$ (escala logarítmica)", fontsize=10, color=cor_texto)
    ax.set_title(
        "Crescimento e decaimento exponencial do gradiente ao longo de $T$ passos",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(loc="lower left", frameon=False, fontsize=9.5, labelcolor=cor_texto)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "t03-gradiente-bptt.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
