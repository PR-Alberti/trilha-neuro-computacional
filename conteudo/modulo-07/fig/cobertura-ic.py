from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    rng = np.random.default_rng(42)
    mu_true = -70.0
    sigma_true = 4.0
    n_amostra = 25
    n_experimentos = 50
    t_critico = stats.t.ppf(0.975, df=n_amostra - 1)

    amostras = rng.normal(loc=mu_true, scale=sigma_true, size=(n_experimentos, n_amostra))
    medias = amostras.mean(axis=1)
    desvios = amostras.std(axis=1, ddof=1)
    margens = t_critico * (desvios / np.sqrt(n_amostra))

    lim_inf = medias - margens
    lim_sup = medias + margens
    cobre = (lim_inf <= mu_true) & (lim_sup >= mu_true)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_cobre = "#4F46E5"
    cor_fora = "#E11D48"

    fig, ax = plt.subplots(figsize=(7.6, 6.2))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    indices = np.arange(1, n_experimentos + 1)

    for idx, low, high, media, ok in zip(indices, lim_inf, lim_sup, medias, cobre):
        cor = cor_cobre if ok else cor_fora
        lw = 1.6 if ok else 2.2
        ax.hlines(y=idx, xmin=low, xmax=high, color=cor, linewidth=lw, zorder=2)
        ax.scatter([media], [idx], color=cor, s=16, zorder=3)

    # Alças artificiais para legenda garantida mesmo se todos cobrirem
    n_cobre = int(cobre.sum())
    n_fora = int((~cobre).sum())
    ax.plot([], [], color=cor_cobre, linewidth=1.8, marker="o", markersize=4, label=f"Cobre $\\mu$ ({n_cobre} de {n_experimentos})")
    ax.plot([], [], color=cor_fora, linewidth=2.2, marker="o", markersize=4, label=f"Não cobre $\\mu$ ({n_fora} de {n_experimentos})")
    ax.axvline(mu_true, color=cor_texto, linestyle="--", linewidth=1.6, zorder=1, label="Média populacional $\\mu = -70$ mV")

    ax.set_xlabel("Potencial de repouso (mV)", fontsize=10, color=cor_texto)
    ax.set_ylabel("Índice do experimento repetido", fontsize=10, color=cor_texto)
    ax.set_title("Cobertura de 50 intervalos de confiança de 95% ($n = 25$)", fontsize=12, fontweight="bold", color=cor_texto, pad=10)
    ax.set_yticks([1, 10, 20, 30, 40, 50])
    ax.set_ylim(0, n_experimentos + 1)
    ax.grid(True, axis="x", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(loc="upper right", frameon=True, framealpha=0.85, fontsize=9)

    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "cobertura-ic.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
