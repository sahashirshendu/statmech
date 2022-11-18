from pylab import *
from scipy.optimize import curve_fit

n=1
k=1.38e-23
na=6.02e23

data=loadtxt('specific_heat1.txt')
T=data[:,0]**0.5
cv=data[:,1]*T

def cvf(T,tf,td):
    return pi**2*n*na*k/(2*tf)*T+12*pi**4*n*na*k/(5*td**3)*T**3

param,_=curve_fit(cvf,T,cv)
tf=param[0]
td=param[1]
print("Debye Temperature =",td,"K")
print("Fermi Temperature =",tf,"K")
print("Fermi Energy =",k*tf,"J")

plot(T,cv,'.',label='Data')
plot(T,cvf(T,tf,td),label='Fitted Plot')
xlabel("$T$")
ylabel("$C_V(T)$")
legend()
show()
