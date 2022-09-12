#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:47:35 2022

@author: patry
"""
import sys 
def quick_sort(A,lo,hi):
    
    def partition(A,lo,hi):
        pivot=A[hi]
        
        i=lo-1
        for j in range(lo,hi):
            if A[j]<= pivot:
                i=i+1
                (A[i],A[j])=(A[j],A[i])
        i=i+1
        (A[i],A[hi])=(A[hi],A[i])
        return i
    if lo>=hi or lo <0:
        return
    p= partition(A, lo, hi)
    quick_sort(A, lo, p-1)
    quick_sort(A, p+1, hi)
    return A

l=len(sys.argv)
if l <3:
    sys.exit('error')
A=[]
try:
    for i in range(1,l):
        A.append(int(sys.argv[i]))
except:
    sys.exit('veuillez ne rentrer que des nombres')
else:
    quick_sort(A, 0,len(A)-1)
    for i in range(0,len(A)):
        print(A[i],end=' ')
    print('')
