#!/bin/bash

# script hecho por Elvin Vargas
# finalidad resolber el reto del reciclage 

# inicializo las variables
dinero=20
helado=0
tarrina=0

while [[ $dinero -ge 1 || $tarrina -ge 1 ]]; do
    # la linea anterior inicia el bucle while comprueba que dinero y tarrina  sea mayor o igual 1  
    echo "¿Cuánto vale un helado? 2"
    echo "¿Cuánto me devuelven por una tarrina? 1"
    Echo "¿Cuánto dinero tengo? $dinero"

    if [[ $dinero -lt 2 && $tarrina -eq 0 ]]; then # compruebo que dinero mayor que 2 y tarrina seha igual 0
        echo "Ya no puedes comprar mas helados ni tienes mas tarrinas para cambiar"
        echo "compraste en total $helado helados"
        break # sale del script 
    else
        read -p "introdusca 1 para comprar un helado, 2 para cambiar una tarrina o 3 para salir" ele # le pide al usuario que introdusca una eleccion para comprar helado, cambiar tarrina o salir del programa
        if [ $ele -eq 1 ]; then # comprueba si el usuario quiere comprar helado
            if [ $dinero -ge 2 ]; then # comprueba que el dinero sea igual o mayor a 2 paraque pueda comprar helado
                dinero=$(( dinero - 2 )) # le resta el valor del helado al dinero 
                helado=$(( helado + 1 )) # dice cuantos helados a comprado el usuario
                tarrina=$(( tarrina + 1)) # suma una tarrina por cada helado que compre el usuario
                echo "He comprado un helado, ahora tengo $helado helados, tarrina $tarrina y $dinero monedas."
            else # si no tiene dinero suficiente para comprar helado 
                echo "un helado vale 2 monedas y tu solo tienes $dinero"
            fi # cierra el if 
        elif [ $ele -eq 2 ]; then # comprueba que el usuario quiera cambiar una tarrina
            if [ $tarrina -ge 1 ]; then # verifica que el usuario tengo almenos una tarrina para cambiar
                tarrina=$(( tarrina - 1)) # resta la tarrina que cambio el usuario
                dinero=$(( dinero + 1)) # le suma el dinero de la tarrina 
                echo "He cambiado una tarrina, ahora tengo $tarrina tarrinas y $dinero monedas."
            else # si no tiene tarrina
                echo "No puedes cambiar ninguna tarrina por que tienes $tarrina"
            fi # cierra el if 
        elif [ $ele -eq 3 ]; then # si el usuario quiere salir del script 
            echo "Elegiste salir"
            echo "compraste en total $helado helados"
            break # sale del script
        else # si el usuario coloca una opsion no valida
            echo "elija una opsion valida"
        fi # cierra el if 
    fi # cierra el if 
done # cierra el bucle while 

