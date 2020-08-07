# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:42:41 2020

@author: User
"""
print("contador inicial")
c1=int(input())
print("contador final")
c2=int(input())
if c2<c1:
    print("El contador final es menor que el inicial")
    c2=int(input())
tipo=int(input("impresora (1. B/N, 2. Color): "))
if tipo==1:
    im=c2-c1
    print("impresones:",im)
    cos=im*0.06
    print("Costo:","$",cos)
if tipo==2:
    im=c2-c1
    print("impresones:",im)
    cos=im*0.12
    print("Costo:","$",cos)
    
