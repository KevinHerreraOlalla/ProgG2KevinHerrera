# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:17:34 2020

@author: User
"""
matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],
       [0,0,0,0,0,0],[0,0,0,0,0,0],
       [0,0,0,0,0,0]]
a=int(input("Ingrese filas: "))
b=int(input("Ingrese columnas: "))
for fila in range(0,a):
    for columna in range(0,b):
        print("Ingrese el valor de la posicion:",fila,columna)
        matrix[fila][columna]=int(input())
print("\n")
print(matrix,"\n")



