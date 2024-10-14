#!/usr/bin/env python3


# script hecho por Elvin Vargas
# finalidad resolber el reto del reciclage 

# inicializo las variables
dinero = 20
helado = 0
tarrina = 0

while True:
    # la linea anterior inicia el bucle while   
    print("¿Cuánto vale un helado? 2")
    print("¿Cuánto me devuelven por una tarrina? 1")
    print(f"¿Cuánto dinero tengo? {dinero}")
    if dinero < 2 and tarrina == 0: # compruebo que dinero mayor que 2 y tarrina seha igual 0
        print(f"Ya no puedes comprar mas helados ni tienes mas tarrinas para cambiar")
        print(f"compraste en total {helado} helados")
        break # sale del script 
    else:
        try:
         ele = int(input("introdusca 1 para comprar un helado, 2 para cambiar una tarrina o 3 para salir")) # le pide al usuario que introdusca una eleccion para comprar helado, cambiar tarrina o salir del programa
         if ele == 1: # comprueba si el usuario quiere comprar helado
            if dinero >= 2: # comprueba que el dinero sea igual o mayor a 2 paraque pueda comprar helado
                dinero = dinero - 2 # le resta el valor del helado al dinero 
                helado = helado + 1 # dice cuantos helados a comprado el usuario
                tarrina = tarrina + 1 # suma una tarrina por cada helado que compre el usuario
                print(f"He comprado un helado, ahora tengo {helado} helados, tarrina {tarrina} y {dinero} monedas.")
            else: # si no tiene dinero suficiente para comprar helado 
                print(f"un helado vale 2 monedas y tu solo tienes {dinero}")
            #fi  cierra el if 
         elif ele == 2: # comprueba que el usuario quiera cambiar una tarrina
            if tarrina >= 1: # verifica que el usuario tengo almenos una tarrina para cambiar
                tarrina = tarrina - 1 # resta la tarrina que cambio el usuario
                dinero = dinero + 1 # le suma el dinero de la tarrina 
                print(f"He cambiado una tarrina, ahora tengo {tarrina} tarrinas y {dinero} monedas.")
            else: # si no tiene tarrina
                print(f"No puedes cambiar ninguna tarrina por que tienes {tarrina}")
            #fi  cierra el if 
         elif ele == 3: # si el usuario quiere salir del script 
            print(f"Elegiste salir")
            print(f"compraste en total {helado} helados")
            break # sale del script
         else: # si el usuario coloca una opsion no valida
            print(f"elija una opsion valida")
        except ValueError:
         print(f"elija una opsion valida")
        