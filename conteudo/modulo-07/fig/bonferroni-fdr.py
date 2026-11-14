from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def bh_mascara(p_valores: np.ndarray, q: float = 0.05) -> np.ndarray:
    m = len(p_valores)
    ordem = np.argsort(p_valores)
    p_ord = p_valores[ordem]
    limiares = (np.arange(1, m + 1) / m) * q
    passam = np.where(p_ord <= limiares)[0]
    rejeita = np.zeros(m, dtype=bool)
    if len(passam) > 0:
        k_max = passam[-1]
        rejeita[ordem[: k_max + 1]] = True
    return rejeita


def main() -> None:
    rng = np.random.default_rng(42)
    m = 200
    n_ativos = 25
    n_nulos = m - n_ativos
    alpha = 0.05
    q = 0.05

    z_nulos = rng.normal(loc=0.0, scale=1.0, size=n_nulos)
    z_ativos = rng.normal(loc=3.2, scale=1.0, size=n_ativos)
    z_todos = np.concatenate([z_nulos, z_ativos])

    p_valores = 2.0 * stats.norm.sf(np.abs(z_todos))
    ordem = np.argsort(p_valores)
    p_ord = p_valores[ordem]
    k = np.arange(1, m + 1)

    limiar_bonf = alpha / m
    reta_bh = (k / m) * q

    rej_bonf = p_ord <= limiar_bonf
    rej_bh = bh_mascara(p_ord, q=q)
    apenas_bh = rej_bh & (~rej_bonf)
    nao_rej = ~rej_bh

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_bonf = "#DC2626"
    cor_bh = "#4F46E5"
    cor_apenas_bh = "#0D9488"
    cor_neutro = "#94A3B8"

    plt.rcParams["svg.fonttype"] = "none"

    fig, (ax_log, ax_zoom) = plt.subplots(1, 2, figsize=(10.2, 4.4))
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: todos os m = 200 p-valores em escala logarítmica
    ax_log.scatter(
        k[nao_rej], p_ord[nao_rej],
        color=cor_neutro, s=16, alpha=0.75,
        label=f"Não rejeitados ({int(nao_rej.sum())})", zorder=2,
    )
    ax_log.scatter(
        k[apenas_bh], p_ord[apenas_bh],
        color=cor_apenas_bh, s=26,
        label=f"Só BH ({int(apenas_bh.sum())})", zorder=3,
    )
    ax_log.scatter(
        k[rej_bonf], p_ord[rej_bonf],
        color=cor_bonf, s=26,
        label=f"Bonferroni e BH ({int(rej_bonf.sum())})", zorder=4,
    )
    ax_log.plot(k, reta_bh, color=cor_bh, linewidth=2.0, label="Limiar BH: $(k/m)q$", zorder=3)
    ax_log.axhline(
        limiar_bonf, color=cor_bonf, linestyle="--", linewidth=1.6,
        label="Bonferroni: $\\alpha/m$", zorder=3,
    )
    ax_log.axhline(
        alpha, color="#64748B", linestyle=":", linewidth=1.3,
        label="Sem correção: $\\alpha = 0{,}05$", zorder=2,
    )
    ax_log.set_yscale("log")
    ax_log.set_xlim(0, m + 5)
    ax_log.set_ylim(1e-7, 1.5)
    ax_log.set_title("Visão geral ($m = 200$, escala log)", fontsize=11.5, fontweight="bold", color=cor_texto, pad=10)
    ax_log.set_xlabel("Posição ordenada $k$", fontsize=10, color=cor_texto)
    ax_log.set_ylabel("p-valor ordenado $p_{(k)}$", fontsize=10, color=cor_texto)
    ax_log.legend(fontsize=8.2, frameon=False, loc="lower right")

    # Painel direito: zoom linear nos menores k para destacar a reta de BH
    k_max_zoom = 35
    mask_zoom = k <= k_max_zoom
    ax_zoom.scatter(
        k[mask_zoom & nao_rej], p_ord[mask_zoom & nao_rej],
        color=cor_neutro, s=22, alpha=0.85, zorder=2,
    )
    ax_zoom.scatter(
        k[mask_zoom & apenas_bh], p_ord[mask_zoom & apenas_bh],
        color=cor_apenas_bh, s=30, zorder=3,
    )
    ax_zoom.scatter(
        k[mask_zoom & rej_bonf], p_ord[mask_zoom & rej_bonf],
        color=cor_bonf, s=30, zorder=4,
    )
    ax_zoom.plot(k[mask_zoom], reta_bh[mask_zoom], color=cor_bh, linewidth=2.0, zorder=3)
    ax_zoom.axhline(limiar_bonf, color=cor_bonf, linestyle="--", linewidth=1.6, zorder=3)

    if np.any(rej_bh):
        k_corte = int(k[rej_bh][-1])
        ax_zoom.axvline(k_corte, color=cor_apenas_bh, linestyle="-.", linewidth=1.2, alpha=0.85)
        desloc, alinhamento = (0.7, "left") if k_corte <= 25 else (-0.7, "right")
        ax_zoom.text(
            k_corte + desloc, 0.0082,
            f"Maior $k = {k_corte}$",
            color=cor_apenas_bh, fontsize=9, fontweight="bold", ha=alinhamento,
        )

    ax_zoom.set_xlim(0, k_max_zoom + 1)
    ax_zoom.set_ylim(-0.0004, 0.010)
    ax_zoom.set_title("Zoom nos menores $k$ (escala linear)", fontsize=11.5, fontweight="bold", color=cor_texto, pad=10)
    ax_zoom.set_xlabel("Posição ordenada $k$", fontsize=10, color=cor_texto)
    ax_zoom.set_ylabel("p-valor ordenado $p_{(k)}$", fontsize=10, color=cor_texto)

    for ax in (ax_log, ax_zoom):
        ax.patch.set_alpha(0.0)
        ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    fig.suptitle(
        "Comparações múltiplas ($m = 200$, $\\alpha = q = 0{,}05$): Bonferroni vs. Benjamini–Hochberg",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        y=1.02,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "bonferroni-fdr.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
