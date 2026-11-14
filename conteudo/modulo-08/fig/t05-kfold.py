from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    k_dobras = 5
    cor_treino = "#4F46E5"   # indigo
    cor_teste = "#0D9488"    # teal
    cor_texto = "#334155"
    cor_borda = "#FFFFFF"

    fig, ax = plt.subplots(figsize=(9.2, 4.4))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    largura_bloco = 1.6
    altura_bloco = 0.62
    espaco_x = 0.14
    espaco_y = 0.92

    for rodada in range(k_dobras):
        y_pos = (k_dobras - 1 - rodada) * espaco_y
        ax.text(
            -0.25,
            y_pos + altura_bloco / 2,
            f"Rodada {rodada + 1}",
            va="center",
            ha="right",
            fontsize=10.5,
            fontweight="bold",
            color=cor_texto,
        )

        for dobra in range(k_dobras):
            x_pos = dobra * (largura_bloco + espaco_x)
            eh_teste = dobra == rodada
            cor = cor_teste if eh_teste else cor_treino
            rotulo = "Teste" if eh_teste else "Treino"

            retangulo = patches.FancyBboxPatch(
                (x_pos, y_pos),
                largura_bloco,
                altura_bloco,
                boxstyle="round,pad=0.02,rounding_size=0.08",
                linewidth=1.2,
                edgecolor=cor_borda,
                facecolor=cor,
                alpha=0.92 if eh_teste else 0.78,
            )
            ax.add_patch(retangulo)

            ax.text(
                x_pos + largura_bloco / 2,
                y_pos + altura_bloco / 2,
                rotulo,
                va="center",
                ha="center",
                fontsize=9.5,
                fontweight="bold",
                color="#FFFFFF",
            )

        x_escore = k_dobras * (largura_bloco + espaco_x) + 0.25
        ax.text(
            x_escore,
            y_pos + altura_bloco / 2,
            f"→  Escore $E_{rodada + 1}$",
            va="center",
            ha="left",
            fontsize=10,
            color=cor_texto,
        )

    # Cabeçalho das dobras no topo
    y_topo = (k_dobras - 1) * espaco_y + altura_bloco + 0.28
    for dobra in range(k_dobras):
        x_pos = dobra * (largura_bloco + espaco_x) + largura_bloco / 2
        ax.text(
            x_pos,
            y_topo,
            f"Dobra {dobra + 1}",
            va="bottom",
            ha="center",
            fontsize=10,
            fontweight="bold",
            color=cor_texto,
        )

    # Resumo da média na base
    largura_total = k_dobras * largura_bloco + (k_dobras - 1) * espaco_x
    ax.text(
        largura_total / 2,
        -0.55,
        r"Estimativa final: $\mathrm{CV}_{(5)} = \frac{1}{5}\sum_{i=1}^{5} E_i$   (média das 5 rodadas)",
        va="center",
        ha="center",
        fontsize=10.5,
        fontweight="bold",
        color=cor_texto,
    )

    ax.set_xlim(-1.6, k_dobras * (largura_bloco + espaco_x) + 2.0)
    ax.set_ylim(-0.95, y_topo + 0.45)
    ax.axis("off")

    ax.set_title(
        "Validação cruzada 5-fold (cada amostra vai para o teste exatamente 1 vez)",
        fontsize=12,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )

    destino = Path(__file__).resolve().parent / "t05-kfold.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
