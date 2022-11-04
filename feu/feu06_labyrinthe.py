#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:39:10 2022

@author: patry
"""
import sys 
import random
check =False
while check == False:
    check =True
    file = open("labyrinthe.txt","w+")
    
    height =int(sys.argv[1])
    width =int(sys.argv[2])
    chars =['*',' ','o','1','2']
    gates='$'
    entry = random.randint(0, width-4) +2
    entry2= random.randint(0, width-4) +2
    file.write(str(height))
    file.write('X')
    file.write(str(width))
    for i in range(len(chars)):
        file.write(str(chars[i]))
    file.write('\n')
    for i in range(height):
        for j in range(width):
            if i == 0 and j == entry:
                file.write(chars[3])
            elif i == height -1 and j == entry2:
                file.write(chars[4])
            elif 0<i<height-1 and 0<j<width - 1 and random.randint(0, 100) > 20:
                file.write(chars[1])
            else : 
                file.write(chars[0])
        file.write('\n')
    
    file=open("labyrinthe.txt",'r')
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
            x=i
    if mat[1][x]=='*':
        check=False
    long=len(mat)
    for i in range(len(mat[long-1])):
        if mat[long-1][i]==str(2):
            absi_2=i
    if mat[long-2][absi_2]=='*':
        check=False
