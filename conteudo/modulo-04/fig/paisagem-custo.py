from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    # Dados do neurônio visual: contraste (x) e taxa de disparo em Hz (y)
    x_dados = np.array([0.2, 0.4, 0.6, 0.8])
    y_dados = np.array([21.0, 27.0, 43.0, 49.0])

    # Reta ótima: y = 50x + 10
    a_otimo, b_otimo = 50.0, 10.0
    x_reta = np.linspace(0.0, 1.0, 100)
    y_reta = a_otimo * x_reta + b_otimo
    y_previsto = a_otimo * x_dados + b_otimo

    # Grade para as curvas de nível de J(a, b)
    a_vals = np.linspace(25.0, 75.0, 200)
    b_vals = np.linspace(-5.0, 25.0, 200)
    A, B = np.meshgrid(a_vals, b_vals)

    J = np.zeros_like(A)
    for xi, yi in zip(x_dados, y_dados):
        J += (A * xi + B - yi) ** 2
    J /= len(x_dados)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_dados = "#4F46E5"
    cor_contorno = "#0D9488"
    cor_min = "#E11D48"

    fig, (ax_dados, ax_cont) = plt.subplots(1, 2, figsize=(10.2, 4.4))
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: espaço dos dados e reta ótima
    for xi, yi, ypi in zip(x_dados, y_dados, y_previsto):
        ax_dados.plot([xi, xi], [yi, ypi], color=cor_grade, linestyle=":", linewidth=1.3, zorder=2)
    ax_dados.plot(x_reta, y_reta, color=cor_dados, linewidth=2.2, label="$\\hat{y} = 50x + 10$", zorder=3)
    ax_dados.scatter(x_dados, y_dados, color=cor_min, s=42, zorder=4, label="Dados medidos")
    ax_dados.set_title("Espaço dos dados: reta ótima", fontsize=11, fontweight="bold", color=cor_texto, pad=10)
    ax_dados.set_xlabel("Contraste $x$", fontsize=9.5, color=cor_texto)
    ax_dados.set_ylabel("Taxa de disparo $y$ (Hz)", fontsize=9.5, color=cor_texto)
    ax_dados.set_xlim(0.0, 1.0)
    ax_dados.set_ylim(5.0, 65.0)
    leg = ax_dados.legend(frameon=False, fontsize=8.5, loc="upper left")
    for txt in leg.get_texts():
        txt.set_color(cor_texto)

    # Painel direito: espaço dos parâmetros e curvas de nível de J(a, b)
    niveis = [8, 15, 25, 40, 60, 90, 130, 180, 240, 310, 390, 480]
    cs = ax_cont.contour(A, B, J, levels=niveis, colors=cor_contorno, linewidths=1.25)
    ax_cont.clabel(cs, inline=True, fontsize=8, fmt="%d")
    ax_cont.scatter([a_otimo], [b_otimo], marker="*", s=180, color=cor_min, zorder=5)
    ax_cont.annotate(
        "mínimo",
        xy=(a_otimo, b_otimo),
        xytext=(56.5, 16.5),
        color=cor_min,
        fontsize=9.5,
        fontweight="bold",
        arrowprops={"arrowstyle": "->", "color": cor_min, "lw": 1.2},
        zorder=6,
    )
    ax_cont.set_title("Espaço dos parâmetros: curvas de nível de $J(a, b)$", fontsize=11, fontweight="bold", color=cor_texto, pad=10)
    ax_cont.set_xlabel("Inclinação $a$ (Hz por unidade de contraste)", fontsize=9.5, color=cor_texto)
    ax_cont.set_ylabel("Intercepto $b$ (Hz)", fontsize=9.5, color=cor_texto)
    ax_cont.set_xlim(25.0, 75.0)
    ax_cont.set_ylim(-5.0, 25.0)

    # Estilo compartilhado
    for ax in (ax_dados, ax_cont):
        ax.patch.set_alpha(0.0)
        ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "paisagem-custo.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
