# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 19:46:40 2020

@author: User
"""

cal1=int(input("Ingrese su primera calificacion: "))
cal2=int(input("Ingrese su segunda calificacion: "))
cal3=int(input("Ingrese su tercera calificacion: "))
if cal1>cal2 and cal2>cal3:
    claf=cal1+cal2
    print("Su calificacion final es: ",claf)
else:
    claf=cal2+cal3
    print("Su calificacion final es: ",claf)
