def partir(valor, tamano):
    # Esta función recibe una cadena donde se le pasan números. Luego devuelve una lista de enteros con los números partidos al tamaño elegido, usamos 2 para el propósito del ejercicio
    try:
        valor = str(valor)
    except:
        return None
    return [int(valor[i:i+tamano]) for i in range(0, len(valor), tamano)]

def calcular_divisores(num):
    # Esta función calcula los divisores de los números devueltos en la lista por la función partir. Utiliza la fórmula de que un número es divisor de otro si al dividirlo su reciduo es 0. Por último, utiliza un contador que contará a partir de 2 mientras que el contador sea menor al número
    contador = 2
    suma = 0
    while contador < num:
        if contador == num:
            break
        if num % contador == 0:
            suma += contador
        contador += 1
    return suma


def sumar_divisores_partidos(valor, tamano):
# Por último, esta función combina las otras 2, primero obteniendo la lista con la función partir, recorriendo dicha lista y luego llamando a la función que calcula los divisores para que calcule cada número partido y finalmente sume los divisores y devuelva un entero
    partes = partir(valor, tamano)
    suma_total = 0

    for parte in partes:
        suma_total += calcular_divisores(parte)

    return suma_total

try:
    numero = input("Ingrese el número con dígitos pares")
    print(sumar_divisores_partidos(numero, 2))

except Exception as e:
    print(f"A ocurrido un error inesperado. {e}")
