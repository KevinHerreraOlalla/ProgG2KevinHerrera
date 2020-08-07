# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:53:48 2020

@author: User
"""
cant=int(input("Cantidad de llantas: "))
Pu=int(input("Precio Unitario: "))
if cant>4:
    pre=Pu*cant
    des=pre*0.10
    total=pre-des
    print("Valor a pagar",total)

else:
      pre=Pu*cant
      print("Valor a pagar",pre)
    
    


