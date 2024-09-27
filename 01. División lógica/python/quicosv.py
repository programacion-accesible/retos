# Basado en villegasamador.py
# Utilizo sumas y restas para facilitar la comprensión del algoritmo
# También se calcula el resto de la división.

# Esta clase no hace nada, pero está ahí para generar un error
class NoPermitido(Exception):
	pass

# Función que calcula la división
def divide(dividendo,divisor):
	# Al empezar el cociente es 0 y el resto es el dividendo
	cociente=0	
	resto=dividendo
	# La división termina cuando el resto sea menor que el divisor
	while resto>=divisor:
		# Este algoritmo va de incrementa rel cociente y disminuir el resto
		# Lo que sumaremos al cociente parte de 1
		sumarCociente=1
		# Lo que restamos al resto parte del divisor
		restarResto=divisor
		# El resto nos marca los cálculos
		while restarResto<=resto:
			# Si nos vamos a pasar salimos del bucle
			if(restarResto+restarResto>=resto):
				break
			else:
			# Como no nos hemos pasado seguimos incrementando	
				restarResto+=restarResto
				sumarCociente+=sumarCociente
		# Actualizamos el cociente y el resto
		cociente+=sumarCociente
		resto-=restarResto
	return cociente,resto

# Pedimos el dividendo y el divisor controlando los errores
while True:
	try:
		dividendo=int(input("Dividendo: "))
		if(dividendo<0): raise NoPermitido
	except ValueError:
		print("Eso no es un número.")
		continue
	except NoPermitido:
		print("Sólo sé dividirsi el dividendo es positivo.")
		continue
	else:
		break
while True:
	try:
		divisor=int(input("Divisor: "))
		if(dividendo<=0): raise NoPermitido
	except ValueError:
		print("Eso no es un número.")
		continue
	except NoPermitido:
		print("No se puede dividir entre 0. Además, solo sé dividirsi el dividendo es positivo.")
		continue
	else:
		break

# Calculamos el cociente y el resto con los valores proporcionados
if(dividendo==0):
	cociente=0
	resto=divisor
else:
	cociente,resto=divide(dividendo,divisor)

# Informamos al usuario del resultado
print(f"el cociente es {cociente} y el resto es {resto}.")