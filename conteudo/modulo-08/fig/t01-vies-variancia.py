from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


def curva_sintonia(x: np.ndarray) -> np.ndarray:
    """Curva de resposta ao contraste estilo Naka-Rushton (em Hz)."""
    return 10.0 + 70.0 * (x ** 2) / (x ** 2 + 0.35 ** 2)


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    rng = np.random.default_rng(0)
    n_treino = 20
    n_rep = 300
    sigma = 6.0

    x_treino = np.linspace(0.0, 1.0, n_treino)
    f_treino = curva_sintonia(x_treino)
    X_treino = x_treino.reshape(-1, 1)

    # Múltiplas realizações de ruído: Y_treino tem formato (n_treino, n_rep)
    ruido_treino = rng.normal(0.0, sigma, size=(n_treino, n_rep))
    Y_treino = f_treino[:, None] + ruido_treino

    x_grade = np.linspace(0.02, 0.98, 50)
    f_grade = curva_sintonia(x_grade)
    X_grade = x_grade.reshape(-1, 1)

    graus = np.arange(1, 13)
    mse_treino_medio = []
    mse_teste_medio = []
    vies2_medio = []
    var_media = []

    for grau in graus:
        modelo = Pipeline([
            ("poly", PolynomialFeatures(degree=int(grau), include_bias=False)),
            ("scaler", StandardScaler()),
            ("reg", LinearRegression()),
        ])
        modelo.fit(X_treino, Y_treino)

        Y_pred_treino = modelo.predict(X_treino)
        Y_pred_teste = modelo.predict(X_grade)

        mse_tr = float(np.mean((Y_treino - Y_pred_treino) ** 2))
        vies2 = float(np.mean((np.mean(Y_pred_teste, axis=1) - f_grade) ** 2))
        variancia = float(np.mean(np.var(Y_pred_teste, axis=1)))
        mse_te = vies2 + variancia + sigma ** 2

        mse_treino_medio.append(mse_tr)
        vies2_medio.append(vies2)
        var_media.append(variancia)
        mse_teste_medio.append(mse_te)

    grau_otimo = int(graus[int(np.argmin(mse_teste_medio))])

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_treino = "#0D9488"
    cor_teste = "#4F46E5"
    cor_vies = "#D97706"
    cor_var = "#E11D48"

    fig, (ax_err, ax_bv) = plt.subplots(1, 2, figsize=(10.2, 4.3))
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: Erro médio de treino vs. teste
    ax_err.plot(graus, mse_treino_medio, marker="o", markersize=4.5, linewidth=2.2,
                color=cor_treino, label="MSE de treino")
    ax_err.plot(graus, mse_teste_medio, marker="s", markersize=4.5, linewidth=2.2,
                color=cor_teste, label="MSE de teste esperado")
    ax_err.axhline(sigma ** 2, color=cor_grade, linestyle=":", linewidth=1.4,
                    label=f"Ruído irredutível ($\\sigma^2 = {int(sigma ** 2)}$)")
    ax_err.axvline(grau_otimo, color=cor_teste, linestyle="--", linewidth=1.1, alpha=0.55)
    ax_err.set_title("Erro de treino $\\times$ erro de teste", fontsize=11.5,
                     fontweight="bold", color=cor_texto, pad=10)
    ax_err.set_xlabel("Grau do polinômio (flexibilidade)", fontsize=10, color=cor_texto)
    ax_err.set_ylabel("Erro quadrático médio ($\\mathrm{Hz}^2$)", fontsize=10, color=cor_texto)
    ax_err.set_xticks(graus)
    ax_err.legend(frameon=False, fontsize=8.8, loc="best")

    # Painel direito: Decomposição Viés² vs. Variância
    ax_bv.plot(graus, vies2_medio, marker="^", markersize=4.5, linewidth=2.2,
               color=cor_vies, label="$\\mathrm{Viés}^2$")
    ax_bv.plot(graus, var_media, marker="v", markersize=4.5, linewidth=2.2,
               color=cor_var, label="Variância")
    ax_bv.plot(graus, mse_teste_medio, linestyle="--", linewidth=1.8,
               color=cor_teste, label="MSE de teste ($\\mathrm{Viés}^2 + \\mathrm{Var} + \\sigma^2$)")
    ax_bv.axvline(grau_otimo, color=cor_teste, linestyle="--", linewidth=1.1, alpha=0.55)
    ax_bv.set_title("Compromisso viés–variância", fontsize=11.5,
                    fontweight="bold", color=cor_texto, pad=10)
    ax_bv.set_xlabel("Grau do polinômio (flexibilidade)", fontsize=10, color=cor_texto)
    ax_bv.set_ylabel("Componente do erro ($\\mathrm{Hz}^2$)", fontsize=10, color=cor_texto)
    ax_bv.set_xticks(graus)
    ax_bv.legend(frameon=False, fontsize=8.8, loc="best")

    for ax in (ax_err, ax_bv):
        ax.patch.set_alpha(0.0)
        ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    fig.suptitle(
        "Simulação de Monte Carlo: flexibilidade, curva em U e decomposição do erro",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        y=1.02,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "t01-vies-variancia.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
