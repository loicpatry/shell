#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:46:48 2022

@author: patry
"""
import sys 

try : 
    nombre= int(sys.argv[1])
except : 
    string = sys.argv[1]
    liste= string.split(' ')
    
    n= liste.__len__()
    for i in range(n):
        liste2=[]
        for letter in liste[i]:
            liste2.append(letter)
        liste2[0]=liste2[0].upper()
        liste[i]="".join(liste2)
        
    string_crr = " ".join(liste)
    print(string_crr)
        
else: 
    sys.exit('veuillez entrer une chaine de caractère')
