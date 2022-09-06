#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 23:02:33 2022
@author: patry
"""

alphabet  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,27) : 
    if i == 26 : 
        print('')
    else :     
        print(alphabet[i],end='')
    i= i+1 
