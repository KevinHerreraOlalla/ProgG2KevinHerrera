# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 19:01:40 2020

@author: User
"""
hor=int(input("Horas trabajadas: "))
ta=int(input("Tarifa por hora: "))
if hor>40:
    tra=hor*ta
    hor2=hor-40
    des=hor2*ta
    bono=des*0.50
    total=tra+bono
    print("Descuento 40")
    print("Valor a pagar: ",total)
else:
     tra=hor*ta
     print("Valor a pagar: ",tra)
    

