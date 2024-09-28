#include <stdio.h>

// Como no estoy nada seguro de si los mins que trae C (que van con números reales) soportarían la precisión long long int, voy a implementar una. Porque puedo.
// También digo que es probable que con unos doubles esto fuese perfectamente, pero ya que puedo usar enteros para todo, usemos enteros.
// Con doubles haría falta redondear para quitar el .0 a todos los mensajes, cosa que no tengo claro cómo hacer, aunque es posible que simplemente un `(long long int) a` y manteniendo las cadenas de formatos exactamente igual aquello fuese bien.

long long unsigned int llumin(long long unsigned int a, long long unsigned int b) {
    return a < b? a: b;
}

int main(void) {
    unsigned long long n, coste_minimo; // Vamos a ser puristas, utilizando estos enteros para todo. Con enteros más pequeños esto no iría, fallaría el último test. El unsigned no es importante, pero nos permite tener el doble de números, aunque son innecesarios según cómo nos los acotan en el ejercicio.
    int a, b; // Pero no tanto, no nos importa que los dólares no tengan signo, nos ahorraríamos solo un bit.
    printf("Ingrese la cantidad de litros (N): ");
    scanf("%llu", &n);
    printf("Ingrese el costo de la botella de 1 litro (A): ");
    scanf("%d", &a);
    printf("Ingrese el costo de una botella de 2 litros (B): ");
    scanf("%d", &b);
    // Si las botellas no son divisibles por dos, devolvemos siempre la cuenta con las de un litro porque no se pueden mezclar.
    if (n % 2 != 0) {
        coste_minimo = a * n;
        } else {
            // Si no, calculamos el coste mínimo y lo devolvemos.
            coste_minimo = llumin(a*n, (b*n)/2);
        }
    printf("El costo mínimo para comprar %llu botellas de agua es: %llu dólares\n", n, coste_minimo);
return 0;    
}
