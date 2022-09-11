#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 09:46:43 2022

@author: patry
"""
import sys 

#############################################################################

def tri_selectif(mon_tableau):
        l= len(mon_tableau)
        for i in range(0,l-1):
            mini=i
            for j in range(i+1,l):
                if mon_tableau[j]<mon_tableau[mini]:
                    mini=j
            if mini != i:
                (mon_tableau[i],mon_tableau[mini])=(mon_tableau[mini],mon_tableau[i])
        for element in mon_tableau:
            print(element,end=' ')
        print('')

#############################################################################
n=len(sys.argv)

if n<3:
    sys.exit('error')
try:
    for q in range(1,n):
        nombre=int(sys.argv[q])
except: 
    sys.exit('veuilez n\'entrez que des nombres')
else:

    mon_tableau=[]
    
    for m in range(1,n):
        mon_tableau.append(int(sys.argv[m]))
    
    tri_selectif(mon_tableau)
