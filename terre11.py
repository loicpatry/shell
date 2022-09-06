#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:43:52 2022

@author: patry
"""
import sys

if sys.argv.__len__() <2 :
    sys.exit('error')
if sys.argv.__len__() >2 :
    sys.exit('error')

try:
    nombre= int(sys.argv[1])
except: 
    sys.exit('Veuillez entre un nombre')
else: 
    if nombre ==0 :
        sys.exit('Non, ce n\'est pas un nombre premier')
    if nombre ==1 :
        sys.exit('Non, ce n\'est pas un nombre premier')
    if nombre ==2 :
        sys.exit('Oui, c\'est un nombre premier')   
    for i in range(2,int(nombre/2+1)):
        if (nombre%i) ==0:
            sys.exit('Non, ce n\'est pas un nombre premier')
    sys.exit('Oui, c\'est un nombre premier')
