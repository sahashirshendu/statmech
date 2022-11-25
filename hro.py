from pylab import *

k = 1.38e-23
hb = 1.05e-34
n = 6.02e23
w = 1e12
T = linspace(1e-5,50,500)
U1 = zeros(500)
U2 = zeros(500)
C1 = zeros(500)
C2 = zeros(500)

for i in range(500):
    U1[i] = n*k*T[i]
    U2[i] = 0.5*n*hb*w/tanh(hb*w/(2*k*T[i]))
    C1[i] = n*k
    C2[i] = n*k*(hb*w/(k*T[i]))**2*exp(hb*w/(k*T[i]))/(exp(hb*w/(k*T[i]))-1)**2

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
