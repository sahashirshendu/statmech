from pylab import *

k = 1
N = 1000
T = linspace(0.01, 20, N)
ep = [1, 6]

def E(ep, T):
    sum = 0
    mup = 0
    for i in range(len(ep)):
        sum = sum + ep[i] * exp(- ep[i] / (k * T))
        mup = mup + exp(- ep[i] / (k * T))
    return sum * N / mup

EN = np.zeros(N)
for i in range(N):
    EN[i] = E(ep, T[i])

C = np.zeros(N)
h = 19.99 / (N - 1)
for i in range(N - 1):
    C[i] = (EN[i + 1] - EN[i]) / h

plot(T, EN)
plot(T, C)
show()
