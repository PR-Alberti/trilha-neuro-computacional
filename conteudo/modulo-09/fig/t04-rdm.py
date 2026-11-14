from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    digits = load_digits()
    x = digits.data / 16.0
    y = digits.target

    prototipos = np.array([x[y == d].mean(axis=0) for d in range(10)])
    rdm = 1.0 - np.corrcoef(prototipos)

    cor_texto = "#475569"

    fig, ax = plt.subplots(figsize=(6.8, 5.8))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    im = ax.imshow(rdm, cmap="viridis", vmin=0.0, vmax=float(np.max(rdm)))

    ticks = np.arange(10)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels([str(d) for d in range(10)])
    ax.set_yticklabels([str(d) for d in range(10)])
    ax.set_xlabel("Dígito", fontsize=10.5, color=cor_texto, labelpad=8)
    ax.set_ylabel("Dígito", fontsize=10.5, color=cor_texto, labelpad=8)
    ax.set_title(
        "RDM dos 10 dígitos em espaço de pixels (load_digits)",
        fontsize=12,
        fontweight="bold",
        color=cor_texto,
        pad=12,
    )
    ax.tick_params(colors=cor_texto, labelsize=9.5)

    limiar_texto = float(np.max(rdm)) * 0.55
    for i in range(10):
        for j in range(10):
            valor = rdm[i, j]
            cor_celula = "white" if valor < limiar_texto else "#1E293B"
            ax.text(
                j,
                i,
                f"{valor:.2f}".replace(".", ","),
                ha="center",
                va="center",
                fontsize=7.5,
                color=cor_celula,
            )

    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Dissimilaridade (1 − correlação de Pearson)", fontsize=9.5, color=cor_texto)
    cbar.ax.tick_params(colors=cor_texto, labelsize=8.5)

    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "t04-rdm.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
