import torch; torch.set_num_threads(2)

import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(0)

T = 50
betas = torch.linspace(1e-3, 0.2, T)
alphas = 1.0 - betas
alpha_bar = torch.cumprod(alphas, dim=0)


def amostrar_dados(n):
    modos = torch.randint(0, 2, (n, 1)).float() * 4.0 - 2.0  # -2.0 ou +2.0
    return modos + 0.3 * torch.randn(n, 1)


eps_theta = nn.Sequential(
    nn.Linear(2, 64),
    nn.SiLU(),
    nn.Linear(64, 64),
    nn.SiLU(),
    nn.Linear(64, 64),
    nn.SiLU(),
    nn.Linear(64, 1),
)
opt = torch.optim.Adam(eps_theta.parameters(), lr=2e-3)

for passo in range(2500):
    x0 = amostrar_dados(256)
    t_idx = torch.randint(0, T, (256,))
    ab = alpha_bar[t_idx].unsqueeze(1)
    eps = torch.randn_like(x0)
    x_t = torch.sqrt(ab) * x0 + torch.sqrt(1.0 - ab) * eps
    t_norm = (t_idx.float().unsqueeze(1) + 1.0) / T
    perda = F.mse_loss(eps_theta(torch.cat([x_t, t_norm], dim=1)), eps)
    opt.zero_grad()
    perda.backward()
    opt.step()

with torch.no_grad():
    x = torch.randn(2000, 1)
    for t_idx in reversed(range(T)):
        t_norm = torch.full((2000, 1), (t_idx + 1) / T)
        eps_pred = eps_theta(torch.cat([x, t_norm], dim=1))
        a_t, ab_t, b_t = alphas[t_idx], alpha_bar[t_idx], betas[t_idx]
        media = (x - (b_t / torch.sqrt(1.0 - ab_t)) * eps_pred) / torch.sqrt(a_t)
        x = media + torch.sqrt(b_t) * torch.randn_like(x) if t_idx > 0 else media

x = x.squeeze()
esq, dir_ = x[x < 0], x[x >= 0]
# Valores aproximados; podem variar levemente entre versoes e maquinas
print(f"Fracao esq ≈ {len(esq)/len(x):.2f} | media ≈ {esq.mean():.2f}, desvio ≈ {esq.std():.2f}")
print(f"Fracao dir ≈ {len(dir_)/len(x):.2f} | media ≈ {dir_.mean():.2f}, desvio ≈ {dir_.std():.2f}")
# Fracao esq ≈ 0.50 | media ≈ -1.99, desvio ≈ 0.32
# Fracao dir ≈ 0.50 | media ≈ 2.01, desvio ≈ 0.31
      