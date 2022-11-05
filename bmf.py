from pylab import *

E = linspace(-0.5,0.5,1001)
u = 0  # chemeical potential is taken to be 0
e = 1.6e-19
k = 1.38e-23

def f(T, a):
    return 1 / (exp(((E - u) * e) / (k * T)) + a)

plot(E, f(100, -1), label="100 K")
plot(E, f(250, -1), label="250 K")
plot(E, f(500, -1), label="500 K")
ylim(0, 2)
title("Bose-Einstein Distribution")
xlabel("$E \\ (eV)$")
ylabel("$f(E)$")
legend()
show()

plot(E, f(100, 0), label="100 K")
plot(E, f(250, 0), label="250 K")
plot(E, f(500, 0), label="500 K")
ylim(0, 3)
title("Maxwell-Boltzmann Distribution")
xlabel("$E \\ (eV)$")
ylabel("$f(E)$")
legend()
show()

plot(E, f(100, +1), label="100 K")
plot(E, f(250, +1), label="250 K")
plot(E, f(500, +1), label="500 K")
ylim(0, 1)
title("Fermi-Dirac Distribution")
xlabel("$E \\ (eV)$")
ylabel("$f(E)$")
legend()
show()
