from pylab import *
from scipy.optimize import curve_fit

n=1
e=1.6e-19
k=1.38e-23
na=6.02e23

data=loadtxt('specific_heat1.txt')
data=data[data[:,0].argsort()]
T=data[:,0]**0.5
cv=data[:,1]*T

def cved(T,tf,td):
    gamma = pi ** 2 * n * na * k / (2 * tf)
    alpha = 12 * pi ** 4 * n * na * k / (5 * td ** 3)
    return gamma * T + alpha * T ** 3


popt, pcov = curve_fit(cved, T, cv)
TF, TD = popt[0], popt[1]
dTF = sqrt(pcov[0, 0])
dTD = sqrt(pcov[1, 1])
print("Debye Temperature = ( {TD:.5} ± {dTD:.3} ) K")
print("Fermi Temperature = ( {TF:.5} ± {dTF:.3} ) K")
print("Fermi Energy =", k * TF, "J")

plot(T, cv, ".", label="Data")
plot(T, cved(T, TF, TD), label="Fitted Plot")
xlabel("$T$")
ylabel("$C_V(T)")
legend()
tight_layout(pad = 2)
show()
