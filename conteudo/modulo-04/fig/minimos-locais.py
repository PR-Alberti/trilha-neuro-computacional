from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def j_func(w):
    return w**4 - 4.0 * w**2 + w


def j_deriv(w):
    return 4.0 * w**3 - 8.0 * w + 1.0


def executar_gd_1d(w0, eta, n_passos):
    w = float(w0)
    traj = [w]
    for _ in range(n_passos):
        w = w - eta * j_deriv(w)
        traj.append(w)
    return np.array(traj)


def main() -> None:
    w_grid = np.linspace(-2.1, 2.1, 400)
    j_grid = j_func(w_grid)

    traj_esq = executar_gd_1d(w0=-0.2, eta=0.04, n_passos=15)
    traj_dir = executar_gd_1d(w0=0.4, eta=0.04, n_passos=15)

    w_glob, j_glob = -1.473, j_func(-1.473)
    w_loc, j_loc = 1.347, j_func(1.347)
    w_max, j_max = 0.126, j_func(0.126)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_curva = "#64748B"
    cor_glob = "#0D9488"
    cor_loc = "#4F46E5"
    cor_destaque = "#E11D48"

    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.plot(w_grid, j_grid, color=cor_curva, linewidth=2.0, label=r"$J(w) = w^4 - 4w^2 + w$", zorder=2)

    ax.plot(
        traj_esq,
        j_func(traj_esq),
        color=cor_glob,
        marker="o",
        markersize=4.5,
        linewidth=1.5,
        label=r"Partindo de $w_0 = -0{,}2$ ($\eta = 0{,}04$)",
        zorder=4,
    )
    ax.plot(
        traj_dir,
        j_func(traj_dir),
        color=cor_loc,
        marker="s",
        markersize=4.2,
        linewidth=1.5,
        label=r"Partindo de $w_0 = 0{,}4$ ($\eta = 0{,}04$)",
        zorder=4,
    )

    ax.scatter([w_glob, w_loc], [j_glob, j_loc], marker="*", s=160, color=cor_destaque, zorder=6)
    ax.scatter([w_max], [j_max], marker="^", s=75, color=cor_destaque, zorder=6)

    ax.annotate(
        "mínimo global\n" + r"($w \approx -1{,}47$)",
        xy=(w_glob, j_glob),
        xytext=(-1.55, -2.1),
        ha="center",
        color=cor_destaque,
        fontsize=8.8,
        fontweight="bold",
        arrowprops={"arrowstyle": "->", "color": cor_destaque, "lw": 1.1},
        zorder=7,
    )
    ax.annotate(
        "mínimo local\n" + r"($w \approx 1{,}35$)",
        xy=(w_loc, j_loc),
        xytext=(1.15, 0.9),
        ha="center",
        color=cor_destaque,
        fontsize=8.8,
        fontweight="bold",
        arrowprops={"arrowstyle": "->", "color": cor_destaque, "lw": 1.1},
        zorder=7,
    )
    ax.annotate(
        "barreira (máximo local)\n" + r"($w \approx 0{,}13$)",
        xy=(w_max, j_max),
        xytext=(-0.25, 2.4),
        ha="center",
        color=cor_texto,
        fontsize=8.5,
        arrowprops={"arrowstyle": "->", "color": cor_texto, "lw": 1.0},
        zorder=7,
    )

    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-6.4, 4.4)
    ax.set_xlabel("$w$", fontsize=10.5, color=cor_texto)
    ax.set_ylabel("$J(w)$", fontsize=10.5, color=cor_texto)
    ax.set_title(
        "Bacias de atração em uma paisagem não convexa",
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

    leg = ax.legend(frameon=False, fontsize=8.5, loc="upper left")
    for txt in leg.get_texts():
        txt.set_color(cor_texto)

    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "minimos-locais.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
