#!/usr/bin/env python3
# script hecho por Elvin Vargas
# es la respuesta al reto 03 de adivina el número 

from random import randint
from sys import exit

numero = randint(0, 100)
respuesta=101
contador=0
print("Bienvenido a Adivina el número")
print()
print("Tendrás 6 intentos para adivinar el número que he pensado.")
print("Solo te diré que está  del 0 al 100.")
print()
while numero != respuesta :
    contador = contador + 1
    if contador > 6: 
        print("Intentos agotados")
        print(f"El número era {numero}")
        exit(0)
    else:
        try:
            respuesta = int(input("¿Cual es el numero? del 0 al 100: "))
            print(f"Numero de intentos {contador} de 6.")
            if numero < respuesta:
                print(f"El número es menor a {respuesta}")
            elif numero > respuesta:
                print(f"El número es mayor a {respuesta}")
        except ValueError:
            print("eso no es un número entero")

print(f"¡Has ganado! el número es {numero}.")
