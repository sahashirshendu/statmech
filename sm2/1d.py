from pylab import *
from scipy.optimize import curve_fit

n=1
k=1.38e-23
na=6.02e23

data=loadtxt('specific_heat.txt',delimiter=',')
data=data[data[:,0].argsort()]
T=data[:,0]**(1/3)
cv=data[:,1]

def cvl(T, td):
    return 12*pi**4/5*n*na*k*(T/td)**3

param,_ = curve_fit(cvl,T,cv)
td = param[0]
print("Debye Temperature =", td, "K")
plot(T,cv,'.',label="Data")
plot(T,cvl(T,td),label="Fitted Plot")
xlabel("$T$")
ylabel("$C_V(T)$")
legend()
show()
