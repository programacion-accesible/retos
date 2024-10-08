#!/bin/bash

# se crea la función que filtra los argumentos que aparezcan más de 1 vez
function_filtro() {
# Inicializamos un diccionario asociativo para contar las ocurrencias
declare -A contador

# Inicializamos un array vacío
resultado=()

# Iteramos sobre cada argumento
for elemento in "$@"; do
  # Incrementamos el contador correspondiente al elemento
  ((contador[$elemento]++))
done

# Imprimimos los resultados y guardamos en el array $resultado los elementos que se repiten
for elemento in "${!contador[@]}"; do
if [[ ${contador[$elemento]} > 1 ]]; then
resultado+=$elemento
  echo "$elemento se repite ${contador[$elemento]} veces"
fi
done
}

# comprobamos que en la llamada al script el usuario pase los argumentos, si no lo hace le mostramos un mensaje de error y finalizamos el script
if [[ "$#" -eq 0 ]]; then
echo "Estimado deves ingresar una lista de argumentos ceparadas por espacios"
echo "Ejemplo de uso"
echo "bash elvinv11.sh a a b c"
exit 1
else
function_filtro $@
fi

if [[ ${#resultado[@]} -eq 0 ]]; then
echo "No introdujiste elementos repetidos"
exit 1
else
# finalmente imprimo el array que contiene los elementos que se repiten
echo "Los elementos que introdujiste repetidos son:"
echo " ${resultado[@]}"
fi
