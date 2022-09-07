#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:58:21 2022

@author: patry
"""
import sys 

try :
    nombre1 = int(sys.argv[1])
    nombre2 = int(sys.argv[2])
except:
    sys.exit('entrer deux nombres')
else:
    for i in range(nombre1,nombre2):
        print(i,end=' ')
    print('')
