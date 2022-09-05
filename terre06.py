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
  nombre2 = int(sys.argv[2])
  break
 except ValueError:
  print("erreur") 
nombre_carre=nombre*nombre
nombre2_carre=nombre2*nombre2
if nombre_carre<nombre2_carre or nombre==0 or nombre2==0:
    print('erreur')
else :
    reste = nombre%nombre2
    resultat = nombre/nombre2
    print('resultat: ' ,int(resultat))
    print('reste' ,reste)
