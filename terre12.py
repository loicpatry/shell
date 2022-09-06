#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 20:21:45 2022

@author: patry
"""
import sys 

heure_et_minutes = sys.argv[1]

heure= int(heure_et_minutes[0:2])
minutes= int(heure_et_minutes[3:5])
heure0= heure_et_minutes[0:2]
minutes0= heure_et_minutes[3:5]

if  0<heure<12:
    print(str(heure0)+':'+str(minutes0)+'AM')        
elif heure==12:
    print(str(heure0)+':'+str(minutes0)+'PM')
elif 12< heure < 24:
    heure=heure-12
    print(str(heure)+':'+str(minutes0)+'PM')
else : 
    print('12:00AM')
    
