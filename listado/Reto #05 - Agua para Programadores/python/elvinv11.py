#!/usr/bin/env python3
from sys import exit

# script hecho por Elvin Vargas

while True:
    try:
        n = int(input("Ingrese la cantidad de litros (N): ")) # se pide al usurio cantidad de litros y se guarda ens la variable $n
        if n >= 1 and n <= 10**12: # se comprueba que el valor de $n es mayor o igual que 1 y menor o igual a 10 elevado a la 12
                a = int(input("Ingrese el costo de la botella de 1 litro (A): ")) # se pide el costo y se guarda en la variable $a
                if a >= 1 and a <= 1000: # se comprueba que $a es entero, >= 1 y <= 1000
                    b = int(input("Ingrese el costo de la botella de 2 litros (B): ")) # se pide el costo de la bottella de 2 litros y guarda en $b
                    if b >= 1 and b <= 1000: # se verifica que $b es entero, >= 1 y <= 1000
                        if n % 2 == 0: # se comprueba que $n sea par para luego decidir si puede comprar botellas de 2 litros o de 1 litros
                            total_a = n * a # se multiplica litros por precio
                            total_b = n * b / 2 # se multiplica litros por precios y se divide entre 2 da la cantidad de dinero al comprar botellas de dos litros
                            if total_b <= total_a:  # comprueba si la cantidad de del precio de dos litros es menor que las de 1 litros
                                print(f"El costo mínimo para comprar {n} litro de agua es: {total_b}") # es la salida si el valor de las botellas de 2 litros de agua es menor 
                                exit(0)
                            else:
                                print(f"El costo mínimo para comprar {n} litro de agua es: {total_a}") # es la salida si el valor de las botellas de 1 litros de agua es menor y es un $n es par 
                                exit(0)
                        else:
                            print(f"El costo mínimo para comprar {n} litro de agua es: {n * a}") # es la salida si $n no es par el usuario deve comprar botellas de 1 litros porque no se pueden mesclar
                            exit(0)
                    else:
                        print(f"Estimado el valor deve ser un entero >= 1 y <= 1000")
                else:
                    print(f"Estimado el valor deve ser un entero >= 1 y <= 1000")
        else:
                print(f"Estimado el valor deve ser un entero >= 1 y <= 1000000000000 , es decir menor a un billón.")
    except ValueError:
        print(f"deves introducir un número entero")

