#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:47:23 2022

@author: patry
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:35:27 2022
@author: patry
"""
import sys 
import numpy as np
##########
lines = open(sys.argv[1]).read().splitlines()
##########
def splits(s):
    return [char for char in s]
##########
for i in range(len(lines)):
    lines[i]=splits(lines[i])
##########
lines2 = open(sys.argv[2]).read().splitlines()
##########
def splits(s):
    return [char for char in s]
##########
for i in range(len(lines2)):
    lines2[i]=splits(lines2[i])
##########

L_lines= len(lines)
L= len(lines2)
range_i=L_lines-L
l=[]
for i in range(L):
    l.append(len(lines2[i]))
range_c=len(lines[0])-len(lines2[0])




for i in range(range_i+1):
    line= lines[i:L+i]
    for c in range(range_c+1):
        for b in range(len(line)):
            line[b] = lines[i+b][c:l[b]+c]
        
        x=0
        y=0
        for j in range(len(line)):
            for k in range(len(line[j])):
                if line[j][k]==lines2[j][k] or lines2[j][k]==' ':
                    x=x+1
            
            y=y+len(line[j])
        if x == y:
            print('Trouvé !')
            print('coordonées: ', c,',',i)
            for s in range(len(lines)):
                for y in range(len(lines[s])):
                    lines[s][y] = '-'
            for q in range(len(lines2)):
                for g in range(len(lines2)):
                    lines[i+q][c+g]=lines2[q][g]
                    if lines2[q][g]==' ':
                        lines[i+q][c+g]='-'
            for q in range(len(lines)):
                for g in range(len(lines[q])):
                    print(lines[q][g],end='')
                print('')
            sys.exit()
            
            
sys.exit('Introuvable')
