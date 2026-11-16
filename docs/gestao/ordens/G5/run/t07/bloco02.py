
import torch
import torch.nn as nn

torch.manual_seed(0)

G = nn.Sequential(
    nn.Linear(1, 32),
    nn.LeakyReLU(0.2),
    nn.Linear(32, 32),
    nn.LeakyReLU(0.2),
    nn.Linear(32, 1),
)
D = nn.Sequential(
    nn.Linear(1, 32),
    nn.LeakyReLU(0.2),
    nn.Linear(32, 32),
    nn.LeakyReLU(0.2),
    nn.Linear(32, 1),
)

opt_G = torch.optim.Adam(G.parameters(), lr=1e-3, betas=(0.5, 0.999))
opt_D = torch.optim.Adam(D.parameters(), lr=1e-3, betas=(0.5, 0.999))
bce = nn.BCEWithLogitsLoss()

for passo in range(4000):
    # 1) Atualiza D: reais -> 1, falsos -> 0
    x_real = 4.0 + 1.25 * torch.randn(128, 1)
    x_falso = G(torch.randn(128, 1)).detach()
    perda_D = bce(D(x_real), torch.ones(128, 1)) + bce(D(x_falso), torch.zeros(128, 1))
    opt_D.zero_grad()
    perda_D.backward()
    opt_D.step()

    # 2) Atualiza G (perda nao saturante: maximizar log D(G(z)))
    z = torch.randn(128, 1)
    perda_G = bce(D(G(z)), torch.ones(128, 1))
    opt_G.zero_grad()
    perda_G.backward()
    opt_G.step()

with torch.no_grad():
    amostras = G(torch.randn(5000, 1)).squeeze()

# Valores aproximados; podem variar levemente entre versoes e maquinas
print(f"Media gerada ≈ {amostras.mean():.2f} (alvo: 4.00)")
print(f"Desvio gerado ≈ {amostras.std():.2f} (alvo: 1.25)")
# Media gerada ≈ 3.98 (alvo: 4.00)
# Desvio gerado ≈ 1.24 (alvo: 1.25)
      