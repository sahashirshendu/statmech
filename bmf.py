import numpy as np
import matplotlib.pyplot as plt

E = np.linspace(-0.5, 0.5, 1001)  # energy
u = 0  # chemeical potential is taken to be 0
e = 1.602e-19 # charge of electron
k = 1.381e-23 # Boltzmann Constant


def f(T, a):
    return 1 / (np.exp(((E - u) * e) / (k * T)) + a)


plt.plot(E, f(100, -1), label="100 K")
plt.plot(E, f(250, -1), label="250 K")
plt.plot(E, f(500, -1), label="500 K")
plt.ylim(0, 2)
plt.title("Bose-Einstein Distribution")
plt.xlabel("$E \\ (eV)$")
plt.ylabel("$f(E)$")
plt.legend()
plt.show()

plt.plot(E, f(100, 0), label="100 K")
plt.plot(E, f(250, 0), label="250 K")
plt.plot(E, f(500, 0), label="500 K")
plt.ylim(0, 3)
plt.title("Maxwell-Boltzmann Distribution")
plt.xlabel("$E \\ (eV)$")
plt.ylabel("$f(E)$")
plt.legend()
plt.show()

plt.plot(E, f(100, +1), label="100 K")
plt.plot(E, f(250, +1), label="250 K")
plt.plot(E, f(500, +1), label="500 K")
plt.ylim(0, 1)
plt.title("Fermi-Dirac Distribution")
plt.xlabel("$E \\ (eV)$")
plt.ylabel("$f(E)$")
plt.legend()
plt.show()
