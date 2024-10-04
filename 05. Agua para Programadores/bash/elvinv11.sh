#!/bin/bash

# script hecho por Elvin Vargas

read -p "Ingrese la cantidad de litros (N): " n # se pide al usurio cantidad de litros y se guarda en la variable $n
if [[ $n =~ ^[0-9]+$ ]]; then  # se comprueba que el dato es un entero
    if [[ $n -ge 1 && $n -le 10**12 ]]; then # se comprueba que el valor de $n es mayor o igual que 1 y menor o igual a 10 elevado a la 12
        read -p "Ingrese el costo de la botella de 1 litro (A): " a # se pide el costo y se guarda en la variable $a
        if [[ $a =~ ^[0-9]+$ && $a -ge 1 && $a -le 1000 ]]; then # se comprueba que $a es entero, >= 1 y <= 1000
            read -p "Ingrese el costo de la botella de 2 litros (B): " b # se pide el costo de la bottella de 2 litros y guarda en $b
            if [[ $b =~ ^[0-9]+$ && $b -ge 1 && $b -le 1000 ]]; then # se verifica que $b es entero, >= 1 y <= 1000
                if (( $n % 2 == 0 )); then # se comprueba que $n sea par para luego decidir si puede comprar botellas de 2 litros o de 1 litros
                    total_a=$(($n * $a)) # se multiplica litros por precio
                    total_b=$(($n * $b / 2)) # se multiplica litros por precios y se divide entre 2 da la cantidad de dinero al comprar botellas de dos litros
                    if (( $total_b < $total_a )); then # comprueba si la cantidad de del precio de dos litros es menor que las de 1 litros
                        echo "El costo mínimo para comprar $n litro de agua es: ${total_b}" # es la salida si el valor de las botellas de 2 litros de agua es menor 
                    fi # cierra el if de que comprueba que precio es menor para el usuario
                else
                    echo "El costo mínimo para comprar $n litro de agua es: $(($n * a))" # es la salida si $n no es par el usuario deve comprar botellas de 1 litros porque no se pueden mesclar
                fi # se cierra el if que comprueba si $n es par
            fi # se cierra el if de las comprobaciones de $b
        fi # se cierra el if de las comprobaciones de $a
    fi  # se cierra el if de las comprobaciones de $n
else
    echo "deves introducir un número entero"
fi # se cierra el if que comrueba que $n es entero
