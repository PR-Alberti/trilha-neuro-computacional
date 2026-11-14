from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    dados = load_breast_cancer()
    X_treino, _, y_treino, _ = train_test_split(
        dados.data,
        dados.target,
        test_size=0.3,
        stratify=dados.target,
        random_state=0,
    )

    caminho = DecisionTreeClassifier(random_state=0).cost_complexity_pruning_path(
        X_treino, y_treino
    )
    alphas = np.unique(np.maximum(caminho.ccp_alphas[:-1], 0.0))

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    acc_treino = []
    acc_cv_media = []
    acc_cv_dp = []
    n_folhas = []

    for alpha in alphas:
        clf = DecisionTreeClassifier(ccp_alpha=float(alpha), random_state=0)
        clf.fit(X_treino, y_treino)
        acc_treino.append(clf.score(X_treino, y_treino))
        n_folhas.append(clf.get_n_leaves())

        escores = cross_val_score(
            DecisionTreeClassifier(ccp_alpha=float(alpha), random_state=0),
            X_treino,
            y_treino,
            cv=cv,
        )
        acc_cv_media.append(escores.mean())
        acc_cv_dp.append(escores.std())

    acc_treino = np.array(acc_treino)
    acc_cv_media = np.array(acc_cv_media)
    acc_cv_dp = np.array(acc_cv_dp)
    n_folhas = np.array(n_folhas)

    idx_melhor = int(np.argmax(acc_cv_media))
    alpha_melhor = float(alphas[idx_melhor])

    cor_texto = "#334155"
    cor_grade = "#94A3B8"
    cor_treino = "#4F46E5"
    cor_cv = "#0D9488"
    cor_destaque = "#DC2626"

    fig, (ax_acc, ax_folhas) = plt.subplots(1, 2, figsize=(10.0, 4.1))
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: acurácia de treino e de validação cruzada vs ccp_alpha
    ax_acc.plot(
        alphas,
        acc_treino,
        marker="o",
        markersize=4,
        color=cor_treino,
        linewidth=2.0,
        label="Treino",
    )
    ax_acc.plot(
        alphas,
        acc_cv_media,
        marker="s",
        markersize=4,
        color=cor_cv,
        linewidth=2.0,
        label="Validação cruzada (5-fold)",
    )
    ax_acc.fill_between(
        alphas,
        acc_cv_media - acc_cv_dp,
        acc_cv_media + acc_cv_dp,
        color=cor_cv,
        alpha=0.14,
    )
    ax_acc.axvline(
        alpha_melhor,
        color=cor_destaque,
        linestyle="--",
        linewidth=1.3,
        label=f"Melhor α ≈ {alpha_melhor:.3f}",
    )
    ax_acc.set_title(
        "Acurácia vs. parâmetro de poda (ccp_alpha)",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_acc.set_xlabel("ccp_alpha (α)", fontsize=9.5, color=cor_texto)
    ax_acc.set_ylabel("Acurácia", fontsize=9.5, color=cor_texto)
    ax_acc.set_ylim(0.84, 1.015)
    ax_acc.legend(loc="lower left", frameon=True, framealpha=0.88, fontsize=8.5)

    # Painel direito: número de folhas vs ccp_alpha
    ax_folhas.step(
        alphas,
        n_folhas,
        where="post",
        color=cor_treino,
        linewidth=2.1,
    )
    ax_folhas.scatter(alphas, n_folhas, color=cor_treino, s=22, zorder=3)
    ax_folhas.axvline(
        alpha_melhor,
        color=cor_destaque,
        linestyle="--",
        linewidth=1.3,
    )
    ax_folhas.set_title(
        "Complexidade da árvore podada",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_folhas.set_xlabel("ccp_alpha (α)", fontsize=9.5, color=cor_texto)
    ax_folhas.set_ylabel("Número de folhas |T|", fontsize=9.5, color=cor_texto)

    for ax in (ax_acc, ax_folhas):
        ax.patch.set_alpha(0.0)
        ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=8.5)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "t08-poda.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
