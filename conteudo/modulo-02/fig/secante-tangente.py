from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    x = np.linspace(0.0, 4.0, 300)
    y = x ** 2

    a = 2.0
    fa = a ** 2  # 4.0

    # Retas secantes para h = 1.5 e h = 0.5, e reta tangente (h -> 0)
    h1 = 1.5
    q1_x = a + h1  # 3.5
    q1_y = q1_x ** 2  # 12.25
    m1 = (q1_y - fa) / h1  # 5.5
    sec1_x = np.linspace(1.0, 3.8, 100)
    sec1_y = fa + m1 * (sec1_x - a)

    h2 = 0.5
    q2_x = a + h2  # 2.5
    q2_y = q2_x ** 2  # 6.25
    m2 = (q2_y - fa) / h2  # 4.5
    sec2_x = np.linspace(1.0, 3.8, 100)
    sec2_y = fa + m2 * (sec2_x - a)

    m_tan = 2 * a  # 4.0
    tan_x = np.linspace(0.8, 3.8, 100)
    tan_y = fa + m_tan * (tan_x - a)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_curva = "#4F46E5"
    cor_sec1 = "#F59E0B"
    cor_sec2 = "#0D9488"
    cor_tan = "#E11D48"

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.plot(x, y, color=cor_curva, linewidth=2.5, label="$f(x) = x^2$")
    ax.plot(
        sec1_x,
        sec1_y,
        color=cor_sec1,
        linewidth=1.7,
        linestyle="--",
        label="Secante (h = 1,5; inclinação = 5,5)",
    )
    ax.plot(
        sec2_x,
        sec2_y,
        color=cor_sec2,
        linewidth=1.8,
        linestyle="-.",
        label="Secante (h = 0,5; inclinação = 4,5)",
    )
    ax.plot(
        tan_x,
        tan_y,
        color=cor_tan,
        linewidth=2.2,
        label="Tangente em $x = 2$ ($f'(2) = 4$)",
    )

    # Pontos P, Q1 e Q2
    ax.scatter([a], [fa], color=cor_tan, s=48, zorder=5)
    ax.scatter([q1_x], [q1_y], color=cor_sec1, s=40, zorder=5)
    ax.scatter([q2_x], [q2_y], color=cor_sec2, s=40, zorder=5)

    ax.annotate(
        "$P(2,\\ 4)$",
        xy=(a, fa),
        xytext=(a - 0.55, fa + 1.3),
        fontsize=9.5,
        color=cor_tan,
        fontweight="bold",
    )
    ax.annotate(
        "$Q_1(3{,}5;\\ 12{,}25)$",
        xy=(q1_x, q1_y),
        xytext=(2.25, 13.0),
        fontsize=9,
        color=cor_sec1,
    )
    ax.annotate(
        "$Q_2(2{,}5;\\ 6{,}25)$",
        xy=(q2_x, q2_y),
        xytext=(2.65, 5.4),
        fontsize=9,
        color=cor_sec2,
    )

    ax.set_xlim(0.0, 4.1)
    ax.set_ylim(-0.5, 16.5)
    ax.xaxis.set_major_formatter(
        ticker.FuncFormatter(lambda v, _: f"{v:.1f}".replace(".", ","))
    )
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(
            lambda v, _: f"{int(v)}" if float(v).is_integer() else f"{v:g}".replace(".", ",")
        )
    )
    ax.set_title(
        "Das retas secantes à reta tangente em $f(x) = x^2$",
        fontsize=12,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax.set_xlabel("$x$", fontsize=10.5, color=cor_texto)
    ax.set_ylabel("$f(x)$", fontsize=10.5, color=cor_texto)

    ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(loc="upper left", frameon=False, fontsize=9, labelcolor=cor_texto)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "secante-tangente.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
