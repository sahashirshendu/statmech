from pylab import *

k = 1
N = 1000
T = linspace(0.01,20,N)
ev1 = [1,6]
ev2 = [2,7]

def E(ep, T):
    sum = 0
    s = 0
    for i in range(len(ep)):
        s = s+exp(-ep[i]/(k*T))
        sum = sum+ep[i]*exp(-ep[i]/(k*T))
    return sum*N/s

e1 = zeros(N)
e2 = zeros(N)
for i in range(N):
    e1[i] = E(ev1,T[i])
    e2[i] = E(ev2,T[i])

c1 = zeros(N)
c2 = zeros(N)
h = 19.99 / (N-1)
for i in range(N-1):
    c1[i] = (e1[i+1]-e1[i]) / h
    c2[i] = (e2[i+1]-e2[i]) / h

plot(T,e1)
plot(T,e2)
xlabel('T')
ylabel('E')
show()
plot(T,c1)
plot(T,c2,'--')
xlabel('T')
ylabel('C')
show()
