from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_moons
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    X, y = make_moons(n_samples=220, noise=0.25, random_state=0)

    modelos = [
        (
            "Regressão logística",
            make_pipeline(
                StandardScaler(),
                LogisticRegression(C=1.0, max_iter=1000, random_state=0),
            ),
        ),
        (
            "Análise discriminante linear (LDA)",
            make_pipeline(
                StandardScaler(),
                LinearDiscriminantAnalysis(),
            ),
        ),
        (
            "KNN (K = 1)",
            make_pipeline(
                StandardScaler(),
                KNeighborsClassifier(n_neighbors=1),
            ),
        ),
        (
            "KNN (K = 15)",
            make_pipeline(
                StandardScaler(),
                KNeighborsClassifier(n_neighbors=15),
            ),
        ),
    ]

    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    grade_x, grade_y = np.meshgrid(
        np.linspace(x_min, x_max, 250),
        np.linspace(y_min, y_max, 250),
    )
    pontos_grade = np.c_[grade_x.ravel(), grade_y.ravel()]

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_classe_0 = "#4F46E5"
    cor_classe_1 = "#0D9488"
    mapa_fundo = ListedColormap([cor_classe_0, cor_classe_1])

    plt.rcParams["svg.fonttype"] = "none"
    fig, eixos = plt.subplots(2, 2, figsize=(9.2, 7.6), sharex=True, sharey=True)
    fig.patch.set_alpha(0.0)

    for ax, (titulo, modelo) in zip(eixos.ravel(), modelos):
        modelo.fit(X, y)
        probs = modelo.predict_proba(pontos_grade)[:, 1].reshape(grade_x.shape)
        classes_grade = (probs >= 0.5).astype(int)

        ax.contourf(
            grade_x,
            grade_y,
            classes_grade,
            levels=[-0.5, 0.5, 1.5],
            cmap=mapa_fundo,
            alpha=0.18,
        )
        ax.contour(
            grade_x,
            grade_y,
            probs,
            levels=[0.5],
            colors=["#1E293B"],
            linewidths=1.8,
        )

        ax.scatter(
            X[y == 0, 0],
            X[y == 0, 1],
            color=cor_classe_0,
            edgecolor="white",
            linewidth=0.6,
            s=30,
            alpha=0.9,
            label="Classe 0",
        )
        ax.scatter(
            X[y == 1, 0],
            X[y == 1, 1],
            color=cor_classe_1,
            edgecolor="white",
            linewidth=0.6,
            s=30,
            alpha=0.9,
            label="Classe 1",
        )

        ax.set_title(titulo, fontsize=11.5, fontweight="bold", color=cor_texto, pad=8)
        ax.patch.set_alpha(0.0)
        ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.3, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    eixos[1, 0].set_xlabel("Variável $x_1$", fontsize=10, color=cor_texto)
    eixos[1, 1].set_xlabel("Variável $x_1$", fontsize=10, color=cor_texto)
    eixos[0, 0].set_ylabel("Variável $x_2$", fontsize=10, color=cor_texto)
    eixos[1, 0].set_ylabel("Variável $x_2$", fontsize=10, color=cor_texto)

    handles, labels = eixos[0, 0].get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.96),
        ncol=2,
        frameon=False,
        fontsize=10,
        labelcolor=cor_texto,
    )
    fig.suptitle(
        "Fronteiras de decisão: modelos lineares versus KNN",
        fontsize=13,
        fontweight="bold",
        color=cor_texto,
        y=1.01,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.93])

    destino = Path(__file__).resolve().parent / "t03-fronteiras.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
