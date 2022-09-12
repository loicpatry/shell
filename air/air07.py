#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:20:46 2022

@author: patry
"""
import sys


if len(sys.argv)<3:
    sys.exit('error')
def ma_fonction(array_de_string,string):
    index=[]
    for i in range(0,len(array_de_string)):
        if string in array_de_string[i] or string.upper() in array_de_string[i]:
            index.append(i)
    for element in index:
        array_de_string.pop(element)
        for i in range(0,len(index)):
            index[i]=index[i]-1
            
    
    
    
    return array_de_string
    
    
    
    
    
l= len(sys.argv)
array_de_string=[]
for i in range(1,l-1):
    array_de_string.append(sys.argv[i])
string= sys.argv[l-1]

ma_fonction(array_de_string, string)

for i in range(0,len(array_de_string)):
    print(array_de_string[i],end=' ')
print('')


