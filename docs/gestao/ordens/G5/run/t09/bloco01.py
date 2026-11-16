
import numpy as np

gamma = 0.9
V = np.zeros(3)  # índices: 0 = A, 1 = B, 2 = C (terminal)

for it in range(1, 5):
    V_novo = np.zeros(3)
    V_novo[0] = 0.0 + gamma * V[1]  # A -> B, r = 0
    V_novo[1] = 1.0 + gamma * V[2]  # B -> C, r = 1
    V_novo[2] = 0.0                 # C terminal
    V = V_novo
    print(f"Iteração {it}: V(A)={V[0]:.2f}, V(B)={V[1]:.2f}, V(C)={V[2]:.2f}")

# Iteração 1: V(A)=0.00, V(B)=1.00, V(C)=0.00
# Iteração 2: V(A)=0.90, V(B)=1.00, V(C)=0.00
# Iteração 3: V(A)=0.90, V(B)=1.00, V(C)=0.00
# Iteração 4: V(A)=0.90, V(B)=1.00, V(C)=0.00
      