
import torch
import torch.nn as nn

# 1) Conferindo contagem de parametros no PyTorch (dois vieses por portao)
n_x, n_h = 10, 20
for nome, camada, fator in [
    ("RNN", nn.RNN(n_x, n_h, batch_first=True), 1),
    ("GRU", nn.GRU(n_x, n_h, batch_first=True), 3),
    ("LSTM", nn.LSTM(n_x, n_h, batch_first=True), 4),
]:
    total_pytorch = sum(p.numel() for p in camada.parameters())
    formula = fator * (n_h * n_x + n_h * n_h + 2 * n_h)
    print(f"{nome:4s} | PyTorch = {total_pytorch:4d} | Formula = {formula:4d}")
# RNN  | PyTorch =  640 | Formula =  640
# GRU  | PyTorch = 1920 | Formula = 1920
# LSTM | PyTorch = 2560 | Formula = 2560

# 2) Conferindo o Exemplo 1 (ordem dos portoes no PyTorch: i, f, g, o)
lstm = nn.LSTM(input_size=1, hidden_size=1, batch_first=True)
with torch.no_grad():
    lstm.weight_ih_l0.copy_(torch.tensor([[1.0], [0.0], [0.5], [0.0]]))
    lstm.weight_hh_l0.zero_()
    lstm.bias_ih_l0.copy_(torch.tensor([-1.0, 2.0, 0.0, 1.0]))
    lstm.bias_hh_l0.zero_()

x = torch.tensor([[[1.0]]])   # (N=1, T=1, n_x=1)
h0 = torch.tensor([[[0.0]]])  # (1, N=1, n_h=1)
c0 = torch.tensor([[[1.0]]])

_, (h1, c1) = lstm(x, (h0, c0))
print(f"c1 = {c1.item():.4f}, h1 = {h1.item():.4f}")
# c1 = 1.1119, h1 = 0.5883
      