#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 19:35:10 2022

@author: patry
"""
import sys 

if len(sys.argv) != 2:
    sys.exit('error')

def split(s):
    return [char for char in s]
arguments= split(sys.argv[1])
index=[]
for i in range(0,len(arguments)-1):
    if arguments[i] == arguments[i+1]:
        index.append(i)


for element in index:   
    #print(element)
    arguments.pop(element)
    for i in range(0,len(index)):
        index[i]=index[i]-1
    


arguments2= ''.join(arguments)
print(arguments2)
    

    
