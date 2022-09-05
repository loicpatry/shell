#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 23:02:33 2022

@author: patry
"""
B=input()
alphabet  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
if B == 'a':
    b=1
if B == 'b':
    b=2
if B == 'c':
    b=3
for i in range(b,26) : 
    if i == 25 : 
        print('\n')
    else :     
        print(alphabet[i],end='')
    i= i+1 
