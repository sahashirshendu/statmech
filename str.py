from pylab import *

def f(n):
    sum = 0
    for i in range(1,n+1):
        sum += log(i)
    return sum

n = arange(1,201,1)
f1 = zeros(200)
f2 = zeros(200)
for i in range(200):
    f1[i] = f(n[i])
    f2[i] = n[i]*log(n[i])-n[i]

plot(n,f1,label='ln(N!)')
plot(n,f2,label='Nln(N)-N')
xlabel('N')
xscale('log')
yscale('log')
legend()
show()
