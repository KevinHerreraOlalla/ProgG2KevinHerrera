# -*- coding: utf-8 -*-
"""
Editor de Spyder
type(8)
Este es un archivo temporal.
"""
espacio=" "
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
nacimiento=input("Ingrese su fecha de nacimiento: ")
edad=int(input("Ingrese su edad: "))
if edad>=1 and edad<=12:
    print("Aun es niño")
elif edad>=13 and edad<=18:
    print("Es adolescente")
elif edad>=19 and edad<=35:
    print("Es adulto")
elif edad>=36 and edad<=50:
    print("Es mayor de edad")
    
    

print("\n"*2)
print("Hola mi nombre es"+espacio+nombre+espacio+"y mi apellido"+espacio+apellido+espacio+"mi fecha de nacimiento es"+espacio
      +nacimiento+espacio+"y mi edad"+espacio,edad)