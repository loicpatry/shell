#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 23:51:23 2022

@author: patry
"""
import sys 


N = int(sys.argv[1])
if N<0: 
    sys.exit('-1')
fibonacciList = [0, 1]
term = 2
while term < N + 1:
    value = fibonacciList[term - 1] + fibonacciList[term - 2]
    fibonacciList.append(value)
    term = term + 1
    
print(fibonacciList[N])
