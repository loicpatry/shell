#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:21:21 2022

@author: patry
"""
import random 
import sys 
import numpy as np
#x=sys.argv[1]
file=open('plateau.txt','w+')

try: 
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    density=int(sys.argv[3])
except:
    sys.exit('error')
else:
    
    if x<y:
        l_carre_max=x
    if y<x:
        l_carre_max=y
    if x==y:
        l_carre_max=y
    
    #y=sys.argv[2]
    #density=sys.argv[3]
    tableau=[]
    liste=['x','.']
    
    for i in range(x):
        tableau.append([])
        for j in range(y):
            x=random.choices(liste, cum_weights=(density,100-density))
            tableau[i].append(x[0])
    file.write(sys.argv[1])
    file.write('.')
    file.write('x')
    file.write('o')
    file.write('\n')
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            file.write(tableau[i][j])
        file.write('\n')
