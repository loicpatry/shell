#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:56:01 2022

@author: patry
"""
import sys 

try: 
    nombre= int(sys.argv[1])
except:
    sys.exit('False')
else: 
    sys.exit('True')
