## -*- coding: utf-8 -*-
#"""
#Created on Thu Nov  3 17:09:21 2016
#
#@author: Husna
#"""
#
##104A Homework 4
#
#
#import numpy as np 
#import math
#
#
#
#def spline(x,f,n):
#    h=[0]*(n)               #calculate h values
#    for i in range(0,n):
#        h[i]=x[i+1]-x[i]
#        print(h[i])
#    a=np.zeros((n-1,n-1))
#    for i in range(0,n-1):
#        a[i,i]=2*(h[i]+h[i+1])
#    for i in range(0,n-2):
#        a[i,i+1]=h[i+1]
#    for i in range(1,n-1):
#        a[i,i-1]=h[i+1]
#    d=[0]*(n-1)
#    m=[0]*(n-1)
#    for i in range(0,n-1):
#        d[i]=(-6/(h[i])*(f[i+1]-f[i])+(6/(h[i+1]))*(f[i+2]-f[i+1])
#        #print(d[i])
#    m=np.linalg.solve(a,d)
#    print(m)
#    return(m)
#n=2
#q=[0]*(n-1)
#x=[0,1,2]
#f=[0,1,16]
#z=spline(x,f,n)
#print(m)
#

#
#import numpy as np
#import math
#
#def spline(x,f,m):
#    n = len(x)-1
#    h = [0]*n                           # h values
#    for i in range(0,n):
#        h[i] = x[i+1]-x[i]   
#    y = [0]*(n-1)                         # y values
#    for i in range(0,n-1): 
#        y[i] = (-6/h[i])*(f[i+1]-f[i])+(6/h[i+1])*(f[i+2]-f[i+1])  
#    T = np.zeros((n-1,n-1))
#    for i in range(0,n-2):
#        T[i,i] = 2*(h[i]+h[i+1])
#        T[i,i+1] = h[i+1]
#        T[i+1,i] = h[i+1]
#    T[n-2,n-2] = 2*(h[n-2]+h[n-1])
#    z = [0]*(n+1)
#    q = np.linalg.solve(T,y)
#    for i in range(1,n):
#        z[i] = q[i-1]
#    a = [0]*n
#    b = [0]*n
#    c = [0]*n
#    d = [0]*n
#    for i in range(0,n):
#        a[i] = (1/(6*h[i]))*(z[i+1]-z[i])
#        b[i] = (1/2)*(z[i])
#        c[i] = (1/h[i])*(f[i+1]-f[i])-((1/6)*h[i]*(z[i+1]+2*z[i]))
#        d[i] = f[i]
#    for i in range(0,n):
#        if (m<=x[i+1] and m>=x[i]):
#            P = (a[i]*(m-x[i])**3)+(b[i]*(m-x[i]**2))+(c[i]*(m-x[i]))+d[i]         
#    return P
#
#x = [0,1,2]
#f = [0,1,2]
#m=1.5
#P= spline(x,f,m)
#print(P)
#
#
#
#
## Problem 2 
#
#
#
#def paramcurve(p,x,y,n):
#    l = len(x)-1
#    A = [0]*n
#    for i in range(0,len(x)):
#        A[i] = p[0]+i*((p[l]-p[0])/n)
#    
#    B = [0]*n
#    for i in range(0,len(x)):
#        B[i] = matrix(p,x,A[i])
#    
#    C = [0]*n
#    for i in range(0,len(x)):
#        C[i] = matrix(p,y,A[i])
#    
#    plt.plot(B,C)
#    plt.show()
#
#n = 90    
#a = [0,0.618,.935,1.255,1.636,1.905,2.317,2.827,3.330]
#b = [1.5,.9,.6,.35,.2,.1,.5,1,1.5]
#c = [.75,.9,1,.8,.45,.2,.1,.2,.25]
#D = paramcurve(a,b,c,n)
#print(D)
#
#print(spline(a,b,1.9))


#104A Homework 4


import numpy as np 
import math



def tridiag(N,a,b,c,d):
    m = [0]*N
    m[0]=a[0]
    l = [0]*(N-1)
    for j in range(0,N-1):
        l[j]=c[j]/m[j]
        m[j+1]=a[j+1]-l[j]*b[j]
    y = [0]*N
    y[0]=d[0]
    for j in range(1,N-1+1):
        y[j] = d[j-1]-l[j-1]
    x[N-1] = y[N-1]/m[N-1]
    for j in range(N-2,-1,0-1):
        x[j] = (j[j]-b[j]*x[j+1])/m[j]
        
def spline(x,f,n,p):
    h = [0]*n
    for j in range(0,n-1+1):
        h[j]=x[j+1]-x[j]
    maindiag = [0]*(n-1)
    upperdiag = [0]*(n-2)
    lowerdiag = [0]*(n-2)
    for j in range(0,n-2+1):
        maindiag[j] = 2*(h[j]+h[j+1])
    for j in range(0,n-3+1):
        upperdiag[j] = h[j+1]
    lowerdiag = upperdiag 
    rhs = [0]*(n-1)
    for i in range(0,n-2+1):
        rhs[j] = (-6/h[j])*(f[j+1]-f[j])+(6/h[j+1])*(f[j+2]-f[j+1])
    
    z = tridiag(n-1,maindiag,upperdiag,lowerdiag,rhs)
    z = (0,z,0)
    a = [0]*n
    b = [0]*n
    c = [0]*n
    d = f 
    for j in range(0,n-1+1):
        a[j] = (1/6*h[j])*(z[j+1]-z[j])
        b[j]
        c[j]
    for i in range(0,n-1+1):
        if (p<=x[i+1] and p>=x[j]
            s = a[j]*(x-x[j])**3 + b[j]*(x-x[j])**2 + c[j]*(x-x[j]) + d[j]
    return s,a,b,c,d
      