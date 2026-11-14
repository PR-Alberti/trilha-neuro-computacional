from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    X, y = make_classification(
        n_samples=600,
        n_features=10,
        n_informative=4,
        n_redundant=2,
        class_sep=0.9,
        random_state=0,
    )
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.30, stratify=y, random_state=0
    )

    modelo_forte = make_pipeline(
        StandardScaler(), LogisticRegression(C=1.0, max_iter=1000, random_state=0)
    )
    modelo_forte.fit(X_treino, y_treino)
    escores_forte = modelo_forte.predict_proba(X_teste)[:, 1]
    fpr_f, tpr_f, limiares_f = roc_curve(y_teste, escores_forte)
    auc_f = roc_auc_score(y_teste, escores_forte)

    # Modelo restrito apenas aos dois primeiros atributos para ilustrar separação mais fraca
    modelo_fraco = make_pipeline(
        StandardScaler(), LogisticRegression(C=1.0, max_iter=1000, random_state=0)
    )
    modelo_fraco.fit(X_treino[:, :2], y_treino)
    escores_fraco = modelo_fraco.predict_proba(X_teste[:, :2])[:, 1]
    fpr_w, tpr_w, _ = roc_curve(y_teste, escores_fraco)
    auc_w = roc_auc_score(y_teste, escores_fraco)

    # Ponto correspondente ao limiar padrão 0.5 no modelo completo
    idx_05 = int(np.argmin(np.abs(limiares_f - 0.5)))

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_forte = "#4F46E5"
    cor_fraco = "#0D9488"
    cor_acaso = "#64748B"

    fig, ax = plt.subplots(figsize=(6.4, 5.2))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.plot(
        fpr_f,
        tpr_f,
        color=cor_forte,
        linewidth=2.4,
        label=f"Modelo completo (AUC = {auc_f:.3f})".replace(".", ","),
    )
    ax.fill_between(fpr_f, tpr_f, alpha=0.10, color=cor_forte)

    ax.plot(
        fpr_w,
        tpr_w,
        color=cor_fraco,
        linewidth=2.2,
        label=f"Modelo com 2 variáveis (AUC = {auc_w:.3f})".replace(".", ","),
    )

    ax.plot(
        [0.0, 1.0],
        [0.0, 1.0],
        linestyle="--",
        linewidth=1.6,
        color=cor_acaso,
        label="Acaso (AUC = 0,500)",
    )

    ax.scatter(
        [fpr_f[idx_05]],
        [tpr_f[idx_05]],
        color=cor_forte,
        s=55,
        zorder=4,
    )
    ax.annotate(
        "Limiar $\\tau$ = 0,5",
        xy=(fpr_f[idx_05], tpr_f[idx_05]),
        xytext=(fpr_f[idx_05] + 0.12, tpr_f[idx_05] - 0.12),
        fontsize=9.5,
        color=cor_texto,
        arrowprops={"arrowstyle": "->", "color": cor_texto, "lw": 1.1},
    )

    ax.scatter([0.0], [1.0], color="#D97706", s=50, zorder=4)
    ax.annotate(
        "Classificador ideal (0; 1)",
        xy=(0.0, 1.0),
        xytext=(0.14, 0.96),
        fontsize=9,
        color="#B45309",
        va="center",
    )

    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.04)
    ax.set_xlabel("Taxa de falsos positivos (FPR = 1 − Especificidade)", fontsize=10, color=cor_texto)
    ax.set_ylabel("Taxa de verdadeiros positivos (TPR = Recall)", fontsize=10, color=cor_texto)
    ax.set_title(
        "Curva ROC: efeito do limiar e comparação entre modelos",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(loc="lower right", frameon=True, framealpha=0.85, fontsize=9)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "t04-roc.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
