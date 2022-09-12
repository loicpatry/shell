#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:31:43 2022

@author: patry
"""
import sys 

if len(sys.argv)!= 3:
    sys.exit('error')
try: 
    nbr_collone =int(sys.argv[1])
    nbr_ligne = int(sys.argv[2])
except:
    sys.exit('error')
else: 
    tableau=[]
    for a in range(nbr_ligne):
        tableau.append([])
        for i in range(nbr_collone):
            tableau[a].append(' ')
    
    L_i=len(tableau)
    L_j=len(tableau[0])  
    
    for i in range(L_i):
        for j in range(L_j):
            if (i==0 and j==0) or (i==0 and j==L_j-1) or (i==L_i-1 and j==0) or(i==L_i-1 and j==L_j-1):
                tableau[i][j]='O'
                
                #print(i,j)
            if (i==0 or i==L_i-1) and (j != 0 and j!= L_j-1):
                tableau[i][j]='-'
                #print(i,j)
            if (i != 0 and i != L_i-1) and (j == 0 or j== L_j-1):
                tableau[i][j]='|'
                #print(i,j)
    for i in range(0,len(tableau)):
        tableau[i]=''.join(tableau[i])
        print(tableau[i])
