"""
este es un script que divide usando desplazamientos de bits
"""

# función que toma el número a dividir y el número por el cual dividiremos
def divide(dividendo, divisor):
    # evitamos la división por cero
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    
    # almacenamos el resultado de la división en cociente
    cociente = 0
    # usamos temp_divisor para modificar y ajustar el divisor en el proceso de búsqueda de la potencia de 2 más cercana
    temp_divisor = divisor
    # usamos multiplicador para escalar el cociente y el divisor en potencias de 2
    multiplicador = 1

    # buscamos la mayor potencia de 2 del divisor que sea menor o igual al dividendo
    while temp_divisor <= dividendo:
        # desplazamos los bits una posición hacia la izquierda (multiplicamos por 2 cada valor)
        temp_divisor <<= 1
        multiplicador <<= 1

    # reducimos el divisor y el multiplicador, restando las "porciones grandes" de dividendo
    while multiplicador > 1:
        # desplazamos los bits una posición hacia la derecha (dividimos entre 2 cada valor)
        temp_divisor >>= 1
        multiplicador >>= 1

        # si el dividendo es mayor o igual a temp_divisor
        if dividendo >= temp_divisor:
            # restamos temp_divisor del dividendo
            dividendo -= temp_divisor
            # sumamos el valor actual de multiplicador al cociente (acumulamos la contribución de la potencia de 2 al cociente final)
            cociente += multiplicador

    return cociente # devolvemos el resultado de la división

print("El resultado es: ", divide(100, 5))
