#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:35:27 2022
@author: patry
"""
import sys 
import numpy as np

if len(sys.argv)!= 2:
    sys.exit('error')
####################################################################################
expression1 = sys.argv[1]

expression1 = expression1.split(' ')

expression1= ''.join(expression1)


def split(s):
    return [char for char in s]
expression = split(expression1)

for i in range(len(expression)):
    try : 
        expression[i] = int(expression[i])
    except:
        continue
    else: 
        continue
L= len(expression)
x = False
while x == False:
    x= True
    L= len(expression)
    for i in range(L-1):
        if type(expression[i]) == int and type(expression[i+1]) == int :
            expression[i] = str(expression[i])
            expression[i+1] = str(expression[i+1])
            expression[i]=''.join(expression[i:i+2])
            del expression[i+1]
            expression[i] = int(expression[i])
            
            x= False
            break

####################################################################################
# transforme l'argument en list avec les bon nombre et tout mamene



        
        
        


def calculation(expression):
    index_multiplication=[]
    for i in range(len(expression)):
        if expression[i]  == '*':
            index_multiplication.append((i))
    index_division=[]
    for i in range(len(expression)):
        if expression[i]  == '/':
            index_division.append((i))
    index_addition=[]
    for i in range(len(expression)):
        if expression[i]  == '+':
            index_addition.append((i))
    index_soustraction=[]
    for i in range(len(expression)):
        if expression[i]  == '-':
            index_soustraction.append((i))
    index_modulo=[]
    for i in range(len(expression)):
        if expression[i]  == '%':
            index_modulo.append((i))
    while len(expression)>1:
        while len(index_multiplication)>0 or len(index_division)>0 or len(index_modulo)>0:
            for element in expression:
                for i in range(len(expression)):
                    if expression[i] == element:
                        index=i
                        break
                if element == '*':
                    calcul = float(expression[index-1]) * float(expression[index+1])
                    expression = np.delete(expression,[index-1,index,index+1])
                    expression = np.insert(expression,index-1,calcul)
                    index_multiplication=[]
                    for i in range(len(expression)):
                        if expression[i]  == '*':
                            index_multiplication.append((i))
                    index_division=[]
                    for i in range(len(expression)):
                        if expression[i]  == '/':
                            index_division.append((i))
                    index_addition=[]
                    for i in range(len(expression)):
                        if expression[i]  == '+':
                            index_addition.append((i))
                    index_soustraction=[]
                    for i in range(len(expression)):
                        if expression[i]  == '-':
                            index_soustraction.append((i))
                    index_modulo=[]
                    for i in range(len(expression)):
                        if expression[i]  == '%':
                            index_modulo.append((i))
                    break
                elif element == '/':  
                    calcul = float(expression[index-1]) / float(expression[index+1])
                    expression = np.delete(expression,[index-1,index,index+1])
                    expression = np.insert(expression,index-1,calcul)
                    index_multiplication=[]
                    for i in range(len(expression)):
                        if expression[i]  == '*':
                            index_multiplication.append((i))
                    index_division=[]
                    for i in range(len(expression)):
                        if expression[i]  == '/':
                            index_division.append((i))
                    index_addition=[]
                    for i in range(len(expression)):
                        if expression[i]  == '+':
                            index_addition.append((i))
                    index_soustraction=[]
                    for i in range(len(expression)):
                        if expression[i]  == '-':
                            index_soustraction.append((i)) 
                    index_modulo=[]
                    for i in range(len(expression)):
                        if expression[i]  == '%':
                            index_modulo.append((i))
                    break
                elif element == '%':  
                    calcul = float(expression[index-1]) % float(expression[index+1])
                    expression = np.delete(expression,[index-1,index,index+1])
                    expression = np.insert(expression,index-1,calcul)
                    index_multiplication=[]
                    for i in range(len(expression)):
                        if expression[i]  == '*':
                            index_multiplication.append((i))
                    index_division=[]
                    for i in range(len(expression)):
                        if expression[i]  == '/':
                            index_division.append((i))
                    index_addition=[]
                    for i in range(len(expression)):
                        if expression[i]  == '+':
                            index_addition.append((i))
                    index_soustraction=[]
                    for i in range(len(expression)):
                        if expression[i]  == '-':
                            index_soustraction.append((i))
                    index_modulo=[]
                    for i in range(len(expression)):
                        if expression[i]  == '%':
                            index_modulo.append((i))
                    break
        while len(index_addition)>0 or len(index_soustraction)>0:
            for element in expression:
                for i in range(len(expression)):
                    if expression[i] == element:
                        index=i
                        break
                if expression[i] == '+':
                    calcul = float(expression[index-1]) + float(expression[index+1])
                    expression = np.delete(expression,[index-1,index,index+1])
                    expression = np.insert(expression,index-1,calcul)
                    index_multiplication=[]
                    for i in range(len(expression)):
                        if expression[i]  == '*':
                            index_multiplication.append((i))
                    index_division=[]
                    for i in range(len(expression)):
                        if expression[i]  == '/':
                            index_division.append((i))
                    index_addition=[]
                    for i in range(len(expression)):
                        if expression[i]  == '+':
                            index_addition.append((i))
                    index_soustraction=[]
                    for i in range(len(expression)):
                        if expression[i]  == '-':
                            index_soustraction.append((i))
                    index_modulo=[]
                    for i in range(len(expression)):
                        if expression[i]  == '%':
                            index_modulo.append((i))
                    break
                elif expression[i] == '-':  
                    calcul = float(expression[index-1]) - float(expression[index+1])
                    expression = np.delete(expression,[index-1,index,index+1])
                    expression = np.insert(expression,index-1,calcul)
                    index_multiplication=[]
                    for i in range(len(expression)):
                        if expression[i]  == '*':
                            index_multiplication.append((i))
                    index_division=[]
                    for i in range(len(expression)):
                        if expression[i]  == '/':
                            index_division.append((i))
                    index_addition=[]
                    for i in range(len(expression)):
                        if expression[i]  == '+':
                            index_addition.append((i))
                    index_soustraction=[]
                    for i in range(len(expression)):
                        if expression[i]  == '-':
                            index_soustraction.append((i))
                    index_modulo=[]
                    for i in range(len(expression)):
                        if expression[i]  == '%':
                            index_modulo.append((i))
                    break
                
            
    
    return float(expression[0])
    

index_parenthesis_open=[]
for i in range(len(expression)):
    if expression[i]  == '(':
        index_parenthesis_open.append((i))
        
index_parenthesis_close=[]
for i in range(len(expression)):
    if expression[i]  == ')':
        index_parenthesis_close.append((i))
if len(index_parenthesis_open)>0:
    for i in range(len(index_parenthesis_open)):
        
        expression2= expression[index_parenthesis_open[0]+1:index_parenthesis_close[0]]
        calcul = calculation(expression2)
        print(expression2)
        print(index_parenthesis_open[0])
        print(index_parenthesis_close[0])
        index_a_supp = np.arange(index_parenthesis_open[0],index_parenthesis_close[0]+1,1)
        print(index_a_supp)
        
        #del expression[index_parenthesis_open[0]:index_parenthesis_close[0]+1]
        expression = np.delete(expression,index_a_supp)
       
        expression = np.insert(expression,index_parenthesis_open[0],calcul)
        #expression.insert(index_parenthesis_open[0],calcul)
        index_parenthesis_open=[]
        for b in range(len(expression)):
            if expression[b]  == '(':
                index_parenthesis_open.append((b))
                
        index_parenthesis_close=[]
        for b in range(len(expression)):
            if expression[b]  == ')':
                index_parenthesis_close.append((b))
        print(expression)
        

expression = calculation(expression)
print(expression)
