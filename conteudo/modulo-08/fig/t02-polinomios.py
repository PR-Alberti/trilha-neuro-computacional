from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

plt.rcParams['svg.fonttype'] = 'none'


def curva_sintonia(theta: np.ndarray) -> np.ndarray:
    """Curva de sintonia de orientação (taxa em Hz)."""
    return 5.0 + 35.0 * np.exp(-0.5 * ((theta - 15.0) / 45.0) ** 2)


def main() -> None:
    rng = np.random.default_rng(0)

    # 18 orientações amostradas entre -90° e +90° (janela de 1 s -> contagem = taxa em Hz)
    theta_obs = np.linspace(-90.0, 90.0, 18)
    taxa_real_obs = curva_sintonia(theta_obs)
    taxa_obs = rng.poisson(taxa_real_obs).astype(float)

    theta_grade = np.linspace(-90.0, 90.0, 400)
    taxa_real_grade = curva_sintonia(theta_grade)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"

    configs = [
        (1, "Grau 1 (subajuste)", "#D97706", "-."),
        (3, "Grau 3 (equilibrado)", "#4F46E5", "-"),
        (15, "Grau 15 (sobreajuste)", "#E11D48", ":"),
    ]

    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.plot(
        theta_grade,
        taxa_real_grade,
        color="#64748B",
        linestyle="--",
        linewidth=1.5,
        label="Curva verdadeira",
    )
    ax.scatter(
        theta_obs,
        taxa_obs,
        color="#0F172A",
        s=32,
        zorder=5,
        label="Dados observados (Poisson)",
    )

    for grau, rotulo, cor, estilo in configs:
        modelo = Pipeline(
            [
                ("poly", PolynomialFeatures(degree=grau, include_bias=False)),
                ("scaler", StandardScaler()),
                ("reg", LinearRegression()),
            ]
        )
        modelo.fit(theta_obs.reshape(-1, 1), taxa_obs)
        y_pred = modelo.predict(theta_grade.reshape(-1, 1))
        ax.plot(theta_grade, y_pred, color=cor, linestyle=estilo, linewidth=2.2, label=rotulo)

    ax.set_title(
        "Regressão polinomial em uma curva de sintonia de orientação",
        fontsize=12,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax.set_xlabel("Orientação do estímulo (graus)", fontsize=10, color=cor_texto)
    ax.set_ylabel("Taxa de disparo (Hz)", fontsize=10, color=cor_texto)
    ax.set_xlim(-95, 95)
    ax.set_ylim(-5, 55)
    ax.set_xticks(np.arange(-90, 91, 30))

    ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(frameon=False, fontsize=8.8, loc="upper left")

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "t02-polinomios.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
