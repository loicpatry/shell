#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:37:35 2022

@author: patry
"""
import sys 


if sys.argv.__len__() >2:
    sys.exit('Veuillez entrer une seule chaine de caractère')
if sys.argv.__len__() ==1:
    sys.exit('Veuillez entrer une chaine de caractère')   
try:
    int(sys.argv[1])
except:
    string=sys.argv[1]
    print(string.__len__())  
else:
    sys.exit('error')
    
    
