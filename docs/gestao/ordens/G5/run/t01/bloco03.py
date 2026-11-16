
import numpy as np
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset

digitos = load_digits()
X = digitos.data.astype(np.float32) / 16.0
y = digitos.target.astype(np.int64)

X_tr_full, X_te, y_tr_full, y_te = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)
X_tr, X_val, y_tr, y_val = train_test_split(X_tr_full, y_tr_full, test_size=0.2, random_state=0, stratify=y_tr_full)

ds_tr = TensorDataset(torch.from_numpy(X_tr), torch.from_numpy(y_tr))
X_val_t, y_val_t = torch.from_numpy(X_val), torch.from_numpy(y_val)
X_te_t, y_te_t = torch.from_numpy(X_te), torch.from_numpy(y_te)


def treinar(wd):
    torch.manual_seed(0)
    loader = DataLoader(ds_tr, batch_size=64, shuffle=True)
    modelo = nn.Sequential(nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 10))
    criterio = nn.CrossEntropyLoss()
    opt = torch.optim.Adam(modelo.parameters(), lr=0.01, weight_decay=wd)

    melhor_val = float("inf")
    melhor_estado = None
    sem_melhora = 0

    for epoca in range(1, 101):
        modelo.train()
        for xb, yb in loader:
            opt.zero_grad()
            perda = criterio(modelo(xb), yb)
            perda.backward()
            opt.step()

        modelo.eval()
        with torch.no_grad():
            perda_val = criterio(modelo(X_val_t), y_val_t).item()
        if perda_val < melhor_val - 1e-4:
            melhor_val = perda_val
            melhor_estado = {k: v.clone() for k, v in modelo.state_dict().items()}
            sem_melhora = 0
        else:
            sem_melhora += 1
            if sem_melhora >= 5:
                break

    modelo.load_state_dict(melhor_estado)
    modelo.eval()
    with torch.no_grad():
        acc_te = (modelo(X_te_t).argmax(dim=1) == y_te_t).float().mean().item()
        norma_l2 = sum(p.pow(2).sum().item() for p in modelo.parameters()) ** 0.5
    return epoca, acc_te, norma_l2


for wd in (0.0, 1e-2):
    ep, acc, norma = treinar(wd)
    print(f"weight_decay={wd:.2f} | parou época {ep:2d} | acc teste={acc:.3f} | norma L2={norma:.2f}")

# Saída esperada aproximada (varia conforme versão/máquina):
# weight_decay=0.00 | parou época ≈ 25 | acc teste ≈ 0.96 | norma L2 ≈ 12.0
# weight_decay=0.01 | parou época ≈ 30 | acc teste ≈ 0.96 | norma L2 ≈ 7.0
          