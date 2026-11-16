import numpy as np

def f(x):
    return x ** 2

a, b = 0.0, 2.0
exato = 8.0 / 3.0

for n in [4, 10, 100, 1000]:
    dx = (b - a) / n
    xs = np.linspace(a, b, n + 1)
    esq = np.sum(f(xs[:-1])) * dx
    dir_ = np.sum(f(xs[1:])) * dx
    mids = 0.5 * (xs[:-1] + xs[1:])
    med = np.sum(f(mids)) * dx
    print(f"n={n:4d} | Esq={esq:.6f} | Dir={dir_:.6f} | Med={med:.6f}")

print(f"Exato = {exato:.6f}")
# Saída esperada:
# n=   4 | Esq=1.750000 | Dir=3.750000 | Med=2.625000
# n=  10 | Esq=2.280000 | Dir=3.080000 | Med=2.660000
# n= 100 | Esq=2.626800 | Dir=2.706800 | Med=2.666600
# n=1000 | Esq=2.662668 | Dir=2.670668 | Med=2.666666
# Exato = 2.666667
