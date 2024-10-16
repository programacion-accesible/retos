#!/usr/bin/env python3

from sys import argv, exit
# se crea la función que filtra los argumentos que aparezcan más de 1 vez
def function_filtro(argv): 
# Inicializamos un diccionario asociativo para contar las ocurrencias
    contador = {  }
    # Inicializamos un array vacío
    resultado = []
    # Iteramos sobre cada argumento
    for elemento in argv[1:]:
        # Incrementamos el contador correspondiente al elemento
        contador[elemento] = contador.get(elemento, 0) + 1  
    # Imprimimos los resultados y guardamos en el array $resultado los elementos que se repiten
    for elemento in contador:
        if contador[elemento] > 1 and contador[elemento] % 2 == 0:
            resultado.append(elemento)
            print(f"{elemento} se repite {contador[elemento]} veces")
    return resultado


# comprobamos que en la llamada al script el usuario pase los argumentos, si no lo hace le mostramos un mensaje de error y finalizamos el script
if len(argv) == 1:
    print("Estimado deves ingresar una lista de argumentos ceparadas por espacios")
    print("Ejemplo de uso")
    print("python elvinv11.py a a b c")
    exit(1)
else:
    ele = function_filtro(argv)

if len(ele) == 0:
    print(f"No introdujiste elementos repetidos")
    exit(1)
else:
    # finalmente imprimo el array que contiene los elementos que se repiten
    print(f"Los elementos que introdujiste repetidos son:")
    print(ele)

