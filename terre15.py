#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:52:55 2022

@author: patry
"""
import sys 

n = len(sys.argv)

try :
    for i in range(1,n):   
        nombre = int(sys.argv[i])
except:
    sys.exit('error')
else:
    s=1
    while s<n-1:
        if int(sys.argv[s])>int(sys.argv[s+1]):
            sys.exit('Pas trié!')
        s=s+1
    sys.exit('Trié!')   
    
