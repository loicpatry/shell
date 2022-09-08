#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 09:18:13 2022

@author: patry
"""
import sys 


n = len(sys.argv)
if n<3:
    sys.exit('error')
try:
    for i in range(1,n):
        nombre=int(sys.argv[1])
except: 
    sys.exit('veuillez n\'entrer que des nombres')
else:
    liste_de_nombres= []
    for s in range(1,n):
        liste_de_nombres.append(int(sys.argv[s]))
    N=len(liste_de_nombres)
    difference=[]
    for x in range(0,N-1):
        for l in range(x+1,N):
            dif=abs(((liste_de_nombres[l])-(liste_de_nombres[x])))
            difference.append(dif)
    print(min(difference))
