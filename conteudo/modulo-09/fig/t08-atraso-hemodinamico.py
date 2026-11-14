from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    t = np.linspace(0, 18, 400)
    # Resposta impulsiva hemodinâmica estilizada (pico em ~5 s e pós-depressão suave)
    pico = (t / 5.0) ** 5 * np.exp(-(t - 5.0))
    depressao = 0.25 * (t / 12.0) ** 12 * np.exp(-(t - 12.0))
    bold = pico - depressao

    trs = np.array([2.0, 4.0, 6.0, 8.0])
    bold_trs = (trs / 5.0) ** 5 * np.exp(-(trs - 5.0)) - 0.25 * (
        trs / 12.0
    ) ** 12 * np.exp(-(trs - 12.0))

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_curva = "#4F46E5"
    cor_trs = "#0D9488"
    cor_estimulo = "#E11D48"

    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.axhline(0, color=cor_grade, linewidth=0.9, linestyle="-")
    ax.axvline(0, color=cor_estimulo, linewidth=2.0, linestyle="-", label="Palavra ouvida (t = 0 s)")
    ax.plot(t, bold, color=cor_curva, linewidth=2.4, label="Resposta BOLD")
    ax.vlines(trs, 0, bold_trs, color=cor_trs, linestyle="--", linewidth=1.3, alpha=0.8)
    ax.scatter(trs, bold_trs, color=cor_trs, s=48, zorder=4, label="Amostras com atraso (1 a 4 TRs)")

    ax.axvspan(4.0, 6.0, color=cor_curva, alpha=0.09)
    ax.text(5.0, 1.04, "Pico (~4–6 s)", ha="center", va="bottom", fontsize=9.5, color=cor_curva, fontweight="bold")

    for i, (tr_t, tr_y) in enumerate(zip(trs, bold_trs), start=1):
        ax.text(
            tr_t,
            tr_y + 0.055,
            f"TR+{i}",
            ha="center",
            va="bottom",
            fontsize=8.5,
            color=cor_trs,
            fontweight="bold",
        )

    ax.set_title(
        "Atraso hemodinâmico no fMRI (TR = 2 s)",
        fontsize=12,
        fontweight="bold",
        color=cor_texto,
        pad=12,
    )
    ax.set_xlabel("Tempo após o estímulo (s)", fontsize=10, color=cor_texto)
    ax.set_ylabel("Sinal BOLD relativo (u.a.)", fontsize=10, color=cor_texto)
    ax.set_xlim(-0.8, 18.0)
    ax.set_ylim(-0.30, 1.18)
    ax.set_xticks(np.arange(0, 19, 2))

    ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)
    ax.tick_params(colors=cor_texto, labelsize=9)
    ax.legend(frameon=False, loc="upper right", fontsize=9, labelcolor=cor_texto)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "t08-atraso-hemodinamico.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
