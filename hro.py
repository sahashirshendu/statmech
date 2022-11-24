from pylab import *

k = 1.38e-23
hb = 1.05e-34

def UC(N,w,T):
    return N*k*T

def CC(N,w,T):
    return N*k

def UQ(N,w,T):
    return 0.5*N*hb*w/tanh(hb*w/(2*k*T))

def CQ(N, w, T):
    return N*k*(hb*w/(k*T))**2*exp(hb*w/(k*T))/(exp(hb*w/(k*T))-1)**2

N = 100
w = 1e12
T = linspace(1e-5,50,500)
U1 = zeros(500)
U2 = zeros(500)
C1 = zeros(500)
C2 = zeros(500)

for i in range(500):
    U1[i] = UC(N,w,T[i])
    U2[i] = UQ(N,w,T[i])
    C1[i] = CC(N,w,T[i])
    C2[i] = CQ(N,w,T[i])

plot(T,U1,label='Classical')
plot(T,U2,label='Quantum')
xlabel('T')
ylabel('U(T)')
legend()
show()

plot(T, C1, label='Classical')
plot(T, C2, label='Quantum')
xlabel('T')
ylabel('C(T)')
legend()
show()
