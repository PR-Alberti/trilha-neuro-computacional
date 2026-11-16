
import torch
import torch.nn as nn

torch.manual_seed(0)
X = torch.randn(16, 40, 12)  # (N=16, T=40, n_x=12)

rnn = nn.RNN(input_size=12, hidden_size=24, batch_first=True)
readout = nn.Linear(24, 2)

out, h_final = rnn(X)
y_hat = readout(out)

print("out:", tuple(out.shape))          # out: (16, 40, 24)
print("h_final:", tuple(h_final.shape))  # h_final: (1, 16, 24)
print("y_hat:", tuple(y_hat.shape))      # y_hat: (16, 40, 2)
          