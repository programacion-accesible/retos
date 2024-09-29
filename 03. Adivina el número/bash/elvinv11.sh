#!/bin/bash
# script hecho por Elvin Vargas
# es la respuesta al reto 03 de adivina el número 

export LANG=es_ES.UTF-8 # Está línea establece la codificación UTF-8,  importando la variable de entorno 
numero=$(($RANDOM%101))
respuesta=102
contador=0
echo "Bienvenido a Adivina el número"
echo "  "
echo "Tendrás 6 intentos para adivinar el número que he pensado."
echo "Solo te diré que está  del 0 al 100."
echo "  "
while [ $numero -ne $respuesta ]
do
 let contador=contador+1
 if [ $contador -gt 6 ]
 then
 echo "Intentos agotados"
 echo "El número era $numero"
 exit
 else
  read -p "¿Cual es el numero? del 0 al 100: " respuesta
  echo "Numero de intentos $contador de 6."
  if [ $numero -lt $respuesta ]
  then
   echo "El número es menor a $respuesta"
  elif [ $numero -gt $respuesta ]
  then
   echo "El número es mayor a $respuesta"
  fi 
 fi
done

echo "¡Has ganado! el número es $numero."
