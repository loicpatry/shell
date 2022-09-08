#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 09:46:43 2022

@author: patry
"""
import sys 

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
    
    def my_bubble_sort(mon_tableau):
        for i in range(n-1,1,-1):
            for j in range(0,i-1):
                if mon_tableau[j+1]<mon_tableau[j]:
                    (mon_tableau[j+1],mon_tableau[j])=(mon_tableau[j],mon_tableau[j+1])
        return(mon_tableau)
    
    my_bubble_sort(mon_tableau)
    for element in mon_tableau:
        print(element,end=' ')
    print('')
    
