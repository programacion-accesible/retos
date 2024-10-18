"""
Este es un programa que divide sin tener que usar el signo de división ni el de multiplicación
"""

# Función que recibe los 2 parámetros


def divide_plus(dividendo, divisor):
    # Primero, inicializamos el cociente en 0. Esta variable nos servirá para devolverla cuando tengamos el resultado deseado.
    cociente = 0

    # Validamos si el vivisor es 0 para retornar un error
    if divisor <= 0:
        print('División infinita. Esto no es posible.')
        return False

    # Creamos un bucle while para que se repita mientras el dividendo sea mayor o igual que el  divisor. Este se aplica como lógica iversa, ya que le división se puede hacer mientras el divisor sea menor al dividendo
    while dividendo >= divisor:
        # Esta es la clave y la fórmula para lograr esto. La resta se puede aplicar cuantas veces sea necesaria hasta que el dividendo sea menor al divisor
        dividendo -= divisor

        # Ahora, incrementamos el cociente de uno en uno. Esto representa la cantidad de veces que se hizo la resta, Dándonos el resultado ya que el cociente es el número de veces que se puede restar el divisor al dividendo
        cociente += 1

        # finalmente, retornamos el cociente. Por ahora, nos entrega una división básica, ya que es entera.
    return cociente

pregunta = ""
while pregunta!= "salir":
    try:
        dividendo  = int(input("Ingrese el dividendo"))
        divisor = int(input("Ingrese el divisor"))
        print(divide_plus(dividendo, divisor))
    except:
        print("Por favor ingrese un número")

    pregunta = input("¿Desea continuar?")
