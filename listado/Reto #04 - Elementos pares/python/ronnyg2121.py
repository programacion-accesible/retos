
# Estto es una función que toma una lista de elementos y devuelve solo los elementos que se repitan un número par de veces

def elementosPares(lista):
    filtrada = []
    for i in lista:
        contador = lista.count(i)
        if contador % 2 == 0 and i not in filtrada:
            filtrada.append(i)
    return filtrada

def main():
    lista_ejemplo = ["a", "c", "c", 1, 31, 1, 2, "c", "c", "D", "D"]
    print(elementosPares(lista_ejemplo))

main()
