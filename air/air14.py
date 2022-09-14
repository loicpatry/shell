#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:15:11 2022

@author: patry
"""
import sys
import filecmp
import colorama
from colorama import Fore
import os 

#######################################################################
def air01_try1 (string,Separateur,essai1):
    f=open('air01_try1.txt','x')
    f1=open('air01_try1_test.txt','x')


    #if len(sys.argv)!= 2:
        #sys.exit('error')
    #Separateur=' '
    #string=sys.argv[1]
    def separateur(string,Separateur):
        def split(s):
            return [char for char in s]
        
        
        string_split=split(string)
        L=len(string_split)
        b=0
        for i in range(0,L):
            if string_split[i]== str(Separateur):
                stringprint= "".join(string_split[b:i])
                
                f.write(stringprint)
                b=i+1
        stringprint="".join(string_split[b:])
        f.write(stringprint)
        
    separateur(string, Separateur)
    f1.write('bonjour')
    f1.write('les')
    f1.write('gars')
    x= filecmp.cmp('air01_try1.txt', 'air01_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air01 (1/1) : success')
        essai1=1
    if x == False:
        print(Fore.RED + 'air01 (1/1) : failure')
        essai1=0
    os.remove('air01_try1.txt')
    os.remove('air01_try1_test.txt')
    
    return essai1
        
def air02_try1(string_a_couper,string_separateur,essai2):
    f=open('air02_try1.txt','x')
    f1=open('air02_try1_test.txt','x')
    #string_a_couper=sys.argv[1]
    #string_separateur=sys.argv[2]
    def separateur2(string_a_couper,string_separateur):
        
        string_a_suivre=[]
        Separateur=' '
        string=string_a_couper
        def separateur(string,Separateur):
            def split(s):
                return [char for char in s]
            
            
            string_split=split(string)
            L=len(string_split)
            b=0
            for i in range(0,L):
                if string_split[i]== str(Separateur):
                    stringprint= "".join(string_split[b:i])
                    
                    string_a_suivre.append((stringprint))
                    b=i+1
            stringprint="".join(string_split[b:])
            string_a_suivre.append((stringprint))
            return string_a_suivre
        separateur(string, Separateur)
        try:
            index= string_a_suivre.index(string_separateur)
        except:
            sys.exit('separateur pas dans la liste')
        else:
        
            for i in range(0,index):
                
                f.write(string_a_suivre[i])
            for i in range(index+1,len(string_a_suivre)):
                
                f.write(string_a_suivre[i])
        
        
    
    separateur2(string_a_couper,string_separateur)
    f1.write('Crevette magique dans')
    f1.write('mer des étoiles')
    x= filecmp.cmp('air02_try1.txt', 'air02_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air02 (1/1) : success')
        essai2=1
    if x == False:
        print(Fore.RED + 'air02 (1/1) : failure')
        essai2=0
    os.remove('air02_try1.txt')
    os.remove('air02_try1_test.txt')
    return essai2    
    
    
def air03_try1(tableau_arg,separateur,essai3):
    f=open('air03_try1.txt','x')
    f1=open('air03_try1_test.txt','x')
    #tableau_arg=[]
    #for i in range(1,len(sys.argv)-1):
        #tableau_arg.append(sys.argv[i])
    #separateur = sys.argv[len(sys.argv)-1]
    def concat (tableau_arg,separateur):
        for i in range(0,len(tableau_arg)):
            f.write(tableau_arg[i])
            f.write(separateur)
        
    concat(tableau_arg,separateur)
    f1.write('je teste des trucs')
    x= filecmp.cmp('air03_try1.txt', 'air03_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air03 (1/1) : success')
        essai3=1
    if x == False:
        print(Fore.RED + 'air03 (1/1) : failure')
        essai3=0
    os.remove('air03_try1.txt')
    os.remove('air03_try1_test.txt')   
    return essai3

def air04_try1(liste_arg,essai4_1):
    f=open('air04_try1.txt','x')
    f1=open('air04_try1_test.txt','x')
    
    for i in range(0,len(liste_arg)):
        liste_arg_ref=[]
        for i in range(len(liste_arg)):
            liste_arg_ref.append(liste_arg[i])
            
        liste_arg.remove(liste_arg[i])
    
        if liste_arg_ref[i] in liste_arg:
            continue
        else:
            f.write(str(liste_arg_ref[i]))
    f1.write('5')
    x= filecmp.cmp('air04_try1.txt', 'air04_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air04 (1/2) : success')
        essai4_1=1
    if x == False:
        print(Fore.RED + 'air04 (1/2) : failure')
        essai4_1=0
    os.remove('air04_try1.txt')
    os.remove('air04_try1_test.txt') 
    return essai4_1
    
def air04_try2(liste_arg,essai4_2):
    f=open('air04_try2.txt','x')
    f1=open('air04_try2_test.txt','x')
    
    for i in range(0,len(liste_arg)):
        liste_arg_ref=[]
        for i in range(len(liste_arg)):
            liste_arg_ref.append(liste_arg[i])
            
        liste_arg.remove(liste_arg[i])
    
        if liste_arg_ref[i] in liste_arg:
            continue
        else:
            f.write(str(liste_arg_ref[i]))
    f1.write('5')
    x= filecmp.cmp('air04_try2.txt', 'air04_try2_test.txt')
    if x == True :
        print(Fore.GREEN +'air04 (2/2) : success')
        essai4_2=1
    if x == False:
        print(Fore.RED + 'air04 (2/2) : failure')
        essai4_2=0
    os.remove('air04_try2.txt')
    os.remove('air04_try2_test.txt') 
    return essai4_2
    
    
def air05_try1(chaine,essai5):
    f=open('air05_try1.txt','x')
    f1=open('air05_try1_test.txt','x')
    def split(s):
        return [char for char in s]
    arguments= split(chaine)
    index=[]
    for i in range(0,len(arguments)-1):
        if arguments[i] == arguments[i+1]:
            index.append(i)
    
    
    for element in index:   
        #print(element)
        arguments.pop(element)
        for i in range(0,len(index)):
            index[i]=index[i]-1
        
    
    
    arguments2= ''.join(arguments)
    f.write(arguments2)
    f1.write('Helo milady, bien ou quoi ?')
    x= filecmp.cmp('air05_try1.txt', 'air05_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air05 (1/1) : success')
        essai5=1
    if x == False:
        print(Fore.RED + 'air05 (1/1) : failure')
        essai5=0
    os.remove('air05_try1.txt')
    os.remove('air05_try1_test.txt') 
    return essai5
def air06_try1(variable,operation,number,essai6_1):
    f=open('air06_try1.txt','x')
    f1=open('air06_try1_test.txt','x')
    if operation== '+':
        for i in range(0,len(variable)):
            variable[i]= variable[i] + number
    if operation== '-':
        for i in range(0,len(variable)):
            variable[i]= variable[i] - number
    if operation== '*':
        for i in range(0,len(variable)):
            variable[i]= variable[i] * number
    if operation== '/':
        for i in range(0,len(variable)):
            variable[i]= variable[i] / number
            
    for i in range(0,len(variable)):
        f.write(str(variable[i]))
    f1.write('34567')
    x= filecmp.cmp('air06_try1.txt', 'air06_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air06 (1/2) : success')
        essai6_1=1
    if x == False:
        print(Fore.RED + 'air06 (1/2) : failure')
        essai6_1=0
    os.remove('air06_try1.txt')
    os.remove('air06_try1_test.txt') 
    return essai6_1
    
def air06_try2(variable,operation,number,essai6_2):
    f=open('air06_try2.txt','x')
    f1=open('air06_try2_test.txt','x')
    if operation== '+':
        for i in range(0,len(variable)):
            variable[i]= variable[i] + number
    if operation== '-':
        for i in range(0,len(variable)):
            variable[i]= variable[i] - number
    if operation== '*':
        for i in range(0,len(variable)):
            variable[i]= variable[i] * number
    if operation== '/':
        for i in range(0,len(variable)):
            variable[i]= variable[i] / number
            
    for i in range(0,len(variable)):
        f.write(str(variable[i]))
    f1.write('56715')
    x= filecmp.cmp('air06_try2.txt', 'air06_try2_test.txt')
    if x == True :
        print(Fore.GREEN +'air06 (2/2) : success')
        essai6_2=1
    if x == False:
        print(Fore.RED + 'air06 (2/2) : failure')
        essai6_2=0
    os.remove('air06_try2.txt')
    os.remove('air06_try2_test.txt') 
    return essai6_2
    
    
def air07_try1(array_de_string,string,essai7_1):
    f=open('air07_try1.txt','x')
    f1=open('air07_try1_test.txt','x')
    def ma_fonction(array_de_string,string):
        index=[]
        for i in range(0,len(array_de_string)):
            if string in array_de_string[i] or string.upper() in array_de_string[i]:
                index.append(i)
        for element in index:
            array_de_string.pop(element)
            for i in range(0,len(index)):
                index[i]=index[i]-1
                
        return array_de_string
    ma_fonction(array_de_string, string)

    for i in range(0,len(array_de_string)):
        f.write(array_de_string[i])
    f1.write('Michel')
    x= filecmp.cmp('air07_try1.txt', 'air07_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air07 (1/2) : success')
        essai7_1=1
    if x == False:
        print(Fore.RED + 'air07 (1/2) : failure')
        essai7_1=0
    os.remove('air07_try1.txt')
    os.remove('air07_try1_test.txt') 
    return essai7_1
    
def air07_try2(array_de_string,string,essai7_2):
    f=open('air07_try2.txt','x')
    f1=open('air07_try2_test.txt','x')
    def ma_fonction(array_de_string,string):
        index=[]
        for i in range(0,len(array_de_string)):
            if string in array_de_string[i] or string.upper() in array_de_string[i]:
                index.append(i)
        for element in index:
            array_de_string.pop(element)
            for i in range(0,len(index)):
                index[i]=index[i]-1
                
        return array_de_string
    ma_fonction(array_de_string, string)

    for i in range(0,len(array_de_string)):
        f.write(array_de_string[i])
    f1.write('MichelThérèseBenoit')
    x= filecmp.cmp('air07_try2.txt', 'air07_try2_test.txt')
    if x == True :
        print(Fore.GREEN +'air07 (2/2) : success')
        essai7_2=1
    if x == False:
        print(Fore.RED + 'air07 (2/2) : failure')
        essai7_2=0
    os.remove('air07_try2.txt')
    os.remove('air07_try2_test.txt') 
    return essai7_2
    
def air08_try1(array,new_element,essai8_1):
    f=open('air08_try1.txt','x')
    f1=open('air08_try1_test.txt','x')
    ########################################################################
    def tri_selectif(mon_tableau): 
            l= len(mon_tableau)
            for i in range(0,l-1):
                mini=i
                for j in range(i+1,l):
                    if mon_tableau[j]<mon_tableau[mini]:
                        mini=j
                if mini != i:
                    (mon_tableau[i],mon_tableau[mini])=(mon_tableau[mini],mon_tableau[i])
            return(mon_tableau)
        
    ########################################################################
    
    def sorted_insert(array, new_element):
        
        array.append(new_element)
        
        tri_selectif(array)
        for i in range(0,len(array)):
            f.write(str(array[i]))
        
    ########################################################################
    sorted_insert(array, new_element)
    f1.write('1234')
    x= filecmp.cmp('air08_try1.txt', 'air08_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air08 (1/2) : success')
        essai8_1=1
    if x == False:
        print(Fore.RED + 'air08 (1/2) : failure')
        essai8_1=0
    os.remove('air08_try1.txt')
    os.remove('air08_try1_test.txt') 
    return essai8_1

def air08_try2(array,new_element,essai8_2):
    f=open('air08_try2.txt','x')
    f1=open('air08_try2_test.txt','x')
    ########################################################################
    def tri_selectif(mon_tableau): 
            l= len(mon_tableau)
            for i in range(0,l-1):
                mini=i
                for j in range(i+1,l):
                    if mon_tableau[j]<mon_tableau[mini]:
                        mini=j
                if mini != i:
                    (mon_tableau[i],mon_tableau[mini])=(mon_tableau[mini],mon_tableau[i])
            return(mon_tableau)
        
    ########################################################################
    
    def sorted_insert(array, new_element):
        
        array.append(new_element)
        
        tri_selectif(array)
        for i in range(0,len(array)):
            f.write(str(array[i]))
        
    ########################################################################
    sorted_insert(array, new_element)
    f1.write('102030334050607090')
    x= filecmp.cmp('air08_try2.txt', 'air08_try2_test.txt')
    if x == True :
        print(Fore.GREEN +'air08 (2/2) : success')
        essai8_2=1
    if x == False:
        print(Fore.RED + 'air08 (2/2) : failure')
        essai8_2=0
    os.remove('air08_try2.txt')
    os.remove('air08_try2_test.txt') 
    return essai8_2
    
    
def air09_try1(array,essai9):
    f=open('air09_try1.txt','x')
    f1=open('air09_try1_test.txt','x')
    
    def tri_selectif(mon_tableau): 
        l= len(mon_tableau)
        for i in range(0,l-1):
            mini=i
            for j in range(i+1,l):
                if mon_tableau[j]<mon_tableau[mini]:
                    mini=j
            if mini != i:
                (mon_tableau[i],mon_tableau[mini])=(mon_tableau[mini],mon_tableau[i])
        return(mon_tableau)
    
    ########################################################################
    
    def sorted_fusion (array1,array2):
        for i in range(0,len(array2)):
            array1.append(array2[i])
        tri_selectif(array1)
        for i in range(0,len(array1)):
            f.write(str(array1[i]))
        
    
    ########################################################################
    
    l = len(array)
    
        
    array1=[]
    array2=[]
    
   
    for i in range(0,l):
        index=[]
        if array[i]== 'fusion':
            index.append(i)
            break
        
        array1.append(int(array[i]))
    
    for i in range(index[0]+1,l):
        array2.append(int(array[i]))
            
    
        
    sorted_fusion(array1, array2)
    f1.write('101520253035')
    x= filecmp.cmp('air09_try1.txt', 'air09_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air09 (1/1) : success')
        essai9=1
    if x == False:
        print(Fore.RED + 'air09 (1/1) : failure')
        essai9=0
    os.remove('air09_try1.txt')
    os.remove('air09_try1_test.txt') 
    return essai9
    
def air10_try1(array,essai10):
    f=open('air10_try1.txt','x')
    f1=open('air10_try1_test.txt','x')
    def ma_rotation (array):
        
        rotation=[]
        for i in range(1,len(array)):
            rotation.append(array[i])
        rotation.append(array[0])
        for i in range(len(rotation)):
            array[i]=rotation[i]
        
        
        return array
        
    
    ma_rotation(array)
    
    for i in range(len(array)):
        f.write(array[i])
    f1.write('AlbertThérèseBenoitMichel')
    x= filecmp.cmp('air10_try1.txt', 'air10_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air10 (1/1) : success')
        essai10=1
    if x == False:
        print(Fore.RED + 'air10 (1/1) : failure')
        essai10=0
    os.remove('air10_try1.txt')
    os.remove('air10_try1_test.txt') 
    return essai10
    
def air11_try1(essai11):
    f=open('a.txt','r')
    f1=open('air11_try1_test.txt','x')
    f1.write('Je danse le mia')
    f1.close()
    f1=open('air11_try1_test.txt','r')
    
    if f.read() == f1.read():
        print(Fore.GREEN +'air11 (1/1) : success')
        essai11=1
    else:
        print(Fore.RED + 'air11 (1/1) : failure')
        essai11=0
    os.remove('air11_try1_test.txt')
    return essai11

def air12_try1(caractere,nombre_etage,essai_12):
    f=open('air12_try1.txt','x')
    f1=open('air12_try1_test.txt','x')
    
    tableau=[]
    for i in range(nombre_etage):
        tableau.append([])
        for a in range(0,(nombre_etage*2)-1):
            tableau[i].append(caractere)
        
    
            
    for i in range(len(tableau)):
        for a in range(0,nombre_etage-1-i):
            tableau[i][a]=' '
        for a in range(nombre_etage+i,len(tableau[i])):
            tableau[i][a]=' '
        tableau[i]= ''.join(tableau[i])
        f.write(tableau[i])
    f1.write('    O    ')
    f1.write('   OOO   ')
    f1.write('  OOOOO  ')
    f1.write(' 0000000 ')
    f1.write('OOOOOOOOO')
    x= filecmp.cmp('air12_try1.txt', 'air12_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air12 (1/1) : success')
        essai_12=1
    if x == False:
        print(Fore.RED + 'air12 (1/1) : failure')
        essai_12=0
    os.remove('air12_try1.txt')
    os.remove('air12_try1_test.txt') 
    return essai_12
    
def air13_try1(A,essai_13):
    f=open('air13_try1.txt','x')
    f1=open('air13_try1_test.txt','x')
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

    quick_sort(A, 0,len(A)-1)
    for i in range(0,len(A)):
        f.write(str(A[i]))
    f1.write('123456')
    x= filecmp.cmp('air13_try1.txt', 'air13_try1_test.txt')
    if x == True :
        print(Fore.GREEN +'air13 (1/1) : success')
        essai_13=1
    if x == False:
        print(Fore.RED + 'air13 (1/1) : failure')
        essai_13=0
    os.remove('air13_try1.txt')
    os.remove('air13_try1_test.txt') 
    return essai_13

    
    
        
    
    
    
    
    
    
    










######################################################################
try : 
    f1=open('air01.py','r')
    f2=open('air02.py','r')
    f3=open('air03.py','r')
    f4=open('air04.py','r')
    f5=open('air05.py','r')
    f6=open('air06.py','r')
    f7=open('air07.py','r')
    f8=open('air08.py','r')
    f9=open('air09.py','r')
    f10=open('air10.py','r')
    f11=open('air11.py','r')
    f12=open('air12.py','r')
    f13=open('air13.py','r')
except:
    sys.exit('error')
else: 
    essai1=1
    essai2=1
    essai3=1
    essai4_1=1
    essai10=1
    essai11=1
    essai4_2=1
    essai5=1
    essai6_1=1
    essai6_2=1
    essai7_1=1
    essai7_2=1
    essai8_1=1
    essai8_2=1
    essai9=1
    essai_12=1
    essai_13=1
    
    string='bonjour les gars'
    Separateur=' '
    air01_try1(string, Separateur,essai1)
    print('#####################')
    string_a_couper='Crevette magique dans la mer des étoiles'
    string_separateur='la'
    air02_try1(string_a_couper, string_separateur,essai2)
    print('#####################')
    tableau_arg=['je','teste','des','trucs']
    separateur=' '
    air03_try1(tableau_arg, separateur,essai3)
    print('#####################')
    liste_arg=[1,2,3,4,5,4,3,2,1]
    air04_try1(liste_arg,essai4_1)
    liste_arg=['bonjour','monsieur','bonjour']
    air04_try2(liste_arg,essai4_2)
    print('#####################')
    chaine='Hello milady,   bien ou quoi ??'
    air05_try1(chaine,essai5)
    print('#####################')
    variable=[1,2,3,4,5]
    operation='+'
    number=2
    air06_try1(variable, operation, number,essai6_1)
    variable=[10,11,12,20]
    operation='-'
    number=5
    air06_try2(variable, operation, number,essai6_2)
    print('#####################')
    array_de_string=['Michel','Albert','Thérèse','Benoit']
    string='t'
    air07_try1(array_de_string, string,essai7_1)    
    string='a'
    air07_try2(array_de_string, string,essai7_2)
    print('#####################')
    array=[1,3,4]
    new_element=2
    air08_try1(array, new_element,essai8_1)
    array=[10,20,30,40,50,60,70,90]
    new_element=33
    air08_try2(array, new_element,essai8_2)
    print('#####################')
    array=[10,20,30,'fusion',15,25,35]
    air09_try1(array,essai9)
    print('#####################')
    array=['Michel','Albert','Thérèse','Benoit']
    air10_try1(array,essai10)
    print('#####################')
    air11_try1(essai11)
    print('#####################')
    caractere='O'
    nombre_etage=5
    air12_try1(caractere, nombre_etage,essai_12)
    print('#####################')
    A=[6,5,4,3,2,1]
    air13_try1(A,essai_13)
    print('#####################')
    print('')
    resultattotal = essai1 + essai2 + essai3 + essai4_1 + essai4_2 + essai5 + essai6_1 + essai6_2 + essai7_1 + essai7_2+ essai8_1 + essai8_2 + essai9 + essai10 + essai11 + essai_12 + essai_13 
    print('Total success : ('+str(resultattotal)+'/17)')
    
    
    
    
