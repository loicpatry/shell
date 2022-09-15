#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:14:44 2022

@author: patry
"""
import sys 
if len(sys.argv) != 2:
    sys.exit('error')

try:
    f=open(sys.argv[1],'r')
    
except: 
    sys.exit('error')
else:
    print(f.read())
