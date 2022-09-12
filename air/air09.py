#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 21:26:40 2022

@author: patry
"""
import sys 

########################################################################
def tri_selectif(mon_tableau): 
        l= len(mon_tableau)
        for i in range(0,l-1):
            mini=i
            for j in range(i+1,l):
                if mon_tableau[j]<mon_tableau[mini]:
                    mini=j
            if mini != i:
                (mon_tableau[i],mon_tableau[mini])=(mon_tableau[mini],mon_tableau[i])
        return(mon_tableau)
    
########################################################################

def sorted_fusion (array1,array2):
    for i in range(0,len(array2)):
        array1.append(array2[i])
    tri_selectif(array1)
    for i in range(0,len(array1)):
        print(array1[i],end=' ')
    print('')

########################################################################

l = len(sys.argv)

if l <4: 
    sys.exit('error')
    
array1=[]
array2=[]

try:
    for i in range(1,l):
        index=[]
        if sys.argv[i]== 'fusion':
            index.append(i)
            break
        
        array1.append(int(sys.argv[i]))
    if len(index) != 1:
            sys.exit('error')
    for i in range(index[0]+1,l):
        array2.append(int(sys.argv[i]))
        
except:
    sys.exit('error')
else:
    
    sorted_fusion(array1, array2)
