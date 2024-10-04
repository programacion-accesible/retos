import random
import sys
class FueraDeRango(Exception):
	pass

minimo=1
maximo=100
totalIntentos=6
ganador=False
objetivo=random.randint(minimo,maximo)
print(f"He pensado en un número entre {minimo} y {maximo}. Tienes {totalIntentos} intentos. A ver si lo aciertas.")

for intento in range(1,totalIntentos+1,1):
	while True:
		try:
			prueba=int(input(f"Intento {intento}: "))
			if(prueba not in range(minimo,maximo+1)): raise FueraDeRango
		except ValueError:
			print("No has escrito un número.")
			continue
		except FueraDeRango:
			print(f"Debes escribir un número entre {minimo} y {maximo}.")
		except KeyboardInterrupt:
			print(f"Sales sin haber adivinado el {objetivo}.")
			sys.exit()
		else:
			break
	if(prueba==objetivo):
		ganador=True
		break
	elif(prueba>objetivo):
		print(f"{prueba} es muy grande.")
	else:
		print(f"{prueba} es muy pequeño.")
if(ganador):
	print("¡Felicidades! ¡Has ganado!")
else:
	print(f"Has perdido. Tenías que adivinar el número {objetivo}.")