#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:21:24 2022

@author: patry
"""
import sys 

if len(sys.argv) != 3:
    sys.exit('error')
try: 
    caractere=sys.argv[1]
    nombre_etage=int(sys.argv[2])
except:
    sys.exit('error')
else:
    tableau=[]
    for i in range(nombre_etage):
        tableau.append([])
        for a in range(0,(nombre_etage*2)-1):
            tableau[i].append(caractere)
        
    
            
    for i in range(len(tableau)):
        for a in range(0,nombre_etage-1-i):
            tableau[i][a]=' '
        for a in range(nombre_etage+i,len(tableau[i])):
            tableau[i][a]=' '
        tableau[i]= ''.join(tableau[i])
        print(tableau[i])
