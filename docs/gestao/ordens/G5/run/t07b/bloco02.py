
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

opt_G = torch.optim.Adam(G.parameters(), lr=5e-4, betas=(0.5, 0.999))
opt_D = torch.optim.Adam(D.parameters(), lr=5e-4, betas=(0.5, 0.999))
bce = nn.BCEWithLogitsLoss()

for passo in range(3000):
    # 1) Atualiza D: reais -> 1, falsos -> 0
    x_real = 4.0 + 1.25 * torch.randn(256, 1)
    x_falso = G(torch.randn(256, 1)).detach()
    perda_D = bce(D(x_real), torch.ones(256, 1)) + bce(D(x_falso), torch.zeros(256, 1))
    opt_D.zero_grad()
    perda_D.backward()
    opt_D.step()

    # 2) Atualiza G (perda nao saturante: maximizar log D(G(z)))
    z = torch.randn(256, 1)
    perda_G = bce(D(G(z)), torch.ones(256, 1))
    opt_G.zero_grad()
    perda_G.backward()
    opt_G.step()

with torch.no_grad():
    amostras = G(torch.randn(10000, 1)).squeeze()

print(f"Media gerada ≈ {amostras.mean():.2f} (alvo: 4.00)")
print(f"Desvio gerado ≈ {amostras.std():.2f} (alvo: 1.25)")
# Média gerada ≈ 4 (alvo 4,00); desvio entre ≈ 1,0 e ≈ 1,6 (alvo 1,25) — o resultado de uma GAN varia de execução para execução
      