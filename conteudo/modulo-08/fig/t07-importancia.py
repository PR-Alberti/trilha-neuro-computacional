from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    rng = np.random.default_rng(0)
    n_amostras = 300
    nomes_bandas = [
        "Delta (0,5–4 Hz)",
        "Teta (4–8 Hz)",
        "Alfa (8–12 Hz)",
        "Beta (13–30 Hz)",
        "Gama (30–80 Hz)",
    ]

    # y = 0 (sono profundo NREM), y = 1 (vigília relaxada)
    y = rng.integers(0, 2, size=n_amostras)
    delta = np.where(y == 0, rng.normal(2.2, 0.8, n_amostras), rng.normal(0.5, 0.7, n_amostras))
    alfa = np.where(y == 1, rng.normal(1.8, 0.7, n_amostras), rng.normal(0.6, 0.6, n_amostras))
    teta = rng.normal(1.0, 0.6, n_amostras)
    beta = rng.normal(0.8, 0.5, n_amostras)
    gama = rng.normal(0.4, 0.4, n_amostras)

    X = np.column_stack([delta, teta, alfa, beta, gama])
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.33, stratify=y, random_state=0
    )

    tubo = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(C=1.0, max_iter=1000)),
    ]).fit(X_treino, y_treino)

    resultado = permutation_importance(
        tubo, X_teste, y_teste, n_repeats=30, random_state=0
    )

    ordem = np.argsort(resultado.importances_mean)
    medias = resultado.importances_mean[ordem]
    desvios = resultado.importances_std[ordem]
    rotulos = [nomes_bandas[i] for i in ordem]

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_ativa = "#4F46E5"
    cor_ruido = "#94A3B8"
    cores = [cor_ativa if ("Delta" in r or "Alfa" in r) else cor_ruido for r in rotulos]

    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    posicoes = np.arange(len(rotulos))
    ax.barh(
        posicoes,
        medias,
        xerr=desvios,
        color=cores,
        alpha=0.88,
        height=0.58,
        error_kw={"ecolor": cor_texto, "elinewidth": 1.4, "capsize": 4},
        zorder=3,
    )
    ax.axvline(0.0, color=cor_texto, linewidth=1.0, linestyle="--", zorder=2)

    ax.set_yticks(posicoes)
    ax.set_yticklabels(rotulos, fontsize=10, color=cor_texto)
    ax.set_xlabel(
        "Queda média na acurácia de teste após permutação (± desvio padrão)",
        fontsize=10,
        color=cor_texto,
    )
    ax.set_title(
        "Importância por permutação no decodificador de vigília vs. sono NREM",
        fontsize=11.8,
        fontweight="bold",
        color=cor_texto,
        pad=12,
    )

    ax.grid(True, axis="x", linestyle=":", linewidth=0.7, alpha=0.45, color=cor_grade, zorder=1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9.5)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "t07-importancia.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
