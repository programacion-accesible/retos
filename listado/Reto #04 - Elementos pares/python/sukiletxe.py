# Como me puse a hacer pruebas en Python para ver si podía hacer algo similar a lo ya hecho en Haskell, me salió esto. La estructura entera se la copio a @ronnyg2121, cuya solución está aquí al lado en su archivo. Lo único que cambia es la función. Ahora bien, ambas cosas hacen exactamente lo mismo, salvo que él comprueba si el elemento actual está en la nueva lista y yo uso un conjunto (que no puede tener duplicados). Mi solución probablemente sea más lenta porque convierte el conjunto a una lista al final. Es posible que utilizando collections.counter  esto vaya más rápido.

def elementosPares(lista):
    # Esto itera sobre la lista original, cuenta los elementos que sean iguales al que está iterando. Si el elemento aparece un número par de veces, lo añade a un conjunto, si no no. Luego crea una lista con los elementos de ese conjunto.
    return list({x for x in lista if lista.count(x) % 2 == 0})

def main():
    lista_ejemplo = ["a", "c", "c", 1, 31, 1, 2, "c", "c", "D", "D"]
    print(elementosPares(lista_ejemplo))

main()
