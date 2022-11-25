import numpy as np
import matplotlib.pyplot as plt

def f1(n):
    sum = 0
    for i in range(1, n + 1):
        sum += np.log(float(i))
    return sum

def f2(n):
    return n * np.log(float(n)) - n

N = np.arange(1, 201, 1)
F1 = np.zeros(len(N))
F2 = np.zeros(len(N))
for i in range(len(N)):
    F1[i] = f1(N[i])
    F2[i] = f2(N[i])

plt.plot(N, F1, label='ln(N!)')
plt.plot(N, F2, label='Nln(N)-N')
plt.xlabel('N')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
