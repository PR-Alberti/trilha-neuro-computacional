from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    a, b = 0.0, 2.0
    n = 4
    dx = (b - a) / n  # 0.5
    x_edges = np.linspace(a, b, n + 1)

    x_curva = np.linspace(a, b, 300)
    y_curva = x_curva ** 2

    h_esq = x_edges[:-1] ** 2  # [0.0, 0.25, 1.0, 2.25]
    h_dir = x_edges[1:] ** 2   # [0.25, 1.0, 2.25, 4.0]

    soma_esq = float(np.sum(h_esq) * dx)  # 1.75
    soma_dir = float(np.sum(h_dir) * dx)  # 3.75

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_curva = "#4F46E5"
    cor_esq = "#0D9488"
    cor_dir = "#E11D48"

    fig, (ax_esq, ax_dir) = plt.subplots(1, 2, figsize=(9.6, 4.3), sharey=True)
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: soma à esquerda
    ax_esq.bar(
        x_edges[:-1],
        h_esq,
        width=dx,
        align="edge",
        color=cor_esq,
        alpha=0.28,
        edgecolor=cor_esq,
        linewidth=1.6,
        zorder=2,
    )
    ax_esq.plot(x_curva, y_curva, color=cor_curva, linewidth=2.4, zorder=3, label="$f(x) = x^2$")
    ax_esq.scatter(x_edges[:-1], h_esq, color=cor_esq, s=36, zorder=4)
    ax_esq.set_title(
        f"Soma à esquerda ($E_4$ = {soma_esq:.2f})".replace(".", ","),
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_esq.set_xlabel("$x$", fontsize=10.5, color=cor_texto)
    ax_esq.set_ylabel("$f(x)$", fontsize=10.5, color=cor_texto)

    # Painel direito: soma à direita
    ax_dir.bar(
        x_edges[:-1],
        h_dir,
        width=dx,
        align="edge",
        color=cor_dir,
        alpha=0.24,
        edgecolor=cor_dir,
        linewidth=1.6,
        zorder=2,
    )
    ax_dir.plot(x_curva, y_curva, color=cor_curva, linewidth=2.4, zorder=3, label="$f(x) = x^2$")
    ax_dir.scatter(x_edges[1:], h_dir, color=cor_dir, s=36, zorder=4)
    ax_dir.set_title(
        f"Soma à direita ($D_4$ = {soma_dir:.2f})".replace(".", ","),
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_dir.set_xlabel("$x$", fontsize=10.5, color=cor_texto)

    fmt_virgula = ticker.FuncFormatter(lambda val, _: f"{val:g}".replace(".", ","))

    for ax in (ax_esq, ax_dir):
        ax.patch.set_alpha(0.0)
        ax.set_xlim(-0.05, 2.1)
        ax.set_ylim(0.0, 4.35)
        ax.set_xticks(x_edges)
        ax.xaxis.set_major_formatter(fmt_virgula)
        ax.yaxis.set_major_formatter(fmt_virgula)
        ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)
        ax.legend(loc="upper left", frameon=False, fontsize=9.5, labelcolor=cor_texto)

    fig.suptitle(
        "Somas de Riemann de $f(x) = x^2$ em [0, 2] com $n = 4$ (valor exato = 8/3 ≈ 2,67)",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        y=1.02,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "somas-riemann.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
