import numpy as np

def f(x):
    return x ** 2

a = 2.0
derivada_exata = 2 * a
hs = np.array([0.1, 0.01, 0.001])

for h in hs:
    razao = (f(a + h) - f(a)) / h
    erro = abs(razao - derivada_exata)
    print(f"h = {h:.3f} | razao = {razao:.6f} | erro = {erro:.6f}")

# Saída esperada:
# h = 0.100 | razao = 4.100000 | erro = 0.100000
# h = 0.010 | razao = 4.010000 | erro = 0.010000
# h = 0.001 | razao = 4.001000 | erro = 0.001000
