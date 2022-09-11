#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 12:38:07 2022

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

#########################################

l=len(sys.argv) ## transformer les arguments en liste
arguments=[]
for i in range(1,l):
    arguments.append(sys.argv[i])

#########################################

for s in range(len(arguments)):  #transformer les arguments en liste de liste avec les letrres
    lol=arguments[s]
    arguments[s] = split(lol)
    
#########################################
    
for a in range(len(arguments)):  # transformer les arguments en liste de liste avec les numéros ASCII
    long2=len(arguments[a])
    for z in range(long2):
        arguments[a][z]=str(ord(arguments[a][z]))

arguments_init=[]
for a in range(0,len(arguments)):
    arguments_init.append(arguments[a])

for i in range(len(arguments)-1,0,-1):
    for j in range(0,i):
        b=0
        while arguments[j+1][b]==arguments[j][b]:
            b=b+1
        if arguments[j+1][b]<arguments[j][b]:
            (arguments[j+1],arguments[j])=(arguments[j],arguments[j+1])
            
for a in range(0,len(arguments)):
    index= arguments_init.index(arguments[a])
    print(sys.argv[index+1],end=' ')
print('')
    
