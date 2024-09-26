/* 
Solución creada por el usuario JohanAnim.
Para el reto de Adivina el número que es el 3, en esta ocación con el lenguaje de programación C#.
*/

using System;

// la clase de la logica del juego
public class AdivinaMiNumero
{
    private int numeroSecreto;
    private int vidas;
    private int nivel;

    public AdivinaMiNumero(int nivel)
    {
        this.nivel = nivel;
        EstablecerVidas();
        GenerarNumeroSecreto();
    }

    private void EstablecerVidas()
    {
        switch (nivel)
        {
            case 1:
                vidas = 6;
                break;
            case 2:
                vidas = 8;
                break;
            case 3:
                vidas = 10;
                break;
            default:
                vidas = 6; // Valor por defecto
                break;
        }
    }

    private void GenerarNumeroSecreto()
    {
        Random random = new Random();
        int rangoSuperior = nivel == 3 ? 200 : nivel * 50; // Ajustar el nivel 3 a un rango superior de 200
        numeroSecreto = random.Next(1, rangoSuperior + 1);
        Console.WriteLine($"¡Estoy pensando en un número entre 1 y {rangoSuperior}! ¿Puedes adivinarlo?");
    }

    public bool Adivinar(int numero)
    {
        if (numero == numeroSecreto)
        {
            Console.WriteLine("¡Felicidades! ¡Lo has logrado!");
            return true;
        }
        else
        {
            vidas--; // Reducir vidas solo si no adivina correctamente
            if (vidas > 0)
            {
                Console.WriteLine($"¡Nooo! Ese no es. Te quedan {vidas} vidas.");
                Console.WriteLine(numero < numeroSecreto ? "Mi número es más grande." : "Mi número es más pequeño.");
            }
            return false;
        }
    }

    public bool JuegoTerminado()
    {
        if (vidas == 0)
        {
            Console.WriteLine("Te has quedado sin vidas.");
            MostrarNumeroSecreto(); // Mostrar el número secreto al final
            return true;
        }
        return false;
    }

    public void MostrarNumeroSecreto()
    {
        Console.WriteLine($"Mi número era: {numeroSecreto}");
    }
}

class Program
{
    static void Main(string[] args)
    {
        bool quiereJugar = true;

        while (quiereJugar)
        {
            Jugar();

            // Preguntar si quiere jugar de nuevo
            Console.WriteLine("¿Quieres volver a jugar? (s/n): ");
            string respuesta = Console.ReadLine().ToLower();
            quiereJugar = respuesta == "s";
        }

        Console.WriteLine("¡Gracias por jugar!");
    }

    static void Jugar()
    {
        Console.WriteLine("¡Bienvenido al juego Adivina mi número!");

        int nivel = 1;
        AdivinaMiNumero juego;

        while (nivel <= 3)
        {
            Console.WriteLine($"¡Bienvenido al nivel {nivel}!");
            juego = new AdivinaMiNumero(nivel);

            bool nivelCompletado = false;
            while (!juego.JuegoTerminado() && !nivelCompletado)
            {
                Console.Write("Ingresa tu número: ");
                if (int.TryParse(Console.ReadLine(), out int numeroAdivinado))
                {
                    if (numeroAdivinado < 1 || numeroAdivinado > (nivel == 3 ? 200 : nivel * 50)) // Ajustar el límite superior del nivel 3
                    {
                        Console.WriteLine($"El número debe estar entre 1 y {(nivel == 3 ? 200 : nivel * 50)}");
                    }
                    else
                    {
                        nivelCompletado = juego.Adivinar(numeroAdivinado);
                    }
                }
                else
                {
                    Console.WriteLine("Entrada inválida. Por favor, ingresa un número entero.");
                }
            }

            if (!juego.JuegoTerminado())
            {
                nivel++; // Avanzar al siguiente nivel
            }
            else
            {
                break; // Terminar el juego si se quedan sin vidas
            }
        }

        if (nivel > 3)
        {
            // Mensaje especial cuando se completan todos los niveles
            Console.WriteLine("¡Felicidades! Has completado todos los niveles. ¡Eres un maestro de adivinanzas!");
        }
    }
}
