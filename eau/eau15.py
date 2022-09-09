#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:23:59 2022

@author: patry
"""
import sys
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
    
def split(s):
    return [char for char in s]
    
l=len(sys.argv)
arguments=[]
for i in range(1,l):
    arguments.append(sys.argv[i])

    
for s in range(len(arguments)):
    lol=arguments[s]
    arguments[s] = split(lol)

for a in range(len(arguments)):
    long2=len(arguments[a])
    for z in range(long2):
        arguments[a][z]=ord(arguments[a][z])
arguments_init=arguments

#print(arguments_init)
L=len(arguments)    
mon_tableau_init=[]
for b in range(0,L):
    mon_tableau_init.append(arguments_init[b][0])
mon_tableau=[]
for b in range(0,L):
    mon_tableau.append(arguments[b][0])
tri_selectif(mon_tableau)

for g in range(0,L):
    index=mon_tableau_init.index(mon_tableau[g])+1
    print(sys.argv[index],end=' ')
print('')

