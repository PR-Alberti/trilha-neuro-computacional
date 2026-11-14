from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage, set_link_color_palette
from sklearn.preprocessing import StandardScaler


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    rng = np.random.default_rng(0)
    n_por_grupo = 6

    # Três perfis eletrofisiológicos sintéticos: (largura do spike em ms, taxa em Hz)
    larg_a = rng.normal(0.32, 0.04, n_por_grupo)
    taxa_a = rng.normal(62.0, 4.5, n_por_grupo)

    larg_b = rng.normal(0.86, 0.05, n_por_grupo)
    taxa_b = rng.normal(14.0, 3.5, n_por_grupo)

    larg_c = rng.normal(0.82, 0.05, n_por_grupo)
    taxa_c = rng.normal(46.0, 4.0, n_por_grupo)

    X = np.column_stack([
        np.concatenate([larg_a, larg_b, larg_c]),
        np.concatenate([taxa_a, taxa_b, taxa_c]),
    ])
    rotulos_neuronios = [f"N{i + 1}" for i in range(len(X))]

    X_esc = StandardScaler().fit_transform(X)
    Z = linkage(X_esc, method="ward")
    corte = 0.5 * (Z[-3, 2] + Z[-2, 2])
    grupos = fcluster(Z, t=3, criterion="maxclust")

    cor_texto = "#334155"
    cor_grade = "#94A3B8"
    paleta = ["#4F46E5", "#0D9488", "#D97706"]
    marcadores = ["o", "^", "s"]

    fig, (ax_esp, ax_den) = plt.subplots(
        1, 2, figsize=(10.4, 4.4), gridspec_kw={"width_ratios": [1.0, 1.2]}
    )
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: espaço de características após o corte em K = 3
    for idx, g in enumerate(sorted(np.unique(grupos))):
        mask = grupos == g
        ax_esp.scatter(
            X[mask, 0],
            X[mask, 1],
            color=paleta[idx % len(paleta)],
            marker=marcadores[idx % len(marcadores)],
            edgecolor="#FFFFFF",
            linewidth=0.6,
            s=54,
            label=f"Grupo {idx + 1} (n = {mask.sum()})",
            zorder=3,
        )

    ax_esp.set_title(
        "Grupos obtidos ao cortar em K = 3",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_esp.set_xlabel("Largura do spike (ms)", fontsize=9.5, color=cor_texto)
    ax_esp.set_ylabel("Taxa de disparo (Hz)", fontsize=9.5, color=cor_texto)
    ax_esp.legend(loc="lower left", frameon=True, framealpha=0.88, fontsize=8.5)
    ax_esp.patch.set_alpha(0.0)
    ax_esp.grid(True, linestyle="--", linewidth=0.6, alpha=0.35, color=cor_grade)
    ax_esp.spines["top"].set_visible(False)
    ax_esp.spines["right"].set_visible(False)
    ax_esp.spines["left"].set_color(cor_grade)
    ax_esp.spines["bottom"].set_color(cor_grade)
    ax_esp.tick_params(colors=cor_texto, labelsize=8.5)

    # Painel direito: dendrograma de Ward sobre dados padronizados
    set_link_color_palette(paleta)
    dendrogram(
        Z,
        labels=rotulos_neuronios,
        ax=ax_den,
        color_threshold=corte,
        above_threshold_color="#64748B",
        leaf_rotation=90,
        leaf_font_size=8.0,
    )
    set_link_color_palette(None)
    ax_den.axhline(
        corte,
        color="#E11D48",
        linestyle="--",
        linewidth=1.5,
        label=f"Corte (h = {corte:.2f}, K = 3)",
    )
    ax_den.set_title(
        "Dendrograma (ligação de Ward)",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_den.set_xlabel("Neurônios registrados", fontsize=9.5, color=cor_texto)
    ax_den.set_ylabel("Distância de fusão (dados padronizados)", fontsize=9.5, color=cor_texto)
    ax_den.legend(loc="upper right", frameon=True, framealpha=0.88, fontsize=8.5)
    ax_den.patch.set_alpha(0.0)
    ax_den.grid(True, axis="y", linestyle="--", linewidth=0.6, alpha=0.35, color=cor_grade)
    ax_den.spines["top"].set_visible(False)
    ax_den.spines["right"].set_visible(False)
    ax_den.spines["left"].set_color(cor_grade)
    ax_den.spines["bottom"].set_color(cor_grade)
    ax_den.tick_params(colors=cor_texto, labelsize=8.5)

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "t09-dendrograma.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
