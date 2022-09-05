#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:37:35 2022

@author: patry
"""
import sys 
i=0
while i==0:
    string=sys.argv[1]
    reverse_string= string[::-1]
    print(reverse_string)
    i=i+1
    if len(sys.argv) >2:
        print('Veuillez entrer une seule chaine de caractère')
        break
