from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    z_neg = np.linspace(-5.0, -0.02, 200)
    z_pos = np.linspace(0.02, 5.0, 200)
    z = np.linspace(-5.0, 5.0, 400)

    sig = 1.0 / (1.0 + np.exp(-z))
    dsig = sig * (1.0 - sig)

    th = np.tanh(z)
    dth = 1.0 - th ** 2

    relu = np.maximum(0.0, z)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_func = "#4F46E5"
    cor_deriv = "#0D9488"

    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.8))
    fig.patch.set_alpha(0.0)

    # 1. Degrau (Heaviside)
    ax = axes[0, 0]
    ax.plot(z_neg, np.zeros_like(z_neg), color=cor_func, linewidth=2.2, label=r"Função $\phi(z)$")
    ax.plot(z_pos, np.ones_like(z_pos), color=cor_func, linewidth=2.2)
    ax.scatter([0.0], [1.0], color=cor_func, s=28, zorder=4)
    ax.scatter([0.0], [0.0], facecolors="white", edgecolors=cor_func, s=28, linewidth=1.5, zorder=4)
    ax.plot(z_neg, np.zeros_like(z_neg), color=cor_deriv, linewidth=1.8, linestyle="--", label=r"Derivada $\phi'(z)$")
    ax.plot(z_pos, np.zeros_like(z_pos), color=cor_deriv, linewidth=1.8, linestyle="--")
    ax.set_title("Degrau (Heaviside)", fontsize=11, fontweight="bold", color=cor_texto, pad=8)
    ax.set_ylim(-0.2, 1.3)

    # 2. Sigmoide logística
    ax = axes[0, 1]
    ax.plot(z, sig, color=cor_func, linewidth=2.2, label=r"$\sigma(z)$")
    ax.plot(z, dsig, color=cor_deriv, linewidth=1.8, linestyle="--", label=r"$\sigma'(z) = \sigma(z)(1-\sigma(z))$")
    ax.scatter([0.0], [0.25], color=cor_deriv, s=28, zorder=4)
    ax.annotate("máx = 0,25", xy=(0.0, 0.25), xytext=(1.1, 0.34), fontsize=8.5, color=cor_deriv,
                arrowprops=dict(arrowstyle="->", color=cor_deriv, lw=0.9))
    ax.set_title("Sigmoide logística", fontsize=11, fontweight="bold", color=cor_texto, pad=8)
    ax.set_ylim(-0.2, 1.3)

    # 3. Tangente hiperbólica
    ax = axes[1, 0]
    ax.plot(z, th, color=cor_func, linewidth=2.2, label=r"$\tanh(z)$")
    ax.plot(z, dth, color=cor_deriv, linewidth=1.8, linestyle="--", label=r"$\tanh'(z) = 1 - \tanh^2(z)$")
    ax.set_title("Tangente hiperbólica (tanh)", fontsize=11, fontweight="bold", color=cor_texto, pad=8)
    ax.set_ylim(-1.25, 1.25)

    # 4. ReLU
    ax = axes[1, 1]
    ax.plot(z, relu, color=cor_func, linewidth=2.2, label=r"$\mathrm{ReLU}(z) = \max(0, z)$")
    ax.plot(z_neg, np.zeros_like(z_neg), color=cor_deriv, linewidth=1.8, linestyle="--", label=r"$\mathrm{ReLU}'(z)$ ($z \neq 0$)")
    ax.plot(z_pos, np.ones_like(z_pos), color=cor_deriv, linewidth=1.8, linestyle="--")
    ax.scatter([0.0, 0.0], [0.0, 1.0], facecolors="white", edgecolors=cor_deriv, s=26, linewidth=1.4, zorder=4)
    ax.set_title("ReLU", fontsize=11, fontweight="bold", color=cor_texto, pad=8)
    ax.set_ylim(-0.5, 5.2)

    for idx, ax in enumerate(axes.flat):
        ax.patch.set_alpha(0.0)
        ax.axhline(0.0, color=cor_grade, linewidth=0.8, alpha=0.6)
        ax.axvline(0.0, color=cor_grade, linewidth=0.8, alpha=0.6)
        ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)
        ax.set_xlim(-5.0, 5.0)
        if idx >= 2:
            ax.set_xlabel("Pré-ativação $z$", fontsize=9.5, color=cor_texto)
        if idx % 2 == 0:
            ax.set_ylabel("Valor", fontsize=9.5, color=cor_texto)
        ax.legend(loc="upper left", frameon=False, fontsize=8.5, labelcolor=cor_texto)

    fig.suptitle(
        "Funções de ativação clássicas e suas derivadas",
        fontsize=13,
        fontweight="bold",
        color=cor_texto,
        y=1.01,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "t01-ativacoes.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
