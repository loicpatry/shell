#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 21:09:44 2022

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

def sorted_insert(array, new_element):
    
    array.append(new_element)
    
    tri_selectif(array)
    for i in range(0,len(array)):
        print(array[i],end=' ')
    print('')
########################################################################
    
    

l = len(sys.argv)

if l <3: 
    sys.exit('error')

array=[]
try:
    for i in range(1,l-1):
        array.append(int(sys.argv[i]))
    new_element=int(sys.argv[l-1])

    
except:
    sys.exit('Veuillez n\'entrer que des nombres')
else:
    sorted_insert(array,new_element)
    
    
