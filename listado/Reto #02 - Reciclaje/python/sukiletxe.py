from time import sleep
def comprar_helado(helados, coste_helado, monedas):
  helados +=1
  monedas -= coste_helado
  return helados, monedas

def cambiar_tarrina(tarrinas, coste_tarrina, monedas):
  tarrinas -= 1
  monedas += coste_tarrina
  return tarrinas, monedas

def preguntar_numero(prompt):
    respuesta = 0
    while not respuesta:
        try:
            respuesta = int(input(prompt))
        except ValueError:
            print("Introduce un número entero.")
    return respuesta

def main():
  coste_helado = preguntar_numero("¿Cuánto vale un helado? ")
  coste_tarrina = preguntar_numero("¿Cuánto me devuelven por una tarrina? ")
  monedas = preguntar_numero("¿Cuánto dinero tengo? ")
  helados = 0
  seguir = True
  while seguir:
    while monedas >= coste_helado:
      helados, monedas = comprar_helado(helados, coste_helado, monedas)
      print(f"He comprado un helado, ahora tengo {helados} helados y {monedas} monedas")
      sleep(2)
    while helados > 0:
      helados, monedas = cambiar_tarrina(helados, coste_tarrina, monedas)
      sleep(2)
      print(f"He cambiado una tarrina, ahora tengo {helados} tarrinas y {monedas} monedas")
    if monedas < coste_helado and helados == 0: 
      seguir = False

main()
