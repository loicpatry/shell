#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 22:03:12 2022

@author: patry
"""
import sys 


n = len(sys.argv)
if n<3: 
    sys.exit('error')
tableau=[]

for i in range(1,n-1):
    tableau.append(sys.argv[i])
try :
    index= tableau.index(sys.argv[n-1])
except: 
    sys.exit('-1')
else: 
    print(index)
