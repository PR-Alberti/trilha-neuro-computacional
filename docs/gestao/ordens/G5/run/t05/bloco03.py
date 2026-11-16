
import math
import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(0)

n, d_model, h = 4, 6, 2
d_k = d_model // h  # 3 dimensões por cabeça

X = torch.randn(n, d_model)
W_Q = torch.randn(d_model, d_model) * 0.5
W_K = torch.randn(d_model, d_model) * 0.5
W_V = torch.randn(d_model, d_model) * 0.5
W_O = torch.randn(d_model, d_model) * 0.5

# Projeta e separa em h cabeças: formato final (h, n, d_k)
Q = (X @ W_Q).view(n, h, d_k).transpose(0, 1)
K = (X @ W_K).view(n, h, d_k).transpose(0, 1)
V = (X @ W_V).view(n, h, d_k).transpose(0, 1)

scores = (Q @ K.transpose(-2, -1)) / math.sqrt(d_k)  # (h, n, n)

# Máscara causal: True estritamente acima da diagonal principal
mascara = torch.triu(torch.ones(n, n, dtype=torch.bool), diagonal=1)
scores = scores.masked_fill(mascara, float("-inf"))

pesos = F.softmax(scores, dim=-1)
cabecas = pesos @ V  # (h, n, d_k)
saida = cabecas.transpose(0, 1).contiguous().view(n, d_model) @ W_O

print("Pesos de atenção (cabeça 0):\n", torch.round(pesos[0], decimals=3))
# Matriz triangular inferior; todas as entradas acima da diagonal são 0.000
print("Máximo no triângulo superior:", float(pesos[:, mascara].max()))
# 0.0
print("Todas as linhas somam 1?", bool(torch.allclose(pesos.sum(dim=-1), torch.ones(h, n))))
# True

mha = nn.MultiheadAttention(embed_dim=64, num_heads=4, batch_first=True)
total_params = sum(p.numel() for p in mha.parameters())
formula = 4 * (64 ** 2) + 4 * 64
print(f"Parâmetros MultiheadAttention: {total_params} | Fórmula: {formula}")
# Parâmetros MultiheadAttention: 16640 | Fórmula: 16640
      