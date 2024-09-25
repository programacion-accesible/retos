

let monedas = 10;
let helados = 0;
let recipientes = 0;

const comprar = () => {
    console.info(`Tienes ${monedas} monedas, ${helados} helados y ${recipientes} recipientes.`);
    while (monedas >=2) {
        helados+= 1;
        recipientes+=1;
        monedas -=2;
        console.info(`Tienes ${monedas} monedas, ${helados} helados y ${recipientes} recipientes.`);
        
    }

}

const reciclar = () => {
    // let devolucion = 1;
    while (recipientes>0) {
        recipientes-= 1;
        monedas+=1;
        console.info(`Reciclaste 1 recipiente . Ahora tienes: ${recipientes} Ganaste 1 monedas y ahora tienes: ${monedas}`);
    }
}



while (monedas >=2 || recipientes >0) {
    comprar();

    reciclar();    
}

