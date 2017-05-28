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
