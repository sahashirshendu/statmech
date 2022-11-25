from pylab import *

n=1
k=1.38e-23
na=6.02e23
td=92

def trap(f,a,b,n):
    h=(b-a)/n
    sum=f(a)+f(b)
    for i in range(1,n):
        sum+=2*f(a+i*h)
    return h/2*sum

T=linspace(1e-5,200,100)

def cv(x):
    return x**4*exp(x)/(exp(x)-1)**2
cvt=zeros(len(T))
for i in range(len(T)):
    cvt[i] = trap(cv,1e-5,td/T[i],100)
cvt=3*n*na*k*3*(T/td)**3*cvt

cvl=12*pi**4/5*n*na*k*(T/td)**3

plot(T, cvt, label="General $T$")
plot(T, cvl, label="T << $T_D$")
xlabel("$T$")
ylabel("$C_V(T)$")
ylim(0,30)
legend()
show()
