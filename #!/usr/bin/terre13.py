#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:42:07 2022

@author: patry
"""
import sys 

heure_et_minutes = sys.argv[1]

heure= int(heure_et_minutes[0:2])
minutes= int(heure_et_minutes[3:5])
PM_OU_AM = heure_et_minutes[5:7]
heure0= heure_et_minutes[0:2]
minutes0= heure_et_minutes[3:5]

if PM_OU_AM == 'AM' and heure==12:
    print('00:'+str(minutes0))
if PM_OU_AM =='AM' and heure<12:
    print(str(heure0)+':'+str(minutes0))
if PM_OU_AM =='PM' and heure==12:
    print(str(heure0)+':'+str(minutes0))
if PM_OU_AM == 'PM' and heure<12:
    heure=heure+12
    print(str(heure)+':'+str(minutes0))
