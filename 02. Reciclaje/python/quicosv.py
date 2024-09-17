while True:
	try:
		monedas=int(input("Cantidad de monedas: "))
	except ValueError:
		print("Eso no es un número")
		continue
	else:
		break

while True:
	try:
		precio=int(input("Precio del producto: "))
	except ValueError:
		print("Eso no es un número")
		continue
	else:
		break

while True:
	try:
		devolucion=int(input("Monedas devueltas por unidad reciclada: "))
	except ValueError:
		print("Eso no es un número.")
	else:
		break

productos=0

def comprar():
	global monedas
	global precio
	global productos
	while(monedas>=precio):
		monedas=monedas-precio
		productos=productos+1
		print(f"Compro un producto. Tengo {monedas} monedas y {productos} productos.")
	
def reciclar():
	global productos
	global monedas
	global devolucion
	while productos>0:
		productos=productos-1
		monedas=monedas+devolucion
		print(f"Devuelvo un envase. Tengo {productos} envases y {monedas} monedas.")

while(monedas>=precio or productos>0):
	comprar()
	reciclar()