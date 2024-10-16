const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para leer entrada del teclado con manejo de errores
const leerEntrada = (pregunta) => {
    return new Promise((resolve, reject) => {
        try {
            rl.question(pregunta, (respuesta) => {
                if (!respuesta) {
                    reject('No se proporcionó una entrada válida');
                } else {
                    resolve(respuesta);
                }
            });
        } catch (error) {
            reject(`Error al leer la entrada: ${error.message}`);
        }
    });
};

let helados = 0;
let recipientes = 0;

const comprar = () => {
    console.info(`Tienes ${monedas} monedas, ${helados} helados y ${recipientes} recipientes.`);
    while (monedas >= 2) {
        helados += 1;
        recipientes += 1;
        monedas -= 2;
        console.info(`Tienes ${monedas} monedas, ${helados} helados y ${recipientes} recipientes.`);
    }
};

const reciclar = () => {
    while (recipientes > 0) {
        recipientes -= 1;
        monedas += 1;
        console.info(`Reciclaste 1 recipiente. Ahora tienes: ${recipientes} recipientes, ganaste 1 moneda y ahora tienes: ${monedas} monedas.`);
    }
};

// Función principal
const main = async () => {
    try {
        const respuesta = await leerEntrada('¿Cuántas monedas tienes? ');
        monedas = parseInt(respuesta);

        if (isNaN(monedas) || monedas < 0) {
            throw new Error('La cantidad de monedas debe ser un número válido y mayor o igual a 0');
        }

        while (monedas >= 2 || recipientes > 0) {
            comprar();
            reciclar();
        }

        rl.close(); // Cerramos la interfaz de readline
    } catch (error) {
        console.error(`Error: ${error}`);
        rl.close();
    }
};

main();
