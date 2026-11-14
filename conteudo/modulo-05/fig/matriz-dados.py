from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def main() -> None:
    # Grade determinística: 8 neurônios x 50 instantes de tempo
    n_neuronios = 8
    n_instantes = 50
    t = np.arange(1, n_instantes + 1)

    # Taxas sintéticas (Hz) com base constante e oscilações de fases/frequências distintas
    X = np.zeros((n_neuronios, n_instantes))
    fases = np.linspace(0.0, 1.5 * np.pi, n_neuronios)
    frequencias = np.array([0.14, 0.18, 0.12, 0.22, 0.16, 0.25, 0.11, 0.20])
    bases = np.array([18.0, 22.0, 15.0, 25.0, 20.0, 28.0, 16.0, 24.0])
    amplitudes = np.array([8.0, 12.0, 6.0, 10.0, 9.0, 13.0, 7.0, 11.0])

    for i in range(n_neuronios):
        X[i, :] = bases[i] + amplitudes[i] * np.sin(frequencias[i] * t + fases[i])

    # Cores sóbrias alinhadas ao padrão do projeto
    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_n2 = "#4F46E5"   # índigo (Neurônio 2)
    cor_n6 = "#0D9488"   # verde-azulado (Neurônio 6)
    cor_col = "#D97706"  # âmbar (instante t = 20)

    idx_n2 = 1
    idx_n6 = 5
    t_destaque = 20
    idx_col = t_destaque - 1

    fig, (ax_img, ax_ts) = plt.subplots(
        1, 2, figsize=(10.4, 4.3), gridspec_kw={"width_ratios": [1.15, 1.0]}
    )
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: matriz inteira como mapa de calor
    im = ax_img.imshow(X, aspect="auto", cmap="viridis", interpolation="nearest")
    cbar = fig.colorbar(im, ax=ax_img, pad=0.03)
    cbar.set_label("Taxa de disparo (Hz)", fontsize=9.5, color=cor_texto)
    cbar.ax.tick_params(colors=cor_texto, labelsize=8.5)

    # Destaque das duas linhas (séries temporais) e de uma coluna (vetor de população)
    ret_n2 = patches.Rectangle(
        (-0.5, idx_n2 - 0.5),
        n_instantes,
        1.0,
        linewidth=1.5,
        linestyle="--",
        edgecolor=cor_n2,
        facecolor="none",
        zorder=3,
    )
    ret_n6 = patches.Rectangle(
        (-0.5, idx_n6 - 0.5),
        n_instantes,
        1.0,
        linewidth=1.5,
        linestyle="--",
        edgecolor=cor_n6,
        facecolor="none",
        zorder=3,
    )
    ret_col = patches.Rectangle(
        (idx_col - 0.5, -0.5),
        1.0,
        n_neuronios,
        linewidth=1.9,
        edgecolor=cor_col,
        facecolor="none",
        zorder=4,
    )
    ax_img.add_patch(ret_n2)
    ax_img.add_patch(ret_n6)
    ax_img.add_patch(ret_col)

    ax_img.set_title(
        "Matriz de dados $\\mathbf{X}$ ($8 \\times 50$)",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_img.set_xlabel("Tempo (instante $t$)", fontsize=10, color=cor_texto)
    ax_img.set_ylabel("Neurônio $i$", fontsize=10, color=cor_texto)
    ax_img.set_yticks(np.arange(n_neuronios))
    ax_img.set_yticklabels([str(i) for i in range(1, n_neuronios + 1)])
    ax_img.set_xticks([0, 9, 19, 29, 39, 49])
    ax_img.set_xticklabels(["1", "10", "20", "30", "40", "50"])
    ax_img.tick_params(colors=cor_texto, labelsize=9)
    for spine in ax_img.spines.values():
        spine.set_edgecolor(cor_grade)

    # Painel direito: séries temporais de duas linhas e destaque da coluna t = 20
    ax_ts.axvspan(t_destaque - 0.6, t_destaque + 0.6, color=cor_col, alpha=0.16, zorder=1)
    ax_ts.axvline(
        t_destaque,
        color=cor_col,
        linestyle="--",
        linewidth=1.6,
        label=f"Coluna $t = {t_destaque}$ (população)",
        zorder=2,
    )
    ax_ts.plot(
        t,
        X[idx_n2, :],
        color=cor_n2,
        linewidth=2.0,
        label="Neurônio 2 (linha 2)",
        zorder=3,
    )
    ax_ts.plot(
        t,
        X[idx_n6, :],
        color=cor_n6,
        linewidth=2.0,
        label="Neurônio 6 (linha 6)",
        zorder=3,
    )
    ax_ts.scatter(
        [t_destaque, t_destaque],
        [X[idx_n2, idx_col], X[idx_n6, idx_col]],
        color=[cor_n2, cor_n6],
        s=34,
        zorder=4,
    )

    ax_ts.set_title(
        "Séries temporais (linhas) e instante (coluna)",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_ts.set_xlabel("Tempo (instante $t$)", fontsize=10, color=cor_texto)
    ax_ts.set_ylabel("Taxa de disparo (Hz)", fontsize=10, color=cor_texto)
    ax_ts.set_xlim(1, n_instantes)
    ax_ts.set_ylim(0, 56)
    ax_ts.set_xticks([1, 10, 20, 30, 40, 50])
    ax_ts.patch.set_alpha(0.0)
    ax_ts.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax_ts.spines["top"].set_visible(False)
    ax_ts.spines["right"].set_visible(False)
    ax_ts.spines["left"].set_color(cor_grade)
    ax_ts.spines["bottom"].set_color(cor_grade)
    ax_ts.tick_params(colors=cor_texto, labelsize=9)
    ax_ts.legend(loc="upper right", frameon=True, framealpha=0.88, fontsize=8.5)

    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "matriz-dados.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
