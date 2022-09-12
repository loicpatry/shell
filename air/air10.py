#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:44:15 2022

@author: patry
"""
import sys 

if len(sys.argv)<3:
    sys.exit('error')

def ma_rotation (array):
    l=len(array)
    rotation=[]
    for i in range(1,len(array)):
        rotation.append(array[i])
    rotation.append(array[0])
    for i in range(len(rotation)):
        array[i]=rotation[i]
    
    
    return array
    
l=len(sys.argv)
array=[]
for i in range(1,l):
    array.append(sys.argv[i])
ma_rotation(array)

for i in range(len(array)):
    print(array[i],end=' ')
print('')
