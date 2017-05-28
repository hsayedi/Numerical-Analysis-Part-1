# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:59:41 2016

@author: Husna
"""

# Homework 5 Number 2 
import math
import numpy 


def ck(f,N):
    c = np.fft.fft(f)
    ak = c.real*(m)
    bk = c.imag*(m)
    return(ak,bk)

def P(x,N,a,b):
    for j in range(1,m):
        sum=a[j]*math.cos(j*x)+b[j]*math.sin(j*x)+sum
    P = .5*a[0]+sum+.5*a[N/2]*math.cos(m*x)
    return(P)

def Prime(a,b,xj,m):
    for j in range(1,m):
        sum = (-j)*a[j]*math.sin(j*xj)+j*b[j]*math.cos(j+xj)

for j in range(0,N):
    x[j]= j*(2*math.pi)/N    
    f[j]= math.exp(math.sin(x[j]))
    
N = 8
m =int(round(N/2,2.0))
f = [0]*N
x = [0]*N
prime=[0]*N
for j in range(0,N):
    x[j]=j*2*math.pi/N
    f[j]=math.exp(math.sin(x[j])
    prime=Prime(a,b,x[j],m)
   


#Y = (-5.79829066331+4.55640490659j)
#
#Z = (Y.real, Y.imag)
#
#A = Y.real
#B = Y.imag
#print(Z)
#    


                  
                  
# Homework 5 Number 4 


import math
import numpy as np

#These will be our C values

N = 8
m =int(round(N/2.0))
f = [0]*N
x = [0]*N
prime=[0]*N
for j in range(0,N):
    x[j]=j*2*math.pi/N
    f[j]=math.exp(math.sin(x[j]))
     
c=np.fft.fft(f)
print(c)                                #printing C values
sum=[0]*N
for i in range(5,8):
    sum[i]=j*i*c[i]*math.exp(i*j*x[0])













