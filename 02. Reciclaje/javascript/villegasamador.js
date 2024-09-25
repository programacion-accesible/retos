let botellas = 0;
let cervezas = 0;
let saldo = 0;

function calcular_cervezas(monedas) {
    if (monedas >= 2) {
        cervezas++;
        monedas -= 2;
        botellas++;
        console.log(`He comprado una cerveza, ahora tengo ${cervezas} cervezas, ${monedas} monedas y ${botellas} botellas.`);
        return calcular_cervezas(monedas);
    } else if (monedas < 2 && botellas >= 1) {
        botellas--;
        monedas++;
        console.log(`He cambiado una botella, ahora tengo ${botellas} botellas y ${monedas} monedas.`);
        return calcular_cervezas(monedas);
    } else {
        saldo += monedas;
        return;
    }
}

calcular_cervezas(10);
console.log(`Finalmente compré ${cervezas} cervezas, y me han quedado ${botellas} botellas y ${saldo} monedas.`);
