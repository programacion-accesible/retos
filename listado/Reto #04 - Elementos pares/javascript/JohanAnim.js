// solución del reto número 4 - Elementos pares
// javascript/JohanAnim.js

// Primero importamos lo necesario para usar entradas de usuario
const readline = require('readline');

// Creamos una función asíncrona que facilita el uso de la entrada de usuario
const leerEntrada = async (pregunta) => {
	const rl = readline.createInterface({
		input: process.stdin,
		output: process.stdout
	});

	const respuesta = await new Promise(resolve => {
		rl.question(pregunta, respuesta => {
			rl.close();
			resolve(respuesta);
		});
	});

	return respuesta;
};

// Vamos a definir una función main para tener todo más ordenado
const main = async () => {
	// Aquí definimos un Array para almacenar todos los elementos
	const elementos = [];

	// ahora creamos un bucle while para pedir los elementos al usuario hasta que este ingrese un elemento negativo
	while (true) {
		// le pedimos al usuario que introduzca un elemento
		const elemento = await leerEntrada('Introduce un elemento para continuar, para salir solo introduce algún número negativo:');

		// si el elemento es negativo, salimos del bucle
		if (elemento < 0) {
			// Usamos filter para verificar los elementos que se han repetido
			const repetidos = elementos.filter((elem, index, self) => self.indexOf(elem) !== index);
			//   luego creamos un nuevo Array con los elementos unicos
			const unicos = [...new Set(repetidos)];
			console.log(`Los elementos que se han repetido son: "${unicos.join('", "')}"`);

			break;
			console.log('Muchas gracias por provar mi programa. Hasta pronto.');
		}

		// añadimos el elemento al Array
		elementos.push(elemento);
	}
};

// Llamamos a la función principal
main();