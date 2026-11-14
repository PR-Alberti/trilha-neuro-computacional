from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier


def desenhar_caixa(
    ax: plt.Axes,
    x: float,
    y: float,
    texto: str,
    cor_borda: str,
    cor_fundo: str,
    largura: float = 2.5,
    altura: float = 0.85,
) -> None:
    caixa = patches.FancyBboxPatch(
        (x - largura / 2, y - altura / 2),
        largura,
        altura,
        boxstyle="round,pad=0.06,rounding_size=0.14",
        linewidth=1.5,
        edgecolor=cor_borda,
        facecolor=cor_fundo,
        zorder=3,
    )
    ax.add_patch(caixa)
    ax.text(
        x,
        y,
        texto,
        ha="center",
        va="center",
        fontsize=8.5,
        fontweight="bold",
        color="#1E293B",
        zorder=4,
    )


def desenhar_arvore(
    ax: plt.Axes,
    arvore: DecisionTreeClassifier,
    node: int,
    x: float,
    y: float,
    dx: float,
    dy: float,
) -> None:
    tree = arvore.tree_
    esq = int(tree.children_left[node])
    dir_ = int(tree.children_right[node])
    n_amostras = int(tree.n_node_samples[node])

    if esq == -1:
        classe = int(np.argmax(tree.value[node][0]))
        if classe == 1:
            rotulo = f"Fast-spiking\n(n = {n_amostras})"
            cor_borda, cor_fundo = "#0D9488", "#CCFBF1"
        else:
            rotulo = f"Piramidal\n(n = {n_amostras})"
            cor_borda, cor_fundo = "#4F46E5", "#E0E7FF"
        desenhar_caixa(ax, x, y, rotulo, cor_borda, cor_fundo, largura=2.0, altura=0.78)
        return

    feat = int(tree.feature[node])
    thr = float(tree.threshold[node])
    nome = "Largura" if feat == 0 else "Taxa"
    unid = "ms" if feat == 0 else "Hz"
    texto_no = f"{nome} ≤ {thr:.2f} {unid}?\n(n = {n_amostras})"
    desenhar_caixa(ax, x, y, texto_no, "#475569", "#F8FAFC", largura=2.5, altura=0.82)

    for filho, sinal, rot_ramo in ((esq, -1, "Sim"), (dir_, 1, "Não")):
        xf = x + sinal * dx
        yf = y - dy
        ax.annotate(
            "",
            xy=(xf, yf + 0.44),
            xytext=(x + sinal * 0.35, y - 0.44),
            arrowprops={"arrowstyle": "->", "color": "#64748B", "lw": 1.3},
            zorder=2,
        )
        ax.text(
            (x + xf) / 2 + sinal * 0.25,
            (y + yf) / 2 + 0.08,
            rot_ramo,
            ha="center",
            va="center",
            fontsize=8.5,
            fontweight="bold",
            color="#475569",
        )
        desenhar_arvore(ax, arvore, filho, xf, yf, dx * 0.50, dy)


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    rng = np.random.default_rng(0)
    n_por_classe = 70

    larg_pir = np.clip(rng.normal(0.78, 0.13, n_por_classe), 0.32, 1.15)
    taxa_pir = np.clip(rng.normal(16.0, 6.5, n_por_classe), 2.0, 46.0)

    larg_fs = np.clip(rng.normal(0.33, 0.08, n_por_classe), 0.16, 0.65)
    taxa_fs = np.clip(rng.normal(54.0, 15.0, n_por_classe), 18.0, 92.0)

    X = np.column_stack([
        np.concatenate([larg_pir, larg_fs]),
        np.concatenate([taxa_pir, taxa_fs]),
    ])
    y = np.array([0] * n_por_classe + [1] * n_por_classe)

    arvore = DecisionTreeClassifier(max_depth=2, random_state=0).fit(X, y)

    cor_texto = "#334155"
    cor_grade = "#94A3B8"
    cor_pir = "#4F46E5"
    cor_fs = "#0D9488"

    fig, (ax_esp, ax_arv) = plt.subplots(
        1, 2, figsize=(10.2, 4.4), gridspec_kw={"width_ratios": [1.1, 1.0]}
    )
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: espaço de variáveis e partição retangular
    xx, yy = np.meshgrid(np.linspace(0.14, 1.16, 300), np.linspace(0.0, 95.0, 300))
    grade = np.column_stack([xx.ravel(), yy.ravel()])
    zz = arvore.predict(grade).reshape(xx.shape)

    ax_esp.contourf(
        xx,
        yy,
        zz,
        levels=[-0.5, 0.5, 1.5],
        colors=["#C7D2FE", "#99F6E4"],
        alpha=0.45,
    )
    ax_esp.contour(
        xx,
        yy,
        zz,
        levels=[0.5],
        colors=["#334155"],
        linestyles="--",
        linewidths=1.6,
    )
    ax_esp.scatter(
        larg_pir,
        taxa_pir,
        color=cor_pir,
        edgecolor="#FFFFFF",
        linewidth=0.6,
        s=36,
        label="Piramidal (0)",
        zorder=3,
    )
    ax_esp.scatter(
        larg_fs,
        taxa_fs,
        color=cor_fs,
        edgecolor="#FFFFFF",
        linewidth=0.6,
        marker="^",
        s=42,
        label="Fast-spiking (1)",
        zorder=3,
    )
    ax_esp.set_title(
        "Partição do espaço em retângulos",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_esp.set_xlabel("Largura do spike (ms)", fontsize=9.5, color=cor_texto)
    ax_esp.set_ylabel("Taxa média de disparo (Hz)", fontsize=9.5, color=cor_texto)
    ax_esp.set_xlim(0.14, 1.16)
    ax_esp.set_ylim(0.0, 95.0)
    ax_esp.legend(loc="upper right", frameon=True, framealpha=0.88, fontsize=8.5)
    ax_esp.patch.set_alpha(0.0)
    ax_esp.grid(True, linestyle="--", linewidth=0.6, alpha=0.35, color=cor_grade)
    ax_esp.spines["top"].set_visible(False)
    ax_esp.spines["right"].set_visible(False)
    ax_esp.spines["left"].set_color(cor_grade)
    ax_esp.spines["bottom"].set_color(cor_grade)
    ax_esp.tick_params(colors=cor_texto, labelsize=8.5)

    # Painel direito: regras hierárquicas da árvore
    ax_arv.patch.set_alpha(0.0)
    desenhar_arvore(ax_arv, arvore, node=0, x=0.0, y=3.2, dx=2.4, dy=1.35)
    ax_arv.set_xlim(-4.8, 4.8)
    ax_arv.set_ylim(-0.2, 3.9)
    ax_arv.axis("off")
    ax_arv.set_title(
        "Árvore de decisão equivalente (profundidade 2)",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    fig.tight_layout()
    destino = Path(__file__).resolve().parent / "t08-particao.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
