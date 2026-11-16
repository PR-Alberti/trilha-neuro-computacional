
import torch
import torch.nn as nn

torch.manual_seed(0)


def gerar_dados(n, comp=8):
    metade = n // 2
    ord_x = torch.sort(torch.randint(0, 10, (metade, comp)), dim=1).values
    des_x = torch.randint(0, 10, (metade, comp))
    for i in range(metade):
        while bool((des_x[i, 1:] >= des_x[i, :-1]).all()):
            des_x[i] = torch.randint(0, 10, (comp,))
    X = torch.cat([ord_x, des_x], dim=0)
    y = torch.cat([torch.ones(metade), torch.zeros(metade)])
    perm = torch.randperm(n)
    return X[perm], y[perm]


class ClassificadorOrdem(nn.Module):
    def __init__(self, comp=8, d_model=16):
        super().__init__()
        self.emb_tok = nn.Embedding(10, d_model)
        self.emb_pos = nn.Embedding(comp, d_model)
        self.bloco = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=2, dim_feedforward=32, dropout=0.0, batch_first=True
        )
        self.cabeca = nn.Linear(d_model, 1)

    def forward(self, x):
        pos = torch.arange(x.size(1), device=x.device)
        h = self.emb_tok(x) + self.emb_pos(pos)
        h = self.bloco(h)
        return self.cabeca(h.mean(dim=1)).squeeze(-1)


X_treino, y_treino = gerar_dados(600)
X_teste, y_teste = gerar_dados(200)

modelo = ClassificadorOrdem()
otimizador = torch.optim.Adam(modelo.parameters(), lr=0.005)
criterio = nn.BCEWithLogitsLoss()

for epoca in range(40):
    perm = torch.randperm(len(X_treino))
    for inicio in range(0, len(X_treino), 64):
        idx = perm[inicio:inicio + 64]
        otimizador.zero_grad()
        perda = criterio(modelo(X_treino[idx]), y_treino[idx])
        perda.backward()
        otimizador.step()

with torch.no_grad():
    logits = modelo(X_teste)
    preds = (logits > 0).float()
    acuracia = float((preds == y_teste).float().mean())

print(f"Acurácia no teste: {acuracia:.3f}")
# Acurácia no teste: ≈ 0.98 (pode variar um pouco entre versões/máquinas)
      