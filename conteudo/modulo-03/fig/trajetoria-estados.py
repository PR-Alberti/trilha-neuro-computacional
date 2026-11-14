from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def trajetoria(t: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    fator = 10.0 * np.exp(-t)
    r1 = 20.0 + fator * np.cos(2.0 * np.pi * t)
    r2 = 20.0 + fator * np.sin(2.0 * np.pi * t)
    return r1, r2


def velocidade(t: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    fator = 10.0 * np.exp(-t)
    c = np.cos(2.0 * np.pi * t)
    s = np.sin(2.0 * np.pi * t)
    dr1 = -fator * (c + 2.0 * np.pi * s)
    dr2 = fator * (2.0 * np.pi * c - s)
    return dr1, dr2


def main() -> None:
    t = np.linspace(0.0, 3.0, 450)
    r1, r2 = trajetoria(t)

    t_setas = np.array([0.0, 0.25, 0.5, 0.75])
    r1_s, r2_s = trajetoria(t_setas)
    v1_s, v2_s = velocidade(t_setas)

    cor_texto = "#475569"
    cor_grade = "#94A3B8"
    cor_n1 = "#4F46E5"
    cor_n2 = "#0D9488"
    cor_vel = "#E11D48"

    fig, (ax_ts, ax_ss) = plt.subplots(1, 2, figsize=(9.8, 4.4))
    fig.patch.set_alpha(0.0)

    # Painel esquerdo: séries temporais r1(t) e r2(t)
    ax_ts.axhline(20.0, color=cor_grade, linestyle=":", linewidth=1.0, alpha=0.8)
    ax_ts.plot(t, r1, color=cor_n1, linewidth=2.1, label="Neurônio 1")
    ax_ts.plot(t, r2, color=cor_n2, linewidth=2.1, linestyle="--", label="Neurônio 2")
    ax_ts.set_title("Séries temporais", fontsize=11.5, fontweight="bold", color=cor_texto, pad=10)
    ax_ts.set_xlabel("Tempo (s)", fontsize=10, color=cor_texto)
    ax_ts.set_ylabel("Taxa de disparo (Hz)", fontsize=10, color=cor_texto)
    ax_ts.set_xlim(0.0, 3.0)
    ax_ts.set_ylim(11.0, 33.0)
    ax_ts.set_xticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
    ax_ts.set_yticks([15, 20, 25, 30])
    ax_ts.legend(frameon=False, fontsize=9, loc="upper right")

    # Painel direito: trajetória no espaço de estados
    ax_ss.plot(r1, r2, color=cor_n1, linewidth=2.1, zorder=3, label="Trajetória $\\mathbf{r}(t)$")
    ax_ss.scatter([30.0], [20.0], color=cor_n1, s=46, zorder=5, label="Início ($t = 0$)")
    ax_ss.scatter([20.0], [20.0], color=cor_n2, marker="X", s=65, zorder=5, label="Ponto fixo $(20, 20)$")
    ax_ss.quiver(
        r1_s,
        r2_s,
        v1_s,
        v2_s,
        angles="xy",
        scale_units="xy",
        scale=16.0,
        color=cor_vel,
        width=0.007,
        headwidth=4.0,
        headlength=5.0,
        zorder=6,
        label="Velocidade $\\mathbf{r}'(t)$ (em escala)",
    )
    ax_ss.annotate(
        "$t = 0$",
        xy=(30.0, 20.0),
        xytext=(30.5, 20.3),
        fontsize=8.5,
        color=cor_texto,
        ha="left",
        va="bottom",
    )
    ax_ss.set_title("Espaço de estados", fontsize=11.5, fontweight="bold", color=cor_texto, pad=10)
    ax_ss.set_xlabel("Taxa do neurônio 1 (Hz)", fontsize=10, color=cor_texto)
    ax_ss.set_ylabel("Taxa do neurônio 2 (Hz)", fontsize=10, color=cor_texto)
    ax_ss.set_xlim(11.0, 33.0)
    ax_ss.set_ylim(11.0, 33.0)
    ax_ss.set_xticks([15, 20, 25, 30])
    ax_ss.set_yticks([15, 20, 25, 30])
    ax_ss.set_aspect("equal")
    ax_ss.legend(frameon=False, fontsize=8.5, loc="lower right")

    for ax in (ax_ts, ax_ss):
        ax.patch.set_alpha(0.0)
        ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35, color=cor_grade)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(cor_grade)
        ax.spines["bottom"].set_color(cor_grade)
        ax.tick_params(colors=cor_texto, labelsize=9)

    fig.suptitle(
        "Oscilação neural amortecida: séries temporais e espaço de estados",
        fontsize=12.5,
        fontweight="bold",
        color=cor_texto,
        y=1.02,
    )
    fig.tight_layout()

    destino = Path(__file__).resolve().parent / "trajetoria-estados.svg"
    fig.savefig(destino, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
