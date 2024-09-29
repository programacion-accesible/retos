class Botellas:
	def __init__(self,cantidad,precio):
		self.cantidad=cantidad
		self.precio=precio
		self.coste=self.precio*self.cantidad

class ValorInvalido:
	pass

minimo=lambda x,y: x if x<y else y

def pedirEntero(mensaje,minimo,maximo):
	while True:
		try:
			entero=int(input(mensaje))
			if(entero<minimo or entero>maximo): raise ValorInvalido
		except ValueError:
			print("Debes escribir un número.")
			continue
		except ValorInvalido:
			print(f"Debes escribir un valor entre {minimo} y {maximo}.")
			continue
		else:
			break
	return entero

n=pedirEntero("Cantidad de litros: ",1,10**12)
a=pedirEntero("Precio de una botella de un litro: ",1,1000)
b=pedirEntero("Precio de una botella de 2 litros: ",1,1000)
botellas1=Botellas(n,a)
if(n%2==1):
	dinero=botellas1.coste
else:
	botellas2=Botellas(n//2,b)
	dinero=minimo(botellas1.coste,botellas2.coste)

if(n==1):
	concuerdaCantidad="un litro"
else:
	concuerdaCantidad=f"{n} litros"

if(dinero==1):
	concuerdaDinero="una unidad monetaria"
else:
	concuerdaDinero=f"{dinero} unidades monetarias"

print(f"El coste mínimo para comprar {concuerdaCantidad} es {concuerdaDinero}.")