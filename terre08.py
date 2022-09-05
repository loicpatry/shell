#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:37:35 2022

@author: patry
"""
import sys 
i=0
while i==0:
    if len(sys.argv) >2:
        print('Veuillez entrer une seule chaine de caractère')
        break
    if type(int(sys.argv[1])) == int:
        print('erreur')
        break
    if len(sys.argv) ==1:
        print('Veuillez une chaine de caractère')
        break
    string=sys.argv[1]
    print(len(string))
    i=i+1
    
