#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:35:27 2022

@author: patry
"""
import sys 
import numpy as np
##########
lines = open('board.txt').read().splitlines()
##########
def splits(s):
    return [char for char in s]
##########
for i in range(len(lines)):
    lines[i]=splits(lines[i])
##########
lines2 = open('to_find.txt').read().splitlines()
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
        print(line)
        if x == y:
            print('success')
                
        
