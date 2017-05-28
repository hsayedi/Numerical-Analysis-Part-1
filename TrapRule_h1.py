# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:34:39 2016

@author: Husna
"""

#Homework 1 number 2
#Name: Husna Sayedi 
#Perm: 3446721
#Date last modified: October 3, 2016
#Composite Trapezoidal Rule: This code is to approximate what the area is under
#a curve of an unintegrable function. The CTR gives us an approximate value of
#the real area of the curve. The CTR gives us a better estimate of the curve 
#by dividing the function into small trapezoids. The output should be numerous 
#values of the small trapezoidal areas. 
#a and b are the bounds of the integra. n is the number of subintervals of equal
#length. The code will sum up the result. The function I am integating is sin(x)

#To check the accuracy of my code, I computed the actual value of sin(x) and then 
#compared it to my code output: 
#Real value when integrated = 0.459697694131860
#Output of code = .45960191978824727
#Error = I[f] - Th[f] = 9.577434361274229e-05

#2

import math


def f(x):
    return math.sin(x)

def Trap(a,b,n):    
    h = float(b-a)/n
    s = .5*f(a)+.5*f(b)
    for i in range(1, n):
        s += f(a + i*h)
    return(h*s)
   
a = 0 
b = 1
n = 20

print(Trap(a,b,n))
            
    










