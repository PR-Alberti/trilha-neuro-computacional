
import torch

# Usamos float64 para alta precisão nas diferenças finitas
x = torch.tensor(1.0, dtype=torch.float64)
y = torch.tensor(1.0, dtype=torch.float64)

w1 = torch.tensor(0.5, dtype=torch.float64, requires_grad=True)
b1 = torch.tensor(0.0, dtype=torch.float64, requires_grad=True)
w2 = torch.tensor(1.0, dtype=torch.float64, requires_grad=True)
b2 = torch.tensor(0.0, dtype=torch.float64, requires_grad=True)


def passo_direto(w1_v, b1_v, w2_v, b2_v):
    z1 = w1_v * x + b1_v
    a1 = torch.sigmoid(z1)
    y_hat = w2_v * a1 + b2_v
    perda = 0.5 * (y_hat - y) ** 2
    return z1, a1, y_hat, perda


z1, a1, y_hat, perda = passo_direto(w1, b1, w2, b2)
perda.backward()

print(f"z1={z1.item():.4f}, a1={a1.item():.4f}, y_hat={y_hat.item():.4f}, loss={perda.item():.4f}")
# z1=0.5000, a1=0.6225, y_hat=0.6225, loss=0.0713
print(f"Autograd -> dL/dw2={w2.grad.item():.4f}, dL/db2={b2.grad.item():.4f}")
# Autograd -> dL/dw2=-0.2350, dL/db2=-0.3775
print(f"Autograd -> dL/dw1={w1.grad.item():.4f}, dL/db1={b1.grad.item():.4f}")
# Autograd -> dL/dw1=-0.0887, dL/db1=-0.0887

eps = 1e-5
with torch.no_grad():
    _, _, _, p_mais = passo_direto(w1 + eps, b1, w2, b2)
    _, _, _, p_menos = passo_direto(w1 - eps, b1, w2, b2)
    grad_num = (p_mais - p_menos) / (2 * eps)
print(f"Diferenças finitas dL/dw1={grad_num.item():.4f}")
# Diferenças finitas dL/dw1=-0.0887

eta = 0.5
with torch.no_grad():
    w1 -= eta * w1.grad
    b1 -= eta * b1.grad
    w2 -= eta * w2.grad
    b2 -= eta * b2.grad
print(f"Atualizados -> w1={w1.item():.4f}, b1={b1.item():.4f}, w2={w2.item():.4f}, b2={b2.item():.4f}")
# Atualizados -> w1=0.5444, b1=0.0444, w2=1.1175, b2=0.1888
      