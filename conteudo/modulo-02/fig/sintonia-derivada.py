from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    r_max = 80.0
    theta_pref = 90.0
    sigma = 20.0

    theta = np.linspace(30.0, 150.0, 400)
    f_theta = r_max * np.exp(-((theta - theta_pref) ** 2) / (2.0 * (sigma ** 2)))
    df_theta = -((theta - theta_pref) / (sigma ** 2)) * f_theta

    t_flanco_esq = theta_pref - sigma  # 70 graus
    t_flanco_dir = theta_pref + sigma  # 110 graus
    f_flanco = r_max * np.exp(-0.5)
    df_flanco_esq = (sigma / (sigma ** 2)) * f_flanco
    df_flanco_dir = -df_flanco_esq

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_curva = "#4F46E5"
    cor_deriv = "#0D9488"
    cor_destaque = "#E11D48"

    fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(7.6, 5.8), sharex=True)
    fig.patch.set_alpha(0.0)

    # Painel superior: curva de sintonia f(theta)
    ax_top.plot(theta, f_theta, color=cor_curva, linewidth=2.4, label="$f(\\theta)$")
    ax_top.scatter(
        [t_flanco_esq, theta_pref, t_flanco_dir],
        [f_flanco, r_max, f_flanco],
        color=cor_destaque,
        s=42,
        zorder=5,
    )
    ax_top.annotate(
        "Pico ($\\theta_{\\mathrm{pref}} = 90^\\circ$, 80 Hz)",
        xy=(theta_pref, r_max),
        xytext=(theta_pref + 6.0, r_max - 4.0),
        fontsize=8.8,
        color=cor_destaque,
    )
    ax_top.annotate(
        "Flanco ($70^\\circ$)",
        xy=(t_flanco_esq, f_flanco),
        xytext=(43.0, f_flanco + 5.0),
        fontsize=8.8,
        color=cor_texto,
    )
    ax_top.annotate(
        "Flanco ($110^\\circ$)",
        xy=(t_flanco_dir, f_flanco),
        xytext=(114.0, f_flanco + 5.0),
        fontsize=8.8,
        color=cor_texto,
    )
    ax_top.set_ylabel("Taxa de disparo $f(\\theta)$ (Hz)", fontsize=10, color=cor_texto)
    ax_top.set_ylim(-4.0, 92.0)
    ax_top.set_title(
        "Curva de sintonia gaussiana e sua derivada ($r_{\\max} = 80$ Hz, $\\theta_{\\mathrm{pref}} = 90^\\circ$, $\\sigma = 20^\\circ$)",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    # Painel inferior: derivada f'(theta)
    ax_bot.axhline(0.0, color=cor_grade, linewidth=1.0, linestyle="-")
    ax_bot.plot(theta, df_theta, color=cor_deriv, linewidth=2.4, label="$f'(\\theta)$")
    ax_bot.scatter(
        [t_flanco_esq, theta_pref, t_flanco_dir],
        [df_flanco_esq, 0.0, df_flanco_dir],
        color=cor_destaque,
        s=42,
        zorder=5,
    )
    ax_bot.annotate(
        "$f'(90^\\circ) = 0$",
        xy=(theta_pref, 0.0),
        xytext=(theta_pref + 4.0, 0.45),
        fontsize=8.8,
        color=cor_destaque,
    )
    ax_bot.annotate(
        "Máximo ($+2{,}43$ Hz/$^\\circ$)",
        xy=(t_flanco_esq, df_flanco_esq),
        xytext=(34.0, df_flanco_esq + 0.35),
        fontsize=8.8,
        color=cor_destaque,
    )
    ax_bot.annotate(
        "Mínimo ($-2{,}43$ Hz/$^\\circ$)",
        xy=(t_flanco_dir, df_flanco_dir),
        xytext=(112.0, df_flanco_dir - 0.55),
        fontsize=8.8,
        color=cor_destaque,
    )
    ax_bot.set_xlabel("Orientação do estímulo $\\theta$ (graus)", fontsize=10, color=cor_texto)
    ax_bot.set_ylabel("$f'(\\theta)$ (Hz/$^\\circ$)", fontsize=10, color=cor_texto)
    ax_bot.set_ylim(-3.2, 3.2)
    ax_bot.set_xticks([30, 50, 70, 90, 110, 130, 150])

    for ax in (ax_top, ax_bot):
        ax.patch.set_alpha(0.0)
        for pos in (t_flanco_esq, theta_pref, t_flanco_dir):
            ax.axvline(pos, color=cor_destaque, linestyle=":", linewidth=1.1, alpha=0.55)
        ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "sintonia-derivada.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
