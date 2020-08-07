# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:32:07 2020

@author: User
"""
x=input("Ingrese un numero para contar: ")
x=int(x)
y=1
acu=0
while y<=x:
    print(y,end=" ")
    acu+=y
    y=y+1
print("La suma de los # es:",acu)
    

