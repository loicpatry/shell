#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:45:47 2022

@author: patry
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:22:41 2022

@author: patry
"""

import random 
import sys 
import numpy as np
#x=sys.argv[1]
x=6
y=10
if x<y:
    l_carre_max=x
if y<x:
    l_carre_max=y
if x==y:
    l_carre_max=y
density=0
#y=sys.argv[2]
#density=sys.argv[3]
tableau=[]
liste=['x','.']
resultat=[]

for i in range(x):
    tableau.append([])
    for j in range(y):
        x=random.choices(liste, cum_weights=(density,100-density))
        tableau[i].append(x[0])
for i in range(len(tableau)):
    print(tableau[i])


for ordo in range(len(tableau)):
    for absi in range(len(tableau[0])):
        for l in range(1,l_carre_max+1):
            try:
                tableau1=[]
                for i in range(l):
                    if absi+l > len(tableau[ordo+1]):
                        break
                    if ordo+l > len(tableau):
                        break
                    tableau1.append(tableau[ordo+i][absi:absi+l])
                
                #print(l)
                #print('')
                check=True
                if len(tableau1) == 0:
                    check=False
                for u in range(len(tableau1)):
                    for y in range(len(tableau1[u])):
                        if tableau1[u][y] == 'x':
                            check=False
                if check == True:
                    resultat.append([l,absi,ordo])
            except:
                continue
            else:
                continue
carre=[]
for i in range(len(resultat)):
    carre.append(resultat[i][0])
max_carre=max(carre)
for i in range(len(carre)):
    if carre[i]==max_carre:
        indice=i
        break
#print(resultat[indice])
########## remplacer carre par des o

long=resultat[indice][0]
absice=resultat[indice][1]
ordonne=resultat[indice][2]
for i in range(long):
    for j in range(long):
        tableau[ordonne+i][absice+j] = 'o'
for i in range(len(tableau)):
    for j in range(len(tableau[i])):
        print(tableau[i][j],end='')
    print('')

