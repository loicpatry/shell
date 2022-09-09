#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 21:59:10 2022

@author: patry
"""
import sys 

if len(sys.argv)!= 2:
    sys.exit('error')
Separateur=' '
string=sys.argv[1]
def separateur(string,Separateur):
    def split(s):
        return [char for char in s]
    
    string=sys.argv[1]
    string_split=split(string)
    L=len(string_split)
    b=0
    for i in range(0,L):
        if string_split[i]== str(Separateur):
            stringprint= "".join(string_split[b:i])
            
            print(stringprint)
            b=i+1
    stringprint="".join(string_split[b:])
    print(stringprint)
    
separateur(string, Separateur)
