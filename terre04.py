#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 23:02:33 2022

@author: patry
"""
import sys 

B = sys.argv[1]
alphabet  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

b = alphabet.index(B)
for i in range(b,26) :
    print(alphabet[i],end='')
    i= i+1

