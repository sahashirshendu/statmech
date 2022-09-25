import numpy as np
import matplotlib.pyplot as plt

k = 1
N = 1000
T = np.linspace(0.01, 20, N)
ep = [1, 6]

def mkt(ep, T):
    sum = 0
    for i in range(len(ep)):
        sum += np.exp(- ep[i] / (k * T))
    return sum

def E(ep, T):
    sum = 0
    for i in range(len(ep)):
        sum += ep[i] * np.exp(- ep[i] / (k * T))
    return sum * N / mkt(ep, T)

EN = np.zeros(N)
for i in range(N):
    EN[i] = E(ep, T[i])

C = np.zeros(N)
h = 19.99 / (N - 1)
for i in range(N - 1):
    C[i] = (EN[i + 1] - EN[i]) / h

plt.plot(T, EN)
plt.plot(T, C)
plt.show()
