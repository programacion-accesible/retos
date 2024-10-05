// Ejercicio para calcular la cantidad mínima de dinero necesario para comprar una cierta cantidad de litros de agua
const readline = require('readline');

const calcularMinimo= (x, y) => (x <y) ? x : y;

// Crear una promesa que envuelve readline.question
const obtenerEntrada = (pregunta) => {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    return new Promise((resolve) => rl.question(pregunta, (respuesta) => {
        rl.close();
        resolve(respuesta);
    }));
};

const main = (cantidad, botella1, botella2) => {
    let costo = 0;
    
    if (cantidad%2!==0) {
        costo = (botella1 * cantidad);
        console.info(`El precio mínimo para comprar ${cantidad} litros de agua es: ${costo}`);
    } else {
        costo = calcularMinimo(botella1* cantidad, (botella2* cantidad) /2);
        console.info(`El precio mínimo para comprar ${cantidad} litros de agua es: ${costo}`);
    }

    return;
};

// Función asíncrona para manejar la entrada de manera secuencial
const ejecutar = async () => {
    try {
        const cantidad = parseInt(await obtenerEntrada('Introduce la cantidad de litros de agua: '));
        const botella1 = parseInt(await obtenerEntrada('Introduce el precio de la botella pequeña: '));
        const botella2 = parseInt(await obtenerEntrada('Introduce el precio de la botella grande: '));

        main(cantidad, botella1, botella2);
    } catch (error) {
        console.error('Ocurrió un error al procesar la entrada.', error);
    }
};

// Ejecutar la función principal
ejecutar();
