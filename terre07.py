#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:37:35 2022

@author: patry
"""
import sys 

if len(sys.argv) >2:
    sys.exit('Veuillez entrer une seule chaine de caractère')
if len(sys.argv) ==1:
    sys.exit('Veuillez une chaine de caractère')   
try:
    int(sys.argv[1])
except:
    string=sys.argv[1]
    reverse_string= string[::-1]
    print(reverse_string)    
else:
    sys.exit('error')
    
