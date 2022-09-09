#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 22:20:29 2022

@author: patry
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 21:59:10 2022

@author: patry
"""
import sys 

if len(sys.argv)!= 3:
    sys.exit('error')
string_a_couper=sys.argv[1]
string_separateur=sys.argv[2]
def separateur2(string_a_couper,string_separateur):
    
    string_a_suivre=[]
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
                
                string_a_suivre.append((stringprint))
                b=i+1
        stringprint="".join(string_split[b:])
        string_a_suivre.append((stringprint))
        return string_a_suivre
    separateur(string, Separateur)
    index= string_a_suivre.index(string_separateur)
    
    for i in range(0,index):
        print(string_a_suivre[i],end=' ')
    print(' ')
    for i in range(index+1,len(string_a_suivre)):
        print(string_a_suivre[i],end=' ')
    print(' ')
