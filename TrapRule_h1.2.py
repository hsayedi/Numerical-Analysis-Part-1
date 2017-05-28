# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:35:22 2016

@author: Husna
"""
#Homework 1 Problem 3
#First I found the exact value of the function I[f]. 
#Next, for h=1/10, our n=10. Therefore using my code, I found the value of Th[f] 
#using that particular value of n. 
#I continued this procedure for h=1/20 with n=20. Then I found Th/2[f] using my code. 
#And lastly, for h=1/40, n=40. Then I found Th/4[f]. 
#
#To verify if Th[f] has a convegent trend, I used the formula 
#(I[f]-Th[f])/(I[f]-Th/2[f]) and 
#(I[f]-Th/2[f])/(I[f]-Th/4[f]) and I found that the value for both of these formulas was 
#approximately 4 (see homework), which verifes that Th[f] has a convergent trend at a 
#quadratic rate.





import math


def f(x):
    return x*(math.e)**(x**2)

def Trap(a,b,n):    
    h = float(b-a)/n
    s = .5*f(a)+.5*f(b)
    for i in range(1, n):
        s += f(a + i*h)
    return(h*s)
   
a = 0 
b = 1
n = 10

print(Trap(a,b,n))
