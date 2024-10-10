#!/bin/bash

# script que muestra la solución del reto 6
# hecho por Elvin Vargas


until false; do

read -p "Ingrese un número: " numero

if [[ $numero =~ ^[0-9]+$ && numero -ge 0 ]]; then
if (( ${#numero} % 2 == 0 )); then
    # Inicializar una variable para almacenar los pares de dígitos
    par_numero=0
    # Inicializar una variable para almacenar la suma de los divisores propios menos 1
    oculto=0
    
    
    # Iterar sobre cada par de dígitos del número
    for (( i=0; i<${#numero}; i+=2 )); do # inicializo un bucle for con $i en 0; se comprueba que el valor de $i es menor a la cantidad de caracteres de $numero y luego se le     suma 2 en cada interacción
        # Extraer dos dígitos a la vez
        par_numero="${numero:$i:2}"
        # dividendo pasa a tomar el valor de cada par de números
        dividendo="$par_numero"
        # inicializo perfecto que guarda la suma de los divisores y se inicializa en cada iteracion
        perfecto=0
        # inicializo divisor en 1 para en el proximo for sea menor que dividendo
        divisor=1
        for ((divisor; divisor<dividendo; divisor++)); do # este bucle comprueba que divisor sea menor al dividendo y si lo es le suma 1 en cada iteracion 
            if (( dividendo % divisor == 0 )); then # el if comprueba que el modulo del dividendo entre el divisor es 0 si lo es lo suma en la variamble prefecto
                perfecto=$((perfecto + divisor))
            fi # cierro el if
        done # cierro el for 
        oculto=$((oculto + perfecto - 1)) # sumo en cada iteracion el valor de perfecto y le resto 1 
    done # cierro el for

    # imprimo el valor del número oculto
    echo "SU NÜMERO OCULTO ES: "
    echo "$oculto"
    exit 0
else 
    echo " el numero que ingrese deve tener digitos pares y ser pocitivo "
fi
else
    echo " el numero que ingrese deve tener digitos pares y ser pocitivo "
fi
done