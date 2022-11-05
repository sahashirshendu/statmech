from pylab import *

"""
v= linspace(0,05,10000)
def f(v):
    return v**2*exp(-v**2)    
n=f(v)
plot(v,n)
show()
"""

def p(v):
    return 2 * a * v**0.5 * exp(-b*v)

v = linspace(0,5,100)
m = 1
k = 1
T = 1
a = pi**-0.5
b = 1
xmin = 0.0
xmax = 1000.0
n = 10000
h = (xmax-xmin)/n

sum = p(xmin)+p(xmax)
for i in range(1,n):
    if i % 2 == 0.0:
        sum += 2*(p(xmin+i*h))
    else:
        sum += 4*(p(xmin+i*h))
I = (h / 3) * sum
print(I)

plot(v, p(v))
show()
