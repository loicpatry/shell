#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:37:35 2022

@author: patry
"""
import sys 

if len(sys.argv) >3:
    sys.exit('Veuillez entrer deux nombres')
if len(sys.argv) < 3:
    sys.exit('Veuillez entrer deux nombres')
try:
    int(sys.argv[1])
except:
    sys.exit('Veuillez entre deux nombre')  
else:
    nombre=int(sys.argv[1])
    exposant=int(sys.argv[2])
    print(nombre**exposant)
    
       
    
#n = 1
#for e in range(1, exposant+1):
    #n=nombre*n
#print(n)

    
