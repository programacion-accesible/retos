#!/bin/bash

##### para ejecutar el codigo use bash elvin11.sh
##### tambien puede otorgarle permiso de ejecucion con chmod +x elvinv11.shy luego ejecutar con ./elvinv11.sh
 
######desglose de la linea siguiente
    ###### read el comando que lee de la entrada estandar (teclado), para luego guardar en una variable
    ###### -p "Escriba el dividendo" el argumento -p "  " imprime el mensaje por pantalla antes de esperar que la persona introdusca la orde
    ###### dividendo define la variable dividendo donde  read guarda lo que escribe el usuario
read -p "Escriba el dividendo  " dividendo
read -p "Ahora escriba el divisor  " divisor
###### las lineas que siguen definen un if que valida que el divisor no es 0 si lo es arroja el mensaje por pantalla y finalisa el script
if [ $divisor -eq 0 ]; then
    echo "el divisor no puede ser 0"
    exit 1
fi 
var=$divisor # inicializo la varible var con el valor del divisor
resultado=0  # inicializo el contador 
###### acotinuacion esta un bucle while se ejecutara asta que var sea mayor que dividendo
while [ $var -le $dividendo ]; do 
    var=$((var + divisor))
    resultado=$((resultado + 1))
done
echo -e  "el resultado de ${dividendo}/${divisor} es $resultado"
###### la linea anterior imprime el resultado y uso delimitadores para la espancion de variables

##### escript realizado por Elvin Vargas Venezuela
