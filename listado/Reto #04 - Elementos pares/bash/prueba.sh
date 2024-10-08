#!/bin/bash
array=("a", "a", "b", "c")

echo " los elementos del array son ${array[@]}"

for elementos in "${array[@]}"; do
echo "imprimo los elementos"
echo "$elementos "
echo "esto es el elemnto no el indice $elemento[0] "
done 
