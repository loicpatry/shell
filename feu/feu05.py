

import random 
import sys 
import numpy as np


if len(sys.argv) != 2:
    sys.exit('error')
try: 
    file=open(sys.argv[1],'r')
except:
    sys.exit('error')
else:
    tab=file.readlines()
    tableau=[]
    for i in range(len(tab)-1):
        tableau.append(tab[i+1])
    
    def split(s):
        return [char for char in s]
    for i in range(len(tableau)):
        tableau[i]=split(tableau[i])
    
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if j==len(tableau[i])-1:
                del tableau[i][j]
    if len(tableau)<len(tableau[0]):
        l_carre_max=len(tableau)
    if len(tableau)>len(tableau[0]):
        l_carre_max=len(tableau[0])
    if len(tableau)==len(tableau[0]):
        l_carre_max=len(tableau)
    resultat=[]
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
                            if tableau1[u][y] == tab[0][2]:
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
            tableau[ordonne+i][absice+j] = tab[0][3]
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            print(tableau[i][j],end='')
        print('')
