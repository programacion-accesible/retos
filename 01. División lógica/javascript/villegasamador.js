/* este es un script que divide usando desplazamientos de bits */

// función que toma el número a dividir y el número por el cual dividiremos
function divide(dividendo, divisor) {
    // evitamos la división por cero
    if (divisor === 0) {
        return Infinity;
    }

    // almacenamos el resultado de la división en cociente
    let cociente = 0;
    // usamos tempDivisor para modificar y ajustar el divisor en el proceso de búsqueda de la potencia de 2 más cercana
    let tempDivisor = divisor;
    // usamos multiplicador para escalar el cociente y el divisor en potencias de 2
    let multiplicador = 1;

    // buscamos la mayor potencia de 2 del divisor que sea menor o igual al dividendo
    while (tempDivisor <= dividendo) {
        // desplazamos los bits una posición hacia la izquierda (multiplicamos por 2 cada valor)
        tempDivisor <<= 1;
        multiplicador <<= 1;
    }

    // reducimos el divisor y el multiplicador, restando las "porciones grandes" de dividendo
    while (multiplicador > 1) {
        // desplazamos los bits una posición hacia la derecha (dividimos entre 2 cada valor)
        tempDivisor >>= 1;
        multiplicador >>= 1;

        // si el dividendo es mayor o igual a tempDivisor
        if (dividendo >= tempDivisor) {
            // restamos tempDivisor del dividendo
            dividendo -= tempDivisor;
            // sumamos el valor actual de multiplicador al cociente (acumulamos la contribución de la potencia de 2 al cociente final)
            cociente += multiplicador;
        }
    }

    return cociente; // devolvemos el resultado de la división
}

// imprime en la consola el resultado
console.log(divide(100, 30));
