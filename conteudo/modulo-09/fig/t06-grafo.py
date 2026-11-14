from pathlib import Path

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    # Matriz de adjacência de um grafo não direcionado com 6 nós (numerados de 1 a 6)
    # Arestas: (1,2), (1,6), (2,3), (2,6), (3,4), (3,5), (4,5), (5,6)
    A = np.array(
        [
            [0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 1, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 1, 1, 0, 1],
            [1, 1, 0, 0, 1, 0],
        ],
        dtype=int,
    )

    # Coordenadas planas em hexágono regular (sem cruzamento de arestas)
    angulos = np.linspace(np.pi / 2, np.pi / 2 - 2 * np.pi, 6, endpoint=False)
    coords = np.column_stack([np.cos(angulos), np.sin(angulos)])

    cor_texto = "#334155"
    cor_aresta = "#64748B"
    cor_no = "#4F46E5"
    cor_borda_no = "#312E81"
    cor_zero = "#F8FAFC"
    cor_um = "#4F46E5"
    cor_grade = "#CBD5E1"

    fig, (ax_grafo, ax_mat) = plt.subplots(1, 2, figsize=(9.4, 4.3))
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: desenho do grafo
    ax_grafo.patch.set_alpha(0.0)
    n = A.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            if A[i, j] == 1:
                ax_grafo.plot(
                    [coords[i, 0], coords[j, 0]],
                    [coords[i, 1], coords[j, 1]],
                    color=cor_aresta,
                    linewidth=2.0,
                    zorder=1,
                )

    ax_grafo.scatter(
        coords[:, 0],
        coords[:, 1],
        s=520,
        color=cor_no,
        edgecolors=cor_borda_no,
        linewidths=1.8,
        zorder=2,
    )

    for idx in range(n):
        ax_grafo.text(
            coords[idx, 0],
            coords[idx, 1],
            str(idx + 1),
            color="#FFFFFF",
            fontsize=11,
            fontweight="bold",
            ha="center",
            va="center",
            zorder=3,
        )

    ax_grafo.set_xlim(-1.35, 1.35)
    ax_grafo.set_ylim(-1.35, 1.35)
    ax_grafo.set_aspect("equal")
    ax_grafo.axis("off")
    ax_grafo.set_title(
        "Grafo não direcionado ($n = 6$ nós)",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    # Painel direito: matriz de adjacência A
    ax_mat.patch.set_alpha(0.0)
    cmap_binario = ListedColormap([cor_zero, cor_um])
    ax_mat.imshow(A, cmap=cmap_binario, vmin=0, vmax=1, aspect="equal")

    for i in range(n):
        for j in range(n):
            valor = A[i, j]
            cor_num = "#FFFFFF" if valor == 1 else cor_texto
            ax_mat.text(
                j,
                i,
                str(valor),
                ha="center",
                va="center",
                color=cor_num,
                fontsize=10.5,
                fontweight="bold" if valor == 1 else "normal",
            )

    ax_mat.set_xticks(range(n))
    ax_mat.set_yticks(range(n))
    ax_mat.set_xticklabels([str(k) for k in range(1, n + 1)], fontsize=9.5, color=cor_texto)
    ax_mat.set_yticklabels([str(k) for k in range(1, n + 1)], fontsize=9.5, color=cor_texto)
    ax_mat.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax_mat.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax_mat.grid(which="minor", color=cor_grade, linestyle="-", linewidth=1.0)
    ax_mat.tick_params(which="minor", bottom=False, left=False)
    ax_mat.set_xlabel("Nó $j$", fontsize=10, color=cor_texto)
    ax_mat.set_ylabel("Nó $i$", fontsize=10, color=cor_texto)
    ax_mat.set_title(
        "Matriz de adjacência $\\mathbf{A}$ ($6 \\times 6$)",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    for spine in ax_mat.spines.values():
        spine.set_color(cor_grade)

    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "t06-grafo.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
