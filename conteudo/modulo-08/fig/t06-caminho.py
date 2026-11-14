from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Lasso, Ridge
from sklearn.preprocessing import StandardScaler


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    rng = np.random.default_rng(0)
    n_amostras, n_vars = 120, 10

    # Variáveis preditoras correlacionadas (como features de estímulo ou canais de EEG)
    fator_comum = rng.normal(0.0, 1.0, size=(n_amostras, 1))
    X_bruto = 0.55 * fator_comum + rng.normal(0.0, 1.0, size=(n_amostras, n_vars))
    X = StandardScaler().fit_transform(X_bruto)

    # Apenas as 3 primeiras variáveis carregam sinal verdadeiro
    pesos_reais = np.array([2.4, -1.8, 1.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    y = X @ pesos_reais + rng.normal(0.0, 0.8, size=n_amostras)
    y = y - y.mean()

    alphas_ridge = np.logspace(-2, 4, 60)
    coefs_ridge = np.array([Ridge(alpha=a).fit(X, y).coef_ for a in alphas_ridge])

    alphas_lasso = np.logspace(-3, 0.5, 60)
    coefs_lasso = np.array(
        [Lasso(alpha=a, max_iter=10000).fit(X, y).coef_ for a in alphas_lasso]
    )

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cores_ativas = ["#4F46E5", "#0D9488", "#D97706"]
    nomes_ativas = [
        "Variável ativa 1 ($\\beta_1 = 2{,}4$)",
        "Variável ativa 2 ($\\beta_2 = -1{,}8$)",
        "Variável ativa 3 ($\\beta_3 = 1{,}2$)",
    ]

    fig, (ax_r, ax_l) = plt.subplots(1, 2, figsize=(10.2, 4.3), sharey=True)
    fig.patch.set_alpha(0.0)

    paineis = [
        (ax_r, alphas_ridge, coefs_ridge, "Ridge (penalidade L2)", "Parâmetro $\\alpha$ (escala log, sem $1/2n$)"),
        (ax_l, alphas_lasso, coefs_lasso, "Lasso (penalidade L1)", "Parâmetro $\\alpha$ (escala log, com $1/2n$)"),
    ]

    for ax, alphas, coefs, titulo, xlabel in paineis:
        ax.patch.set_alpha(0.0)
        ax.axhline(0.0, color=cor_grade, linewidth=0.9, zorder=1)

        # Variáveis de ruído em cinza tracejado
        for j in range(3, n_vars):
            rotulo = "Variáveis de ruído (7)" if j == 3 else None
            ax.plot(
                alphas,
                coefs[:, j],
                color=cor_grade,
                linestyle="--",
                linewidth=1.1,
                alpha=0.75,
                label=rotulo,
                zorder=2,
            )

        # Variáveis ativas em destaque
        for j in range(3):
            ax.plot(
                alphas,
                coefs[:, j],
                color=cores_ativas[j],
                linewidth=2.2,
                label=nomes_ativas[j],
                zorder=3,
            )

        ax.set_xscale("log")
        ax.set_title(titulo, fontsize=11.5, fontweight="bold", color=cor_texto, pad=10)
        ax.set_xlabel(xlabel, fontsize=9.8, color=cor_texto)
        ax.grid(True, which="major", linestyle=":", linewidth=0.7, alpha=0.45, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    ax_r.set_ylabel("Coeficientes estimados $\\hat{\\beta}_j$", fontsize=10, color=cor_texto)
    handles, labels = ax_r.get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        loc="lower center",
        ncol=2,
        frameon=False,
        fontsize=9,
        labelcolor=cor_texto,
        bbox_to_anchor=(0.5, -0.06),
    )
    fig.suptitle(
        "Caminho de regularização: encolhimento suave (Ridge) vs. seleção esparsa (Lasso)",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        y=1.01,
    )
    fig.tight_layout(rect=(0.0, 0.08, 1.0, 0.98))

    destino = Path(__file__).resolve().parent / "t06-caminho.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
