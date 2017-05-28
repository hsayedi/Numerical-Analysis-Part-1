# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:33:38 2016

@author: Husna
"""

# Homework 3 num 3 part A
# computing coefficients to evaluate the corresponding interpolation polynomial at arbitary point x

x = [0,1,2]
f = [0,1,2]
n = 2
a = 3                             #point we are evaluating



def newton(x,f,n,a):
    c = [0]*(n+1)
    for j in range(0,n+1):
        c[j]=f[j]
    for k in range(1,n+1):
        for j in range(n,k-1,-1):
            c[j] = (c[j]-c[j-1])/(x[j]-x[j-k])

    p=c[n]
    for j in range(n-1,-1,-1):
        p=c[j]+(a-x[j])*p          # <---p(a)
    return p



new=newton(x,f,n,a)
print(new)


# Homework 3 num 3 part B
# computing coefficients to evaluate the corresponding interpolation polynomial at arbitary point x


import math
import matplotlib.pyplot as plt
    
def newton(x,f,n,a):
    c = [0]*(n+1)
    for j in range(0,n+1):
        c[j]=f[j]
    for k in range(1,n+1):
        for j in range(n,k-1,-1):
            c[j] = (c[j]-c[j-1])/(x[j]-x[j-k])

    p=c[n]
    for j in range(n-1,-1,-1):
        p=c[j]+(a-x[j])*p          # <---p(a)
    return p


def f(x):
    return math.exp(-x**2)
n = 10   
x = [0]*11
g = [0]*11
for j in range(0,11):
        x[j] = -1+j*(2/10)
        g[j] = f(x[j])
xbar=[0]*101
p=[0]*101
fbar=[0]*101
dif=[0]*101
for j in range(0,101):
        xbar[j] = -1+j*(2/100)
        p[j] = newton(x,g,n,xbar[j])
        fbar[j] = f(xbar[j])
        dif[j]=fbar[j]-p[j]
plt.plot(xbar,dif)    



