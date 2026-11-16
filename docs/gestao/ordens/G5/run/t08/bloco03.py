
import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(0)

texto = (
    "o neuronio dispara sinais eletricos pelo axonio. "
    "sinapses conectam neuronios no cortex cerebral. "
) * 20

chars = sorted(set(texto))
V = len(chars)  # V = 18 caracteres
c2i = {c: i for i, c in enumerate(chars)}
i2c = {i: c for i, c in enumerate(chars)}

dados = torch.tensor([c2i[c] for c in texto], dtype=torch.long)
x_tr, y_tr = dados[:-1], dados[1:]

modelo = nn.Embedding(V, V)
nn.init.zeros_(modelo.weight)  # Começa uniforme: perda = ln(V), PPL = V
otim = torch.optim.Adam(modelo.parameters(), lr=0.1)

with torch.no_grad():
    p0 = F.cross_entropy(modelo(x_tr), y_tr)
print(f"Inicial -> perda: {p0.item():.2f} (ln V = {torch.log(torch.tensor(float(V))):.2f}), PPL: {torch.exp(p0):.2f}")

for _ in range(300):
    perda = F.cross_entropy(modelo(x_tr), y_tr)
    otim.zero_grad()
    perda.backward()
    otim.step()

print(f"Final   -> perda ≈ {perda.item():.2f}, PPL ≈ {torch.exp(perda):.2f}")

# Amostragem com temperatura tau = 0.8 (a saída pode variar entre versões/máquinas)
idx = torch.tensor([c2i["n"]])
gerado = ["n"]
tau = 0.8
with torch.no_grad():
    for _ in range(45):
        probs = F.softmax(modelo(idx[-1]) / tau, dim=-1)
        prox = torch.multinomial(probs, num_samples=1)
        gerado.append(i2c[prox.item()])
        idx = torch.cat([idx, prox])

print("Amostra:", "".join(gerado))
# Saída esperada:
# Inicial -> perda: 2.89 (ln V = 2.89), PPL: 18.00
# Final   -> perda ≈ 1.24, PPL ≈ 3.45 (valores aproximados; podem variar entre versões)
# Amostra: trecho curto no estilo do texto de treino (pode variar entre versões)
      