from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    rng = np.random.default_rng(0)
    n_amostras = 4000

    # Mistura bimodal: 0.5 N(-2, 0.3^2) + 0.5 N(2, 0.3^2)
    modos = rng.choice([-2.0, 2.0], size=n_amostras)
    x0 = modos + 0.3 * rng.standard_normal(n_amostras)

    T = 50
    betas = np.linspace(1e-3, 0.2, T)
    alphas = 1.0 - betas
    alpha_bar = np.cumprod(alphas)

    tempos = [0, 10, 25, 50]
    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_hist = "#4F46E5"
    cor_ref = "#0D9488"

    fig, axes = plt.subplots(2, 2, figsize=(9.2, 5.6), sharex=True, sharey=True)
    fig.patch.set_alpha(0.0)
    grade_x = np.linspace(-4.0, 4.0, 300)
    normal_padrao = np.exp(-0.5 * grade_x**2) / np.sqrt(2.0 * np.pi)

    for ax, t in zip(axes.flat, tempos):
        if t == 0:
            xt = x0
            subtitulo = "$t = 0$ (dados)"
        else:
            ab = alpha_bar[t - 1]
            eps = rng.standard_normal(n_amostras)
            xt = np.sqrt(ab) * x0 + np.sqrt(1.0 - ab) * eps
            subtitulo = f"$t = {t}$ ($\\bar{{\\alpha}}_{{{t}}} \\approx {ab:.2f}$)"

        ax.hist(xt, bins=45, range=(-4.0, 4.0), density=True, color=cor_hist, alpha=0.78, edgecolor="none")
        if t == 50:
            ax.plot(grade_x, normal_padrao, color=cor_ref, linewidth=2.0, linestyle="--", label="N(0, 1)")
            ax.legend(frameon=False, fontsize=9, loc="upper right")

        ax.set_title(subtitulo, fontsize=11, fontweight="bold", color=cor_texto, pad=8)
        ax.patch.set_alpha(0.0)
        ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    axes[1, 0].set_xlabel("$x_t$", fontsize=10, color=cor_texto)
    axes[1, 1].set_xlabel("$x_t$", fontsize=10, color=cor_texto)
    axes[0, 0].set_ylabel("Densidade", fontsize=10, color=cor_texto)
    axes[1, 0].set_ylabel("Densidade", fontsize=10, color=cor_texto)

    fig.suptitle(
        "Processo direto de difusão em mistura bimodal ($T = 50$)",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        y=0.99,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "t07-difusao.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
