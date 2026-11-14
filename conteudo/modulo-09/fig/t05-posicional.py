from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    n_pos = 50
    d_model = 32
    pos = np.arange(n_pos)[:, None]
    dim_pares = np.arange(0, d_model, 2)
    angulos = pos / (10000.0 ** (dim_pares / d_model))

    pe = np.zeros((n_pos, d_model))
    pe[:, 0::2] = np.sin(angulos)
    pe[:, 1::2] = np.cos(angulos)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"

    fig, (ax_heat, ax_curvas) = plt.subplots(
        1, 2, figsize=(10.2, 4.3), gridspec_kw={"width_ratios": [1.35, 1.0]}
    )
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: mapa de calor completo (pos 0..49, d_model 32)
    im = ax_heat.imshow(
        pe, aspect="auto", cmap="RdBu_r", vmin=-1.0, vmax=1.0, origin="lower"
    )
    ax_heat.set_title(
        "Mapa de calor ($d_{\\mathrm{model}} = 32$)",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_heat.set_xlabel("Dimensão do vetor ($j$)", fontsize=10, color=cor_texto)
    ax_heat.set_ylabel("Posição na sequência ($\\mathrm{pos}$)", fontsize=10, color=cor_texto)
    ax_heat.set_xticks([0, 7, 15, 23, 31])
    ax_heat.set_yticks([0, 10, 20, 30, 40, 49])
    ax_heat.tick_params(colors=cor_texto, labelsize=9)
    for spine in ax_heat.spines.values():
        spine.set_color(cor_grade)

    cbar = fig.colorbar(im, ax=ax_heat, fraction=0.046, pad=0.04)
    cbar.set_label("Valor de $\\mathrm{PE}$", fontsize=9.5, color=cor_texto)
    cbar.ax.tick_params(colors=cor_texto, labelsize=8.5)

    # Painel direito: curvas senoidais em três escalas de frequência
    eixo_pos = np.arange(n_pos)
    ax_curvas.plot(
        eixo_pos, pe[:, 0], color="#4F46E5", linewidth=1.8, label="$j = 0$ (rápida: $/1$)"
    )
    ax_curvas.plot(
        eixo_pos, pe[:, 8], color="#0D9488", linewidth=2.0, label="$j = 8$ (média: $/10$)"
    )
    ax_curvas.plot(
        eixo_pos, pe[:, 16], color="#D97706", linewidth=2.2, label="$j = 16$ (lenta: $/100$)"
    )
    ax_curvas.set_title(
        "Ondas em diferentes dimensões",
        fontsize=11.5,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_curvas.set_xlabel("Posição na sequência ($\\mathrm{pos}$)", fontsize=10, color=cor_texto)
    ax_curvas.set_ylabel("Amplitude $\\mathrm{PE}(\\mathrm{pos}, j)$", fontsize=10, color=cor_texto)
    ax_curvas.set_ylim(-1.15, 1.35)
    ax_curvas.set_xticks([0, 10, 20, 30, 40, 49])
    ax_curvas.patch.set_alpha(0.0)
    ax_curvas.grid(True, linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
    ax_curvas.spines["top"].set_visible(False)
    ax_curvas.spines["right"].set_visible(False)
    ax_curvas.spines["left"].set_color(cor_grade)
    ax_curvas.spines["bottom"].set_color(cor_grade)
    ax_curvas.tick_params(colors=cor_texto, labelsize=9)
    ax_curvas.legend(loc="upper right", fontsize=8.5, frameon=True, framealpha=0.85)

    fig.suptitle(
        "Codificação posicional senoidal ($\\mathrm{pos} = 0\\text{–}49$, $d_{\\mathrm{model}} = 32$)",
        fontsize=13,
        fontweight="bold",
        color=cor_texto,
        y=1.02,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "t05-posicional.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
