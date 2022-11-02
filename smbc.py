from pylab import *
from scipy.integrate import quad

n = 100
m = 1000
um = -5.0

t = linspace(0,4,n)
mu = zeros(n)
en = zeros(n)
cv = zeros(n)
cf = zeros(n)

for i in range(n-1,-1,-1):
    if t[i]>1:
        mt = linspace(um,1e-5,m)
        for j in range(m):
            def f(x):
                return x**0.5/(exp((x-mt[j])/t[i])-1.0)
            if abs(quad(f,1e-5,100)[0]-2.315)<=1e-2:
                mu[i] = mt[j]
                break

for i in range(n):
    def g(x):
        return x**1.5/(exp((x-mu[i])/t[i])-1.0)
    en[i] = quad(g,1e-5,100)[0]/2.315

h = (max(t)-min(t))/(n-1)
for i in range(1, n):
    cv[i] = (en[i]-en[i-1])/h

for i in range(n):
    if t[i]<=1:
        def l(x):
            return x**1.5/(exp((x-mu[i])/t[i])-1.0)
        cf[i] = 1-2/(2.612*pi**0.5)*quad(l,1e-5,100)[0]

plot(t, mu)
show()
plot(t, en)
show()
plot(t, cv)
show()
plot(t, cf)
show()
