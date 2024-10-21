#!/usr/bin/env python3
from sys import exit

# script que muestra la solución del reto 6
# hecho por Elvin Vargas


while True:
    try:
        numero = int(input("Ingrese un número: "))
        if len(str(numero)) % 2 == 0:
            # Inicializar una variable para almacenar los pares de dígitos
            par_numero = 0
            # Inicializar una variable para almacenar la suma de los divisores propios menos 1
            oculto = 0
            # Iterar sobre cada par de dígitos del número
            for i  in range(0, len(str(numero)), 2): # inicializo un bucle for con $i en 0; se comprueba que el valor de $i es menor a la cantidad de caracteres de $numero y luego se le     suma 2 en cada interacción
                # Extraer dos dígitos a la vez
                par_numero = str(numero)[i:i+2]
                # dividendo pasa a tomar el valor de cada par de números
                dividendo = int(par_numero)
                print(dividendo, "este es dividendo en cada valor")
                # inicializo perfecto que guarda la suma de los divisores y se inicializa en cada iteracion
                perfecto = 0
                # inicializo divisor en 1 para en el proximo for sea menor que dividendo
                divisor = 1
                while divisor < dividendo: # este bucle comprueba que divisor sea menor al dividendo y si lo es le suma 1 en cada iteracion 
                    if dividendo % divisor == 0: # el if comprueba que el modulo del dividendo entre el divisor es 0 si lo es lo suma en la variamble prefecto
                        perfecto = perfecto + divisor
                        print(perfecto, "esto es prefecto")
                    divisor = divisor + 1
                    print(divisor, "divisor tiene este valor")
                oculto = oculto + perfecto - 1 # sumo en cada iteracion el valor de perfecto y le resto 1 
            # imprimo el valor del número oculto
            print("SU NÚMERO OCULTO ES: ")
            print(oculto)
            exit(0)
        else: 
            print(" el numero que ingrese deve tener digitos pares y ser pocitivo ")
    except ValueError:
        print(" el numero que ingrese deve tener digitos pares y ser pocitivo ")
        
