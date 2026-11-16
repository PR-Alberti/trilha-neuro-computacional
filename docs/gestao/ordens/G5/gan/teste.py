import sys, time, torch, torch.nn as nn
torch.set_num_threads(1)
lr, passos, zd, seed = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
torch.manual_seed(seed)
mk = lambda i: nn.Sequential(nn.Linear(i,32), nn.LeakyReLU(0.2), nn.Linear(32,32), nn.LeakyReLU(0.2), nn.Linear(32,1))
G, D = mk(zd), mk(1)
oG = torch.optim.Adam(G.parameters(), lr=lr, betas=(0.5,0.999)); oD = torch.optim.Adam(D.parameters(), lr=lr, betas=(0.5,0.999))
bce = nn.BCEWithLogitsLoss(); t0=time.time()
for p in range(passos):
    xr = 4.0 + 1.25*torch.randn(256,1); xf = G(torch.randn(256,zd)).detach()
    lD = bce(D(xr), torch.ones(256,1)) + bce(D(xf), torch.zeros(256,1)); oD.zero_grad(); lD.backward(); oD.step()
    lG = bce(D(G(torch.randn(256,zd))), torch.ones(256,1)); oG.zero_grad(); lG.backward(); oG.step()
with torch.no_grad(): a = G(torch.randn(10000,zd)).squeeze()
print(f"lr={lr} passos={passos} zd={zd} seed={seed}: media={a.mean():.2f} desvio={a.std():.2f} t={time.time()-t0:.0f}s")
