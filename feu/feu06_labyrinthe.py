#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:39:10 2022

@author: patry
"""
import sys 
import random
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
