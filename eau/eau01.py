#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 23:23:36 2022

@author: patry
"""
array1 =[0,1,2,3,4,5,6,7,8,9]
array2 =[0,1,2,3,4,5,6,7,8,9]
array3 =[0,1,2,3,4,5,6,7,8,9]

for a in array1:
    for b in array2:
        for c in array3:
            if c>b and b>a and a!=b and b!=c :
                print(str(a)+str(b)+str(c)+',', end=' ')
print('')
                
               
