from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    c0 = 10.0  # mg/L
    k = 0.2    # h^-1
    t_max = 20.0
    t_parcial = 10.0

    t = np.linspace(0.0, t_max, 400)
    c = c0 * np.exp(-k * t)

    t_10 = np.linspace(0.0, t_parcial, 200)
    c_10 = c0 * np.exp(-k * t_10)

    t_cauda = np.linspace(t_parcial, t_max, 200)
    c_cauda = c0 * np.exp(-k * t_cauda)

    auc_10 = (c0 / k) * (1.0 - np.exp(-k * t_parcial))  # 43.23 mg·h/L
    auc_total = c0 / k                                  # 50.00 mg·h/L

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_curva = "#4F46E5"
    cor_cauda = "#0D9488"

    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.fill_between(
        t_10,
        0.0,
        c_10,
        color=cor_curva,
        alpha=0.22,
        label=f"AUC(0, 10 h) ≈ {auc_10:.2f} mg·h/L".replace(".", ","),
    )
    ax.fill_between(
        t_cauda,
        0.0,
        c_cauda,
        color=cor_cauda,
        alpha=0.18,
        label=f"Cauda (t ≥ 10 h): AUC total = {auc_total:.0f} mg·h/L".replace(".", ","),
    )
    ax.plot(t, c, color=cor_curva, linewidth=2.5, label="$C(t) = 10\\,e^{-0,2t}$")

    c_em_10 = c0 * np.exp(-k * t_parcial)
    ax.vlines(t_parcial, 0.0, c_em_10, color=cor_texto, linestyle="--", linewidth=1.3)
    ax.scatter([0.0, t_parcial], [c0, c_em_10], color=cor_curva, s=40, zorder=4)

    ax.annotate(
        "$C_0$ = 10 mg/L",
        xy=(0.0, c0),
        xytext=(1.0, 9.6),
        fontsize=9.5,
        color=cor_curva,
        fontweight="bold",
    )
    ax.annotate(
        f"t = 10 h\nC(10) ≈ {c_em_10:.2f} mg/L".replace(".", ","),
        xy=(t_parcial, c_em_10),
        xytext=(10.6, 2.7),
        fontsize=9,
        color=cor_texto,
        arrowprops={"arrowstyle": "->", "color": cor_texto, "lw": 1.0},
    )

    fmt_virgula = ticker.FuncFormatter(lambda val, _: f"{val:g}".replace(".", ","))
    ax.xaxis.set_major_formatter(fmt_virgula)
    ax.yaxis.set_major_formatter(fmt_virgula)

    ax.set_xlim(0.0, t_max)
    ax.set_ylim(0.0, 11.2)
    ax.set_xticks(np.arange(0, 21, 2))
    ax.set_title(
        "Área sob a curva de concentração plasmática (AUC)",
        fontsize=12,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax.set_xlabel("Tempo $t$ (h)", fontsize=10.5, color=cor_texto)
    ax.set_ylabel("Concentração $C(t)$ (mg/L)", fontsize=10.5, color=cor_texto)

    ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(loc="upper right", frameon=False, fontsize=9, labelcolor=cor_texto)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "auc-farmaco.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
