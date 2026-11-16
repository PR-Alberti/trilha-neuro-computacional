
import torch
import torch.nn as nn

emb = nn.Embedding(num_embeddings=4, embedding_dim=3)
E = torch.tensor([
    [ 0.8,  0.6,  0.1],
    [ 0.7,  0.7,  0.2],
    [-0.5,  0.2,  0.9],
    [-0.4,  0.1,  0.8],
])
with torch.no_grad():
    emb.weight.copy_(E)

idx = torch.tensor([1])  # índice 1 (dendrito) em base zero
e_lookup = emb(idx)
one_hot = torch.tensor([[0.0, 1.0, 0.0, 0.0]])
e_matmul = one_hot @ emb.weight

print("Via nn.Embedding:", e_lookup.detach().numpy())  # [[0.7 0.7 0.2]]
print("Via one-hot @ E: ", e_matmul.detach().numpy())  # [[0.7 0.7 0.2]]
print("Diferenca maxima:", torch.max(torch.abs(e_lookup - e_matmul)).item())  # 0.0
      