#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 00:01:27 2022

@author: patry
"""
import sys
if len(sys.argv) != 2:
    sys.exit('-1')
try : 
    nombre=int(sys.argv[1])
except : 
    sys.exit('-1')
else:
    if nombre<0: 
        sys.exit('-1')
    nombre_premier_list =[]
    liste_de_nombre=[]
    nombre=int(sys.argv[1])
    for i in range(0,nombre*10):
        liste_de_nombre.append(i)
    
    for l in liste_de_nombre:
        for d in range(2,int(l/2+1)):
            if l%d==0 :
                break
        else:
            nombre_premier_list.append(l)
    b=0
    while b<200000:
        try:
            index = nombre_premier_list.index(nombre)
        except:
            nombre=nombre+1
        else:
            print(nombre_premier_list[index])
            sys.exit()
        b=b+1
