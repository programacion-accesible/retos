
# ejercicio número 1 por JohanAnim

print("Bienvenido/a, un programa que divide dos números sin necesidad de usar ni el signo de multiplicación ni el de divición, te lo demostraré!")

try:
	num1 = float(input("Dame el primer número (Dividendo):"))
	print("Bien.")
	num2 = float(input("Ahora dame el segundo número (Divisor):"))

	# ahora aquí asemos la operación para dividir los dos números
	cosiente = 0

	print("Mira el recorrido que emos echo:")
	while(num1>=num2 and num2!=0):
		num1 -= num2
		cosiente+=1
		print(f"{num1} - {num2} = {num1-num2}")
		if num1 < num2:
			print("Y listo.")

	print(f"El resultado de su división es: {cosiente}.")
	print("Muchas gracias por provar mi solución! Si te gustó sígueme en GitHub como @JohanAnim. ¡Hasta la próxima.")
	input("Pulsa enter para finalizar.")

except ZeroDivisionError as e:
	print(f"Lo ciento, pero el programa se detuvo por este motivo: {e}")

except ValueError as e:
	print(f"Lo ciento, pero el programa se detuvo por este motivo: {e}")