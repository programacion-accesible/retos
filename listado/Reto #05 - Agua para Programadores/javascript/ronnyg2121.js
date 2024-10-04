// Ejercicio para calcular la cantidad mínima de dinero necesario para comprar una cierta cantidad de litros de agua


// const calcularMinimo= (x, y) => (x <y) ? x : y;
const main = (cantidad, botella1, botella2) => {
    let costo1 = botella1* cantidad;
    let costo2 = botella2 * cantidad;
    if (!cantidad %2 === 0) {
        console.info(`El precio mínimo para comprar ${cantidad} litros de agua es: ${costo1}`);
    } else {
        console.info(`El precio mínimo para comprar ${cantidad} litros de agua es: ${costo2}`);
    }
return;
}


main(10, 1, 3);