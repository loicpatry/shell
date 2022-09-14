#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 22:42:14 2022

@author: patry
"""
import sys 


if len(sys.argv)==1:
    sys.exit('error')
try: 
    for b in range(1,len(sys.argv)):
            x= int(sys.argv[b])

    
except:
    for i in range(0,len(sys.argv)-1):
        liste_arg=[]
        for b in range(1,len(sys.argv)):
            liste_arg.append(sys.argv[b])
        liste_arg_ref=[]
        for a in range(1,len(sys.argv)):
            liste_arg_ref.append(sys.argv[a])
        liste_arg.remove(liste_arg[i])
        
        if liste_arg_ref[i] in liste_arg:
            continue
        else:
            print(liste_arg_ref[i])
else:
    for i in range(0,len(sys.argv)-1):
        liste_arg=[]
        for b in range(1,len(sys.argv)):
            liste_arg.append(int(sys.argv[b]))
        liste_arg_ref=[]
        for a in range(1,len(sys.argv)):
            liste_arg_ref.append(int(sys.argv[a]))
        liste_arg.remove(liste_arg[i])
        
        if liste_arg_ref[i] in liste_arg:
            continue
        else:
            print(liste_arg_ref[i])
