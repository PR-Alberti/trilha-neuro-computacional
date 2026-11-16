
import numpy as np

gamma = 0.5
V = np.zeros(2)
for _ in range(20):
    V = np.array([0.0 + gamma * V[1], 1.0 + gamma * V[0]])
print(f"V(s0)={V[0]:.4f}, V(s1)={V[1]:.4f}")  # V(s0)=0.6667, V(s1)=1.3333
          