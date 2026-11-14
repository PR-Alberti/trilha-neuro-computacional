from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    g_k = 25.0  # nS
    e_k = -90.0  # mV
    g_na = 4.0  # nS
    e_na = 55.0  # mV
    v_rep = (g_k * e_k + g_na * e_na) / (g_k + g_na)  # -70.0 mV

    v = np.linspace(-110, 75, 400)
    i_k = g_k * (v - e_k)
    i_na = g_na * (v - e_na)
    i_total = i_k + i_na

    cor_texto = "#334155"
    cor_grade = "#94A3B8"
    cor_k = "#4F46E5"
    cor_na = "#0D9488"
    cor_total = "#EA580C"

    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.axhline(0, color=cor_grade, linewidth=1.2, zorder=1)
    ax.axvline(0, color=cor_grade, linewidth=1.0, linestyle=":", alpha=0.7, zorder=1)

    ax.plot(v, i_k, color=cor_k, linewidth=2.3, label="Canal de $\\mathrm{K}^+$ ($g_\\mathrm{K} = 25$ nS)")
    ax.plot(v, i_na, color=cor_na, linewidth=2.3, label="Canal de $\\mathrm{Na}^+$ ($g_\\mathrm{Na} = 4$ nS)")
    ax.plot(
        v,
        i_total,
        color=cor_total,
        linewidth=1.9,
        linestyle="--",
        label="Corrente total ($I_\\mathrm{K} + I_\\mathrm{Na}$)",
    )

    # Potenciais de reversão no eixo V
    ax.scatter([e_k], [0], color=cor_k, s=48, zorder=4)
    ax.scatter([e_na], [0], color=cor_na, s=48, zorder=4)

    ax.annotate(
        "$E_\\mathrm{K} = -90$ mV",
        xy=(e_k, 0),
        xytext=(-107, 170),
        color=cor_k,
        fontsize=9.5,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=cor_k, lw=1.1),
    )
    ax.annotate(
        "$E_\\mathrm{Na} = +55$ mV",
        xy=(e_na, 0),
        xytext=(24, -230),
        color=cor_na,
        fontsize=9.5,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=cor_na, lw=1.1),
    )

    # Equilíbrio em V_rep = -70 mV
    i_k_rep = g_k * (v_rep - e_k)      # +500 pA
    i_na_rep = g_na * (v_rep - e_na)   # -500 pA
    ax.plot([v_rep, v_rep], [i_na_rep, i_k_rep], color="#64748B", linestyle="--", linewidth=1.2, zorder=2)
    ax.scatter([v_rep, v_rep, v_rep], [i_k_rep, 0.0, i_na_rep], c=[cor_k, cor_total, cor_na], s=44, zorder=5)

    ax.annotate(
        "$+500$ pA (saída de $\\mathrm{K}^+$)",
        xy=(v_rep, i_k_rep),
        xytext=(-107, 670),
        color=cor_k,
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color=cor_k, lw=1.0),
    )
    ax.annotate(
        "$-500$ pA (entrada de $\\mathrm{Na}^+$)",
        xy=(v_rep, i_na_rep),
        xytext=(-58, -730),
        color=cor_na,
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color=cor_na, lw=1.0),
    )
    ax.annotate(
        "Repouso: $V = -70$ mV ($I_{\\mathrm{total}} = 0$)",
        xy=(v_rep, 0),
        xytext=(-44, 140),
        color=cor_total,
        fontsize=9,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=cor_total, lw=1.0),
    )

    ax.set_xlim(-110, 75)
    ax.set_ylim(-850, 1050)
    ax.set_title("Curvas corrente-voltagem ($I$-$V$) lineares de $\\mathrm{K}^+$ e $\\mathrm{Na}^+$", fontsize=12, fontweight="bold", color=cor_texto, pad=10)
    ax.set_xlabel("Potencial de membrana $V$ (mV)", fontsize=10, color=cor_texto)
    ax.set_ylabel("Corrente iônica $I$ (pA)", fontsize=10, color=cor_texto)

    ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(loc="upper right", frameon=True, framealpha=0.9, fontsize=9)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "curva-iv.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
