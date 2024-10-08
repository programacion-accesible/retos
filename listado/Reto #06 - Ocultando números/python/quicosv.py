import math

class DigitosImpares(Exception):
	pass

class EmpiezaPorCero(Exception):
	pass

def hacerParejas(numero):
	parejas=[]
	for i in range(0,len(numero),2):
		parejas.append(int(numero[i]+numero[i+1]))
	return parejas

def sumaDivisores(numero):
	divisores=[]
	for i in range(2,numero):
		if len(divisores)>0 and i>max(divisores): break
		if i in divisores: continue
		if numero%i==0:
			divisores.append(i)
			if i!=math.sqrt(numero): divisores.append(numero//i)
	return sum(divisores)

while True:
	try:
		numero=input("Número a ocultar: ")
		int(numero)
		if(len(numero)%2==1): raise DigitosImpares
		if(numero[0]=="0"): raise EmpiezaPorCero
	except ValueError:
		print("No has escrito un número.")
		continue
	except DigitosImpares:
		print("El número debe tener una cantidad par de cifras.")
		continue
	except EmpiezaPorCero:
		print("el número no puede empezar por 0.")
		continue
	else:
		break

ingredientes=[]
for pareja in hacerParejas(numero):
	ingredientes.append(sumaDivisores(pareja))

print(sum(ingredientes))