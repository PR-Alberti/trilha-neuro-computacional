from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    a = 2.0
    L = 7.0
    eps = 0.6
    delta = 0.2  # eps / 3

    x_all = np.linspace(1.3, 2.7, 200)
    y_all = 3.0 * x_all + 1.0

    x_in = np.linspace(a - delta, a + delta, 100)
    y_in = 3.0 * x_in + 1.0

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_reta = "#64748B"
    cor_destaque = "#4F46E5"
    cor_eps = "#0D9488"
    cor_delta = "#6366F1"

    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    # Faixas sombreadas
    ax.axhspan(L - eps, L + eps, color=cor_eps, alpha=0.14, label=r"Faixa $L \pm \varepsilon$ ($7{,}0 \pm 0{,}6$)")
    ax.axvspan(a - delta, a + delta, color=cor_delta, alpha=0.14, label=r"Faixa $a \pm \delta$ ($2{,}0 \pm 0{,}2$)")

    # Retângulo de interseção
    retangulo = patches.Rectangle(
        (a - delta, L - eps),
        2 * delta,
        2 * eps,
        linewidth=1.3,
        edgecolor=cor_destaque,
        facecolor="none",
        linestyle="--",
        zorder=3,
    )
    ax.add_patch(retangulo)

    # Linhas guia centrais
    ax.plot([a, a], [4.8, L], linestyle=":", linewidth=1.1, color=cor_texto, alpha=0.7)
    ax.plot([1.3, a], [L, L], linestyle=":", linewidth=1.1, color=cor_texto, alpha=0.7)

    # Gráfico da função e trecho dentro da janela
    ax.plot(x_all, y_all, color=cor_reta, linewidth=1.8, alpha=0.8, label=r"$f(x) = 3x + 1$")
    ax.plot(x_in, y_in, color=cor_destaque, linewidth=3.2, zorder=4)

    # Ponto (a, L) aberto para destacar que x != a na definição
    ax.scatter([a], [L], s=55, facecolor="white", edgecolor=cor_destaque, linewidth=2.0, zorder=5)

    ax.set_xlim(1.3, 2.7)
    ax.set_ylim(4.8, 9.2)

    ax.set_xticks([1.4, a - delta, a, a + delta, 2.6])
    ax.set_xticklabels([
        "1,4",
        "$a - \\delta$\n1,8",
        "$a$\n2,0",
        "$a + \\delta$\n2,2",
        "2,6",
    ])

    ax.set_yticks([5.0, L - eps, L, L + eps, 9.0])
    ax.set_yticklabels([
        "5,0",
        r"$L - \varepsilon = 6{,}4$",
        r"$L = 7{,}0$",
        r"$L + \varepsilon = 7{,}6$",
        "9,0",
    ])

    ax.set_xlabel("$x$", fontsize=10.5, color=cor_texto)
    ax.set_ylabel("$f(x)$", fontsize=10.5, color=cor_texto)
    ax.set_title(
        r"Definição $\varepsilon$-$\delta$ para $\lim_{x \to 2} (3x + 1) = 7$",
        fontsize=12,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.3, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(loc="upper left", frameon=True, framealpha=0.85, fontsize=8.8)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "epsilon-delta.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
