from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def main() -> None:
    n0 = 100
    t_geracoes = np.arange(0, 11)
    n_bacterias = n0 * (2 ** t_geracoes)

    t_continuo = np.linspace(0, 10, 250)
    n_continuo = n0 * (2 ** t_continuo)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_linear = "#4F46E5"
    cor_log = "#0D9488"

    fig, (ax_lin, ax_log) = plt.subplots(1, 2, figsize=(9.6, 4.2))
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: escala linear
    ax_lin.plot(t_continuo, n_continuo, color=cor_linear, linewidth=2.2)
    ax_lin.scatter(t_geracoes, n_bacterias, color=cor_linear, s=28, zorder=3)
    ax_lin.set_title("Escala linear", fontsize=11.5, fontweight="bold", color=cor_texto, pad=10)
    ax_lin.set_xlabel("Tempo (gerações)", fontsize=10, color=cor_texto)
    ax_lin.set_ylabel("Número de bactérias $N(t)$", fontsize=10, color=cor_texto)
    ax_lin.set_xticks(np.arange(0, 11, 2))
    ax_lin.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda y, _: f"{int(y):,}".replace(",", "."))
    )

    # Painel direito: escala logarítmica
    ax_log.plot(t_continuo, n_continuo, color=cor_log, linewidth=2.2)
    ax_log.scatter(t_geracoes, n_bacterias, color=cor_log, s=28, zorder=3)
    ax_log.set_yscale("log")
    ax_log.set_title("Escala logarítmica", fontsize=11.5, fontweight="bold", color=cor_texto, pad=10)
    ax_log.set_xlabel("Tempo (gerações)", fontsize=10, color=cor_texto)
    ax_log.set_ylabel("Número de bactérias $N(t)$", fontsize=10, color=cor_texto)
    ax_log.set_xticks(np.arange(0, 11, 2))
    ax_log.set_yticks([100, 1000, 10000, 100000])
    ax_log.set_yticklabels(["$10^2$", "$10^3$", "$10^4$", "$10^5$"])
    ax_log.yaxis.set_minor_formatter(ticker.NullFormatter())

    # Estilo compartilhado
    for ax in (ax_lin, ax_log):
        ax.patch.set_alpha(0.0)
        ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    fig.suptitle(
        "Crescimento bacteriano: $N(t) = 100 \\cdot 2^t$",
        fontsize=13,
        fontweight="bold",
        color=cor_texto,
        y=1.02,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "crescimento-bacteriano.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
