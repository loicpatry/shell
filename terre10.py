#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:37:35 2022

@author: patry
"""
import sys 

if len(sys.argv) >2:
    sys.exit('Veuillez entrer un nombres')
if len(sys.argv) < 2:
    sys.exit('Veuillez entrer un nombres')
try:
    int(sys.argv[1])
except:
    sys.exit('Veuillez entre un nombre')  
else:
    nombre=int(sys.argv[1])
    print(nombre**(1/2))
    
