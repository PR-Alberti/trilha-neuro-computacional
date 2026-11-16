
import numpy as np

# Grade espacial 21x21 centrada na origem
eixo = np.arange(-10, 11, dtype=np.float64)
x, y = np.meshgrid(eixo, eixo)

# Filtro de Gabor sintonizado para barras verticais (theta = 0 rad)
lambd, sigma, psi = 6.0, 3.0, 0.0
gabor = np.exp(-(x**2 + y**2) / (2.0 * sigma**2)) * np.cos(2.0 * np.pi * x / lambd + psi)
gabor -= gabor.mean()  # média zero: fundo uniforme claro ou escuro gera resposta nula

angulos = list(range(0, 180, 15))
respostas = []
for ang in angulos:
    rad = np.deg2rad(ang)
    # Barra centrada de largura ~2 pixels inclinada segundo o ângulo
    dist = np.abs(x * np.cos(rad) + y * np.sin(rad))
    barra = (dist <= 1.0).astype(np.float64)
    # Produto interno seguido de retificação (como taxa de disparo >= 0)
    resp = max(0.0, float(np.sum(gabor * barra)))
    respostas.append(resp)

pico = max(respostas)
print("Curva de sintonia de orientação (célula simples simulada):")
for ang, r in zip(angulos, respostas):
    r_norm = r / pico
    traco = "#" * int(round(20 * r_norm))
    print(f"{ang:3d}° | resp = {r_norm:.2f} | {traco}")

# Saída esperada (pico em 0° e queda para valores baixos <= 0.13 longe da orientação preferida):
#   0° | resp = 1.00 | ####################
#  15° | resp = 0.61 | ############
#  30° | resp = 0.33 | #######
#  45° | resp = 0.08 | ##
#  60° | resp = 0.09 | ##
#  75° | resp = 0.07 | #
#  90° | resp = 0.13 | ###
# 105° | resp = 0.07 | #
# 120° | resp = 0.04 | #
# 135° | resp = 0.08 | ##
# 150° | resp = 0.33 | #######
# 165° | resp = 0.61 | ############
      