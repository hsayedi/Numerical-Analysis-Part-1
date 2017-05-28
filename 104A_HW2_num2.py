# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:04:23 2016

@author: Husna
"""
x = [0,1,2]


import numpy as np 

def bay(x,n):
    L=np.zeros((n+1),(n+1))
    L[0,0]=1
    for m in range(1,n+1):
        for j in range(0,m):
            L[m,j]=(L[m-1,j])/(x[j]-x[m])
    p=1
    for k in range(0,m):
        p=p*(x[m]-x[k]) 
    L[m,m]=1/p
    l=L[n]
    return l
    
    

    
    
    
            
    