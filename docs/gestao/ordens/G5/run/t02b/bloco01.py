
import numpy as np
import torch
import torch.nn.functional as F


def conv2d_valida(imagem: np.ndarray, filtro: np.ndarray) -> np.ndarray:
    """Correlação cruzada 2D válida (padding=0, stride=1) em NumPy."""
    h_in, w_in = imagem.shape
    kh, kw = filtro.shape
    h_out = h_in - kh + 1
    w_out = w_in - kw + 1
    saida = np.zeros((h_out, w_out), dtype=np.float32)
    for i in range(h_out):
        for j in range(w_out):
            janela = imagem[i : i + kh, j : j + kw]
            saida[i, j] = np.sum(janela * filtro)
    return saida


# 1. Conferindo o Exemplo 2 (imagem 5x5 e detector de borda vertical 3x3)
X = np.array(
    [
        [0, 0, 4, 4, 0],
        [0, 0, 4, 4, 0],
        [0, 0, 4, 4, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ],
    dtype=np.float32,
)

W = np.array(
    [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1],
    ],
    dtype=np.float32,
)

saida_np = conv2d_valida(X, W)

# Em PyTorch, os tensores têm formato (lote, canais, altura, largura)
X_t = torch.from_numpy(X).unsqueeze(0).unsqueeze(0)
W_t = torch.from_numpy(W).unsqueeze(0).unsqueeze(0)
saida_torch = F.conv2d(X_t, W_t, padding=0, stride=1).squeeze().numpy()

print("Saída NumPy:\n", saida_np)
# [[ 12.  12. -12.]
#  [  8.   8.  -8.]
#  [  4.   4.  -4.]]
print("Igual ao PyTorch?", np.allclose(saida_np, saida_torch))  # True

# 2. Provando que F.conv2d faz correlação cruzada (sem espelhar filtro assimétrico)
W_assim = np.array(
    [
        [1, 2, 0],
        [0, -1, 1],
        [2, 0, -1],
    ],
    dtype=np.float32,
)
W_assim_t = torch.from_numpy(W_assim).unsqueeze(0).unsqueeze(0)
torch_assim = F.conv2d(X_t, W_assim_t, padding=0, stride=1).squeeze().numpy()

print("Igual à correlação cruzada?", np.allclose(torch_assim, conv2d_valida(X, W_assim)))  # True
print("Igual à convolução espelhada?", np.allclose(torch_assim, conv2d_valida(X, np.flip(W_assim))))  # False
      