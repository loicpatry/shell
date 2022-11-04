#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:49:48 2022

@author: patry
"""
import sys
import time
import random
from collections import deque
possibilite_final=[]
chemin_final=[]
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
if len(sys.argv)!= 2:
    sys.exit('error')
def isValid(mat, visited, row, col):
    return (row >= 0) and (row < len(mat)) and (col >= 0) and (col < len(mat[0])) \
           and mat[row][col] == ' ' and not visited[row][col]

def findShortestPathLength(mat, src, dest):
 
    # obtenir la cellule source (i, j)
    i, j = src
 
    # obtenir la cellule de destination (x, y)
    x, y = dest
 
    # Cas de base : entrée invalide
    if not mat or len(mat) == 0 or mat[i][j] == '*' or mat[x][y] == '*':
        return -1
 
    # Matrice `M × N`
    (M, N) = (len(mat), len(mat[0]))
 
    # construit une matrice pour garder une trace des cellules visitées
    visited = [[False for x in range(N)] for y in range(M)]
 
    # créer une Queue vide
    q = deque()
 
    # marque la cellule source comme visitée et met en file d'attente le nœud source
    visited[i][j] = True
    
    # (i, j, dist) représente les coordonnées des cellules de la matrice, et leur
    # distance minimale de la source
    q.append((i, j, 0))
 
    # stocke la longueur du chemin le plus long de la source à la destination
    min_dist = sys.maxsize
    
    # Boucle # jusqu'à ce que la Queue soit vide
    while q:
 
        # retirer de la file d'attente le nœud frontal et le traiter
        (i, j, dist) = q.popleft()
 
        # (i, j) représente une cellule courante, et `dist` stocke sa
        # distance minimale de la source
        
        possibilite_final.append([i,j,dist])
        # si la destination est trouvée, mettre à jour `min_dist` et arrêter
        if i == x and j == y:
            min_dist = dist
            
            break
        
        # vérifie les quatre mouvements possibles à partir de la cellule actuelle
        # et mettre en file d'attente chaque mouvement valide
        for k in range(4):
            # vérifier s'il est possible d'aller en position
            # (i + row[k], j + col[k]) à partir de la position actuelle
            if isValid(mat, visited, i + row[k], j + col[k]):
                
                # marque la cellule suivante comme visitée et la met en file d'attente
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))
                #print(i,j)
                #print(q)
    
    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1


try:
    
    file=open(sys.argv[1],'r')
except:
    sys.exit('error')
else:
    

    mat=file.readlines()
    
    
    del mat[0]
    
    def split(s):
        return [char for char in s]
    for i in range(len(mat)):
        mat[i]=split(mat[i])
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if j == len(mat[i])-1:
                del mat[i][j]
    
    for i in range(len(mat[0])):
        if mat[0][i]==str(1):
            src=(0,i)
    long=len(mat)
    for i in range(len(mat[long-1])):
        if mat[long-1][i]==str(2):
            absi_2=i
            dest=(long-1,i)
            mat[long-1][i]=' '
    
    
    min_dist = findShortestPathLength(mat, src, dest)
    
    if min_dist != -1:
        print("Sortie atteinte en ", min_dist,'coup')
    else:
        sys.exit('labyrinthe inresoluble, relancer le createur de labyrinthe')
    
    L=len(possibilite_final)
    y=possibilite_final[L-1][0]
    x=possibilite_final[L-1][1]
    dist=possibilite_final[L-1][2]
    chemin_final.append([y,x,dist])
    
    while len(chemin_final) != min_dist+1: 
    
        chemin_final=[]
        L=len(possibilite_final)
        y=possibilite_final[L-1][0]
        x=possibilite_final[L-1][1]
        dist=possibilite_final[L-1][2]
        chemin_final.append([y,x,dist])
       
        j=0
        for x in range(13):
            
            possibilite=[]
            for i in possibilite_final:
                
                
                
                if i[2] == chemin_final[j][2] -1:
                    
                    if ((i[0] == chemin_final[j][0]+1 or i[0] == chemin_final[j][0]-1) and i[1]==chemin_final[j][1]) or ((i[1] == chemin_final[j][1]+1 or i[1] == chemin_final[j][1]-1) and i[0]==chemin_final[j][0]):
                        possibilite.append(i)
                
            if len(possibilite)>1:
                chemin_final.append(random.choice(possibilite))
            elif len(possibilite)==0:
                break
            else:
                chemin_final.append(possibilite[0])
            
            
            j=j+1
            
                    
    
    L=len(chemin_final)
    del chemin_final[L-1]
    del chemin_final[0]     
    mat[long-1][absi_2]='2'    
    for i in chemin_final:
        y=i[0]
        x=i[1]
        mat[y][x]='o'
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j],end='')
        print('')
    
        


    
    
