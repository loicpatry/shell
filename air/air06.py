#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 19:57:10 2022

@author: patry
"""
import sys 


L=len(sys.argv)
variable=[]
try: 
    for i in range(1,L-1):
        variable.append(int(sys.argv[i]))
except:
    sys.exit('veuillez rentrer des nombres')
else:
    operation = sys.argv[L-1][0]

    number= int(sys.argv[L-1][1:])

    
    
    if operation== '+':
        for i in range(0,len(variable)):
            variable[i]= variable[i] + number
    if operation== '-':
        for i in range(0,len(variable)):
            variable[i]= variable[i] - number
    if operation== '*':
        for i in range(0,len(variable)):
            variable[i]= variable[i] * number
    if operation== '/':
        for i in range(0,len(variable)):
            variable[i]= variable[i] / number
            
    for i in range(0,len(variable)):
        print(variable[i],end=' ')
    print('')
