botellas = 0
cervezas = 0
saldo = 0

def calcular_cervezas(monedas):
    global cervezas, botellas, saldo

    if monedas >= 2:
        cervezas += 1
        monedas -= 2
        botellas += 1
        print(f"He comprado una cerveza, ahora tengo {cervezas} cervezas, {monedas} monedas y {botellas} botellas.")
        return calcular_cervezas(monedas)
    elif monedas < 2 and botellas >= 1:
        botellas -= 1
        monedas += 1
        print(f"He cambiado una botella, ahora tengo {botellas} botellas y {monedas} monedas.")
        return calcular_cervezas(monedas)
    else:
        saldo += monedas
        return

calcular_cervezas(10)
print(f"Finalmente compré {cervezas} cervezas, y me han quedado {botellas} botellas y {saldo} monedas.")
