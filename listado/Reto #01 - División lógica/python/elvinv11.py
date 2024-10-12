#!/usr/bin/env python3

def divicionSinDividir(dividendo, divisor):
    var = divisor 
    resultado = 0   
    while var <= dividendo: 
        var = var + divisor
        resultado = resultado + 1
    return resultado



while True:
    try:
        dividendo = int(input("Introdusca el dividendo: "))
        if dividendo <= 0:
            print("el dividendo deve ser mayor que 0")
            continue
        divisor = int(input("Ingrese el divisor: "))
        if divisor <= 0 or divisor >= dividendo:
            print("El divisor deve ser mayor que 0 y menor que el dividendo")
            continue
        cociente = divicionSinDividir(dividendo, divisor)
        print(f"el resultado de {dividendo}/{divisor}={cociente}")
        break
    except ValueError:
        print("Deves introducir un entero mayor que 0")
        