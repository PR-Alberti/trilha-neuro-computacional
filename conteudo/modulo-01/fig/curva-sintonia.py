from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def gaussiana(theta: np.ndarray, r_max: float, theta_pref: float, sigma: float) -> np.ndarray:
    return r_max * np.exp(-((theta - theta_pref) ** 2) / (2.0 * (sigma ** 2)))


def main() -> None:
    r_max = 50.0
    theta_pref = 90.0
    sigma = 20.0

    theta = np.linspace(0.0, 180.0, 361)
    taxa_ref = gaussiana(theta, r_max, theta_pref, sigma)
    taxa_ganho = gaussiana(theta, 75.0, theta_pref, sigma)
    taxa_desloc = gaussiana(theta, r_max, 130.0, sigma)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_ref = "#4F46E5"
    cor_ganho = "#0D9488"
    cor_desloc = "#D97706"

    fig, (ax_ref, ax_trans) = plt.subplots(1, 2, figsize=(9.8, 4.2))
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: curva de referencia com theta_pref e theta_pref +- sigma
    ax_ref.plot(theta, taxa_ref, color=cor_ref, linewidth=2.3)

    theta_esq = theta_pref - sigma
    theta_dir = theta_pref + sigma
    r_sigma = float(gaussiana(np.array([theta_dir]), r_max, theta_pref, sigma)[0])

    ax_ref.plot([theta_pref, theta_pref], [0.0, r_max], color=cor_grade, linestyle="--", linewidth=1.2)
    ax_ref.plot([theta_esq, theta_esq], [0.0, r_sigma], color=cor_grade, linestyle=":", linewidth=1.2)
    ax_ref.plot([theta_dir, theta_dir], [0.0, r_sigma], color=cor_grade, linestyle=":", linewidth=1.2)
    ax_ref.plot([theta_esq, theta_dir], [r_sigma, r_sigma], color=cor_ganho, linestyle="-", linewidth=1.5)

    ax_ref.scatter(
        [theta_esq, theta_pref, theta_dir],
        [r_sigma, r_max, r_sigma],
        color=[cor_ganho, cor_ref, cor_ganho],
        s=38,
        zorder=4,
    )

    ax_ref.annotate(
        "Pico: $(90^\\circ,\\ 50\\ \\mathrm{Hz})$",
        xy=(theta_pref, r_max),
        xytext=(106.0, 53.5),
        fontsize=8.6,
        color=cor_texto,
        arrowprops={"arrowstyle": "->", "color": cor_texto, "lw": 1.0},
    )

    ax_ref.annotate(
        "$\\theta_{\\mathrm{pref}} \\pm \\sigma$\n$(70^\\circ\\ \\mathrm{e}\\ 110^\\circ,\\ \\approx 30{,}3\\ \\mathrm{Hz})$",
        xy=(theta_dir, r_sigma),
        xytext=(118.0, 22.0),
        fontsize=8.2,
        color=cor_ganho,
        arrowprops={"arrowstyle": "->", "color": cor_ganho, "lw": 1.0},
    )

    ax_ref.set_title(
        "Curva de sintonia de referência",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_ref.set_xlabel("Orientação do estímulo $\\theta$ (graus)", fontsize=10, color=cor_texto)
    ax_ref.set_ylabel("Taxa de disparo $f(\\theta)$ (Hz)", fontsize=10, color=cor_texto)
    ax_ref.set_xlim(0.0, 180.0)
    ax_ref.set_ylim(0.0, 62.0)
    ax_ref.set_xticks([0, 30, 70, 90, 110, 150, 180])

    # Painel direito: transformacoes (ganho e deslocamento horizontal)
    ax_trans.plot(
        theta,
        taxa_ref,
        color=cor_ref,
        linewidth=1.9,
        linestyle="--",
        label="Base: $r_{\\mathrm{max}}=50$ Hz, $\\theta_{\\mathrm{pref}}=90^\\circ$",
    )
    ax_trans.plot(
        theta,
        taxa_ganho,
        color=cor_ganho,
        linewidth=2.3,
        label="Ganho $1{,}5\\cdot f(\\theta)$: $r_{\\mathrm{max}}=75$ Hz",
    )
    ax_trans.plot(
        theta,
        taxa_desloc,
        color=cor_desloc,
        linewidth=2.3,
        label="Deslocamento $f(\\theta - 40^\\circ)$: $\\theta_{\\mathrm{pref}}=130^\\circ$",
    )

    ax_trans.set_title(
        "Transformações: ganho e deslocamento",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_trans.set_xlabel("Orientação do estímulo $\\theta$ (graus)", fontsize=10, color=cor_texto)
    ax_trans.set_ylabel("Taxa de disparo (Hz)", fontsize=10, color=cor_texto)
    ax_trans.set_xlim(0.0, 180.0)
    ax_trans.set_ylim(0.0, 105.0)
    ax_trans.set_xticks([0, 30, 60, 90, 130, 180])
    ax_trans.set_yticks([0, 25, 50, 75])
    ax_trans.legend(loc="upper left", frameon=False, fontsize=8.0, labelcolor=cor_texto)

    for ax in (ax_ref, ax_trans):
        ax.patch.set_alpha(0.0)
        ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=8.8)

    fig.suptitle(
        "Curva de sintonia gaussiana de orientação ($\\sigma = 20^\\circ$)",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        y=1.02,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "curva-sintonia.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
