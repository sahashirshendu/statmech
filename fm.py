from pylab import *
from scipy.integrate import quad

n = 100
m = 1000
um = -5.0

t = linspace(0,1.5,n)
mu = zeros(n)
en = zeros(n)
cv = zeros(n)
cf = zeros(n)

for i in range(n-1,0,-1):
    mt = linspace(um,1.0,m)
    for j in range(m):
        def f(x):
            return x**0.5/(exp((x-mt[j])/t[i])+1.0)
        if abs(quad(f,1e-5,100)[0]-2./3.)<=1e-2:
            mu[i] = mt[j]
            break

title('Chemical Potential')
plot(t,mu,label='Numerical')
plot(t,1-pi**2/12*t**2,label='Analytical')
plot(t,zeros(len(t)))
legend()
show()
