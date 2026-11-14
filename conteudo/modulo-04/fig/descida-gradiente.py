from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def gradiente_j(w):
    return np.array([2.0 * w[0], 8.0 * w[1]])


def executar_gd(w0, eta, n_passos):
    w = w0.astype(float).copy()
    trajetoria = [w.copy()]
    for _ in range(n_passos):
        w = w - eta * gradiente_j(w)
        trajetoria.append(w.copy())
    return np.array(trajetoria)


def main() -> None:
    w1_vals = np.linspace(-3.0, 3.0, 240)
    w2_vals = np.linspace(-2.0, 2.0, 200)
    W1, W2 = np.meshgrid(w1_vals, w2_vals)
    J = W1**2 + 4.0 * W2**2

    w0 = np.array([-2.5, 1.5])
    traj_suave = executar_gd(w0, eta=0.10, n_passos=12)
    traj_zigue = executar_gd(w0, eta=0.23, n_passos=12)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_suave = "#0D9488"
    cor_zigue = "#4F46E5"
    cor_min = "#E11D48"

    fig, ax = plt.subplots(figsize=(7.6, 5.0))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    niveis = [0.5, 1.5, 3.0, 5.0, 8.0, 11.0, 15.0, 19.0, 23.0]
    cs = ax.contour(W1, W2, J, levels=niveis, colors=cor_grade, linewidths=1.0, alpha=0.8)
    ax.clabel(cs, inline=True, fontsize=7.5, fmt="%.1f")

    ax.plot(
        traj_zigue[:, 0],
        traj_zigue[:, 1],
        color=cor_zigue,
        marker="o",
        markersize=4.5,
        linewidth=1.6,
        linestyle="-",
        label=r"$\eta = 0{,}23$ (zigue-zague perto do limite)",
        zorder=4,
    )
    ax.plot(
        traj_suave[:, 0],
        traj_suave[:, 1],
        color=cor_suave,
        marker="o",
        markersize=4.5,
        linewidth=2.0,
        linestyle="-",
        label=r"$\eta = 0{,}10$ (descida suave)",
        zorder=5,
    )

    ax.scatter([w0[0]], [w0[1]], color="#1E293B", s=55, zorder=6)
    ax.annotate(
        r"início $(-2{,}5;\; 1{,}5)$",
        xy=(w0[0], w0[1]),
        xytext=(-1.95, 1.65),
        color="#1E293B",
        fontsize=9,
        fontweight="bold",
        arrowprops={"arrowstyle": "->", "color": "#1E293B", "lw": 1.0},
        zorder=7,
    )

    ax.scatter([0.0], [0.0], marker="*", s=170, color=cor_min, zorder=6)
    ax.annotate(
        r"mínimo $(0, 0)$",
        xy=(0.0, 0.0),
        xytext=(0.55, -0.55),
        color=cor_min,
        fontsize=9.5,
        fontweight="bold",
        arrowprops={"arrowstyle": "->", "color": cor_min, "lw": 1.1},
        zorder=7,
    )

    ax.set_aspect("equal")
    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(-2.0, 2.0)
    ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_yticks([-2, -1, 0, 1, 2])
    ax.set_xlabel("$w_1$", fontsize=10.5, color=cor_texto)
    ax.set_ylabel("$w_2$", fontsize=10.5, color=cor_texto)
    ax.set_title(
        r"Gradiente descendente em $J(w_1, w_2) = w_1^2 + 4w_2^2$",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)

    leg = ax.legend(frameon=False, fontsize=8.8, loc="upper right")
    for txt in leg.get_texts():
        txt.set_color(cor_texto)

    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "descida-gradiente.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
