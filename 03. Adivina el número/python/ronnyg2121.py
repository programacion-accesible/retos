import random


num = 0
aleatorio = random.randint(1, 100)
vidas = 5
print("Este es un juego de adivina el número")

while True:
    try:
        num = int(input("Por favor ingrese un número"))
    except:
        print("Por favor no ingrese letras. ¡Solo se aceptan números!")
        continue
    if aleatorio < num:
        print("El número introducido es menor.")
        vidas -= 1
        print("Ahora tienes: " + str(vidas), "Vidas")
    elif aleatorio > num:
        print("El número introducido es mayor")
        vidas -= 1
        print("Ahora tienes: " + str(vidas), "Vidas.")
    if num == aleatorio:
        print("¡Felicitaciones! ¡Usted a ganado! \t Lo lograste cuando te quedaban" + str(vidas), "Vidas")
        break
    elif vidas <= 0:
        print("¡No te quedan vidas!")
        print("¡Perdiste! el número aleatorio era: " + str(aleatorio))
        break
