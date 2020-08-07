# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:59:10 2020

@author: User
"""
while True:
    x=input("Ingrese un numero a contar ")
    if x=="q" or x=="quit":
        break
    x=int(x)
    y=1
    acu=0
    while True:
        print(y)
        acu+=y
        y=y+1
        prom=acu/y
        if y>x:
            break
    

print("La suma de los # es:",acu)
print("El promedio es",prom)
