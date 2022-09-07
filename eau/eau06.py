#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 23:06:49 2022

@author: patry
"""
import sys

if sys.argv.__len__() <3:
    sys.exit('error')
if sys.argv.__len__() >3:
    sys.exit('error')
resultat=sys.argv[1].find(sys.argv[2])

if resultat >0: 
    print('True')
if resultat == -1:
    print('False')
