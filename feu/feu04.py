#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:44:34 2022

@author: patry
"""
import random
r=0
import sys

while r ==0:
    
    lines = open(sys.argv[1]).read().splitlines()
    
    
    def split(s):
        return [char for char in s]
   
   # for j in range(len(lines[0])):
        #count=[]
        #x=0
        #for i in range(len(lines)):
            #if lines[i][j] == '.':
                #count.append(i)
            #else:
                #x=x+i
        #if len(count) == 1:
            #lines[i][j] = 45 - x
        
        
        
    for i in range(len(lines)):
        lines[i]= split(lines[i])
    for j in range(len(lines)):
        count=[]
        x=0
        for i in range(len(lines[j])):
            if lines[j][i] == '.':
                count.append(i)
            else:
                lines[j][i] = int(lines[j][i])
                x=x+lines[j][i]
        
        if len(count) == 1:
            lines[j][count[0]] = int(45 - x)
    for j in range(len(lines)):
        count=[]
        x=0
        for i in range(len(lines[j])):
            if lines[i][j] == '.':
                count.append(i)
            else:
                lines[i][j] = int(lines[i][j])
                x=x+lines[i][j]
        
        if len(count) == 1:
            lines[count[0]][j] = int(45 - x)
            
   
    lines2=lines
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '.':
                lines[i][j] = random.randint(1,10)
            else: 
                lines[i][j] = int(lines[i][j])
    resultat_ligne=[]
    for i in range(len(lines)):
        x=0
        for j in range(len(lines[i])):
            x = x+ lines[i][j]
        resultat_ligne.append(x)
    resultat_colonne=[]
    for i in range(len(lines)):
        x=0
        for j in range(len(lines)):
            x = x +lines[j][i]
        resultat_colonne.append(x)
    x=0
    
    for i in range(3):
        for j in range(3):
            x= x+ lines[i][j]
    resultat_bloc1 =x
    x=0
    
    for i in range(3,6):
        for j in range(3):
            x= x+ lines[i][j]
    resultat_bloc2 =x
    x=0
    
    for i in range(6,9):
        for j in range(3):
            x= x+ lines[i][j]
    resultat_bloc3 =x
    x=0
    
    for i in range(3):
        for j in range(3,6):
            x= x+ lines[i][j]
    resultat_bloc4 =x
    x=0
    
    for i in range(3):
        for j in range(6,9):
            x= x+ lines[i][j]
    resultat_bloc5 =x
    x=0
    
    for i in range(6,9):
        for j in range(6,9):
            x= x+ lines[i][j]
    resultat_bloc6 =x
    x=0
    
    for i in range(3,6):
        for j in range(6,9):
            x= x+ lines[i][j]
    resultat_bloc7 =x
    x=0
    
    for i in range(3,6):
        for j in range(3,6):
            x= x+ lines[i][j]
    resultat_bloc8 =x
    x=0
    
    for i in range(6,9):
        for j in range(3,6):
            x= x+ lines[i][j]
    resultat_bloc9 =x
    
    if resultat_ligne[0] == 45:
        if resultat_ligne[1] == 45:
            if resultat_ligne[2] == 45:
                if resultat_ligne[3] == 45:
                    if resultat_ligne[4] == 45:
                        if resultat_ligne[5] == 45:
                            if resultat_ligne[6] == 45:
                                if resultat_ligne[7] == 45:
                                    if resultat_ligne[8] == 45:
                                        if resultat_colonne[0] == 45:
                                            if resultat_colonne[1] == 45:
                                                if resultat_colonne[2] == 45:
                                                    if resultat_colonne[3] == 45:
                                                        if resultat_colonne[4] == 45:
                                                            if resultat_colonne[5] == 45:
                                                                if resultat_colonne[6] == 45:
                                                                    if resultat_colonne[7] == 45:
                                                                        if resultat_colonne[8] == 45:
                                                                            if resultat_bloc1 == 45:
                                                                                if resultat_bloc2 == 45:
                                                                                    if resultat_bloc3 == 45:
                                                                                        if resultat_bloc4 == 45:
                                                                                            if resultat_bloc5 == 45:
                                                                                                if resultat_bloc6 == 45:
                                                                                                    if resultat_bloc7 == 45:
                                                                                                        if resultat_bloc8 == 45:
                                                                                                            if resultat_bloc9 == 45:
                                                                                                                r= 1
                                                                                                                for i in range(len(lines)):
                                                                                                                    for j in range(len(lines[i])):
                                                                                                                        print(lines[i][j],end='')
                                                                                                                    print('')
                                                                                                                

    
                                                                                                         
    
            


        
    
