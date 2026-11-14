from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    t = np.linspace(0.0, 1.0, 1600)

    bandas = [
        ("Banda teta", 6, "#0D9488"),
        ("Banda alfa", 10, "#4F46E5"),
        ("Banda beta", 20, "#D97706"),
        ("Banda gama", 40, "#E11D48"),
    ]

    cor_texto = "#475569"
    cor_grade = "#94A3B8"

    fig, axes = plt.subplots(4, 1, figsize=(8.4, 6.6), sharex=True, sharey=True)
    fig.patch.set_alpha(0.0)

    for ax, (nome, freq, cor) in zip(axes, bandas):
        y = np.sin(2.0 * np.pi * freq * t)
        ax.patch.set_alpha(0.0)
        ax.axhline(0.0, color=cor_grade, linestyle="-", linewidth=0.8, alpha=0.55)
        ax.plot(t, y, color=cor, linewidth=1.85)

        ax.set_title(
            f"{nome} — {freq} Hz ({freq} ciclos em 1 s)",
            loc="left",
            fontsize=10.5,
            fontweight="bold",
            color=cor_texto,
            pad=6,
        )
        ax.set_ylim(-1.25, 1.25)
        ax.set_yticks([-1.0, 0.0, 1.0])
        ax.set_yticklabels(["-1", "0", "1"])
        ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    axes[-1].set_xlim(0.0, 1.0)
    axes[-1].set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    axes[-1].xaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{x:.1f}".replace(".", ","))
    )
    axes[-1].set_xlabel("Tempo $t$ (s)", fontsize=10.5, color=cor_texto, labelpad=6)

    fig.text(
        0.01,
        0.5,
        "Amplitude normalizada",
        va="center",
        rotation="vertical",
        fontsize=10.5,
        color=cor_texto,
    )

    fig.suptitle(
        "Oscilações sinusoidais nas bandas de frequência do EEG (1 s)",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        y=0.99,
    )
    fig.tight_layout(rect=[0.03, 0.0, 1.0, 0.96])

    destino = Path(__file__).resolve().parent / "senoides-eeg.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
