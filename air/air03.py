#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 22:34:56 2022

@author: patry
"""
import sys 
if len(sys.argv)==1:
    sys.exit('error')
tableau_arg=[]
for i in range(1,len(sys.argv)-1):
    tableau_arg.append(sys.argv[i])
separateur = sys.argv[len(sys.argv)-1]
def concat (tableau_arg,separateur):
    for i in range(0,len(tableau_arg)):
        print(tableau_arg[i],end=separateur)
    print('')
concat(tableau_arg,separateur)
