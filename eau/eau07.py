#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:42:20 2022

@author: patry
"""
import sys 

if len(sys.argv) != 2:
    sys.exit('error')

try : 
    nombre= int(sys.argv[1])
except : 
    string = sys.argv[1]
    liste=[]
    for letter in string:
        liste.append(letter)
    n= string.__len__()
    for i in range(n):
        if i%2==0:
            liste[i]=liste[i].upper()
        else: 
            liste[i]=liste[i].lower()
    string_crr = "".join(liste)
    print(string_crr)
        
else: 
    sys.exit('veuillez entrer une chaine de caractère')
