#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:52:55 2022

@author: patry
"""
import sys 

if len(sys.argv) >4:
    sys.exit('error')
if len(sys.argv) <4 :
    sys.exit('error')

try :
    nombre1 = int(sys.argv[1])
    nombre2 = int(sys.argv[2])
    nombre3 = int(sys.argv[3])
except:
    sys.exit('error')
else:
    if nombre1==nombre2 and nombre1==nombre3:
        sys.exit('error')
    if nombre1>nombre2 and nombre1<nombre3 :
        print(nombre1)
    if nombre2>nombre3 and nombre2<nombre1 :
        print(nombre2)
    if nombre3>nombre1 and nombre3<nombre2 :
        print(nombre3)
