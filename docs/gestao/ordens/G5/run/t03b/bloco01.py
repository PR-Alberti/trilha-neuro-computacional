
import torch
import torch.nn as nn

# RNN escalar (entrada=1, oculto=1) sem vies para conferir o Exemplo 1
rnn = nn.RNN(input_size=1, hidden_size=1, bias=False, batch_first=True)
readout = nn.Linear(in_features=1, out_features=1, bias=True)

with torch.no_grad():
    rnn.weight_hh_l0.fill_(0.5)
    rnn.weight_ih_l0.fill_(0.5)
    readout.weight.fill_(2.0)
    readout.bias.fill_(-0.1)

# Tensor de entrada no formato (N=1 lote, T=3 passos, n_x=1 feature)
x = torch.tensor([[[1.0], [0.4], [-0.8]]])
h0 = torch.zeros(1, 1, 1)  # (num_camadas=1, N=1, n_h=1)

out, h_final = rnn(x, h0)
y_hat = readout(out)

print("Forma de x:", tuple(x.shape))        # Forma de x: (1, 3, 1)
print("Forma de out:", tuple(out.shape))    # Forma de out: (1, 3, 1)
print("Forma de h_final:", tuple(h_final.shape))  # Forma de h_final: (1, 1, 1)
print("Estados h_t:", [round(v, 4) for v in out.squeeze().tolist()])
# Estados h_t: [0.4621, 0.4062, -0.1944]
print("Saidas y_hat:", [round(v, 4) for v in y_hat.squeeze().tolist()])
# Saidas y_hat: [0.8242, 0.7124, -0.4888]
      