
import torch
import torch.nn as nn

for w in (0.5, 1.5):
    rnn = nn.RNN(input_size=1, hidden_size=1, bias=False, batch_first=True)
    with torch.no_grad():
        rnn.weight_hh_l0.fill_(w)
        rnn.weight_ih_l0.fill_(0.0)

    # h0 muito pequeno mantém 1 - h_t^2 ≈ 1, isolando o efeito de w^20
    x = torch.zeros(1, 20, 1)
    h0 = torch.tensor([[[1e-7]]], requires_grad=True)
    _, h_final = rnn(x, h0)
    h_final.squeeze().backward()

    grad_medido = h0.grad.item()
    print(f"w = {w:.1f} | dh_20/dh_0 = {grad_medido:.4e} | w^20 = {w**20:.4e}")
# w = 0.5 | dh_20/dh_0 = 9.5367e-07 | w^20 = 9.5367e-07
# w = 1.5 | dh_20/dh_0 = 3.3253e+03 | w^20 = 3.3253e+03

# Demonstracao de clip_grad_norm_ sobre um parametro com gradiente grande
param = nn.Parameter(torch.zeros(3))
param.grad = torch.tensor([3.0, -4.0, 12.0])
norma_antes = torch.nn.utils.clip_grad_norm_([param], max_norm=2.6)
print("Norma antes:", round(norma_antes.item(), 2))   # Norma antes: 13.0
print("Gradiente cortado:", [round(v, 4) for v in param.grad.tolist()])  # Gradiente cortado: [0.6, -0.8, 2.4]
      