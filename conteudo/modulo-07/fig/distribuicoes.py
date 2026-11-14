import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    plt.rcParams["svg.fonttype"] = "none"

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_indigo = "#4F46E5"
    cor_teal = "#0D9488"
    cor_amber = "#D97706"
    cor_rose = "#E11D48"

    fig, axes = plt.subplots(2, 2, figsize=(10.2, 7.6))
    fig.patch.set_alpha(0.0)
    (ax_bin, ax_pois), (ax_exp, ax_norm) = axes

    # 1. PMF Binomial(n = 10, p = 0.3)
    n_sitios = 10
    p_ves = 0.3
    k_bin = np.arange(0, n_sitios + 1)
    pmf_bin = np.array(
        [math.comb(n_sitios, int(k)) * (p_ves**k) * ((1 - p_ves) ** (n_sitios - k)) for k in k_bin]
    )
    ax_bin.bar(k_bin, pmf_bin, width=0.66, color=cor_indigo, alpha=0.85, zorder=3)
    ax_bin.axvline(n_sitios * p_ves, color=cor_texto, linestyle="--", linewidth=1.2, zorder=4)
    ax_bin.text(
        n_sitios * p_ves + 0.25,
        max(pmf_bin) * 0.92,
        "$\\mathbb{E}[X] = 3{,}0$",
        fontsize=9,
        color=cor_texto,
    )
    ax_bin.set_title(
        "Binomial($n = 10;\\; p = 0{,}3$) — Liberação quântica",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_bin.set_xlabel("Vesículas liberadas ($k$)", fontsize=9.5, color=cor_texto)
    ax_bin.set_ylabel("Probabilidade $P(X = k)$", fontsize=9.5, color=cor_texto)
    ax_bin.set_xticks(k_bin)
    ax_bin.set_ylim(0, 0.31)

    # 2. PMF Poisson(lambda = 4)
    lam_spikes = 4.0
    k_pois = np.arange(0, 13)
    pmf_pois = np.array(
        [math.exp(-lam_spikes) * (lam_spikes ** int(k)) / math.factorial(int(k)) for k in k_pois]
    )
    ax_pois.bar(k_pois, pmf_pois, width=0.66, color=cor_teal, alpha=0.85, zorder=3)
    ax_pois.axvline(lam_spikes, color=cor_texto, linestyle="--", linewidth=1.2, zorder=4)
    ax_pois.text(
        lam_spikes + 0.3,
        max(pmf_pois) * 0.92,
        "$\\mathbb{E}[X] = \\lambda = 4$",
        fontsize=9,
        color=cor_texto,
    )
    ax_pois.set_title(
        "Poisson($\\lambda = 4$) — Spikes em 200 ms a 20 Hz",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_pois.set_xlabel("Número de spikes ($k$)", fontsize=9.5, color=cor_texto)
    ax_pois.set_ylabel("Probabilidade $P(X = k)$", fontsize=9.5, color=cor_texto)
    ax_pois.set_xticks(np.arange(0, 13, 2))
    ax_pois.set_ylim(0, 0.24)

    # 3. PDF Exponencial(lambda = 20 Hz -> 0.02 ms^-1, media = 50 ms)
    lam_ms = 0.02
    t_ms = np.linspace(0, 250, 500)
    pdf_exp = lam_ms * np.exp(-lam_ms * t_ms)
    ax_exp.plot(t_ms, pdf_exp, color=cor_amber, linewidth=2.2, zorder=3)
    mask_cauda = t_ms >= 100.0
    ax_exp.fill_between(t_ms[mask_cauda], pdf_exp[mask_cauda], color=cor_amber, alpha=0.25, zorder=2)
    ax_exp.axvline(50.0, color=cor_texto, linestyle="--", linewidth=1.2, zorder=4)
    ax_exp.text(55.0, 0.0165, "Média = 50 ms", fontsize=9, color=cor_texto)
    ax_exp.text(114.0, 0.0042, "$P(\\mathrm{ISI} > 100\\;\\mathrm{ms}) \\approx 0{,}135$", fontsize=8.5, color=cor_texto)
    ax_exp.set_title(
        "Exponencial ($\\lambda = 20$ Hz) — Intervalos entre spikes",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_exp.set_xlabel("Intervalo entre spikes, ISI (ms)", fontsize=9.5, color=cor_texto)
    ax_exp.set_ylabel("Densidade $f(t)$ ($\\mathrm{ms}^{-1}$)", fontsize=9.5, color=cor_texto)
    ax_exp.set_xlim(0, 250)
    ax_exp.set_ylim(0, 0.022)

    # 4. PDF Normal N(-70, 2^2) em mV
    mu_v = -70.0
    sigma_v = 2.0
    v_mv = np.linspace(-77.0, -63.0, 500)
    pdf_norm = (1.0 / (sigma_v * math.sqrt(2.0 * math.pi))) * np.exp(
        -0.5 * ((v_mv - mu_v) / sigma_v) ** 2
    )
    ax_norm.plot(v_mv, pdf_norm, color=cor_rose, linewidth=2.2, zorder=3)
    mask_v = v_mv >= -67.0
    ax_norm.fill_between(v_mv[mask_v], pdf_norm[mask_v], color=cor_rose, alpha=0.25, zorder=2)
    ax_norm.axvline(mu_v, color=cor_texto, linestyle="--", linewidth=1.2, zorder=4)
    ax_norm.text(-69.7, 0.175, "$\\mu = -70$ mV", fontsize=9, color=cor_texto)
    ax_norm.text(-66.6, 0.032, "$P(V > -67) \\approx 0{,}0668$", fontsize=8.5, color=cor_texto)
    ax_norm.set_title(
        "Normal $\\mathcal{N}(-70,\\; 2^2)$ — Ruído no potencial de repouso",
        fontsize=11,
        fontweight="bold",
        color=cor_texto,
        pad=10,
    )
    ax_norm.set_xlabel("Potencial de membrana $V$ (mV)", fontsize=9.5, color=cor_texto)
    ax_norm.set_ylabel("Densidade $f(v)$ ($\\mathrm{mV}^{-1}$)", fontsize=9.5, color=cor_texto)
    ax_norm.set_xlim(-77.0, -63.0)
    ax_norm.set_ylim(0, 0.225)

    for ax in (ax_bin, ax_pois, ax_exp, ax_norm):
        ax.patch.set_alpha(0.0)
        ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade, zorder=0)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=8.5)

    fig.suptitle(
        "Distribuições fundamentais em neurociência computacional",
        fontsize=13,
        fontweight="bold",
        color=cor_texto,
        y=1.01,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "distribuicoes.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
