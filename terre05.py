#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:26:18 2022

@author: patry


"""
import sys 

while True:
 try:
  nombre = int(sys.argv[1])
  break
 except ValueError:
  print("Tu nous la metrra pas a l'envers") 
nombre2=nombre%2 
if nombre2 == 0 :
    print('pair')
else :
    print('impair')

        
