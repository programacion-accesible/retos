# **cocinando la lasaña**

Este reto es tomado de la plataforma [Exercism](https://exercism.org/), misma que está repleta de ejercicios de programación en más de 70 lenguajes y las soluciones son revisadas por personas

## Enunciado

Vas a escribir un código que te ayudará a cocinar una lasaña espectacular a partir de tu libro de cocina favorito.

Tienes cinco tareas, todas relacionadas con la preparación de tu receta.

1. **Define el tiempo de horneado esperado en minutos como una constante**  
   Define la constante `EXPECTED_BAKE_TIME` que representa cuántos minutos debe hornearse la lasaña en el horno. Según tu recetario, la lasaña debe estar en el horno durante 40 minutos:

   ```código
   print(EXPECTED_BAKE_TIME)
   Salida: 40
   ```

2. **Calcula el tiempo de horneado restante en minutos**  
   Completa la función `bake_time_remaining()` que toma los minutos reales que la lasaña ha estado en el horno como argumento y devuelve cuántos minutos aún necesita la lasaña para hornearse según la constante `EXPECTED_BAKE_TIME`.

   ```código
   bake_time_remaining(30)
   Salida: 10
   ```

3. **Calcula el tiempo de preparación en minutos**  
   Define la función `preparation_time_in_minutes()` que toma el número de capas que quieres agregar a la lasaña como argumento y devuelve cuántos minutos tardarías en prepararlas. Supón que cada capa tarda 2 minutos en prepararse.

   ```código
   preparation_time_in_minutes(2)
   Salida: 4
   ```

4. **Calcular el tiempo total de cocción transcurrido (preparación + horneado) en minutos**  
   Define la función `elapsed_time_in_minutes()` que toma dos parámetros como argumentos: `number_of_layers` (la cantidad de capas agregadas a la lasaña) y `elapsed_bake_time` (la cantidad de minutos que la lasaña ha estado horneándose en el horno). Esta función debe devolver la cantidad total de minutos que ha estado cocinando, o la suma de su tiempo de preparación y el tiempo que la lasaña ya ha pasado horneándose en el horno.

   ```código
   elapsed_time_in_minutes(3, 20)
   Salida: 26
   ```

5. **Actualizar la receta con notas**  
   Regresa a la receta y agrega "notas" en forma de docstrings en las funciones.
6. **Añade pruebas unitarias para cada una de las funciones que diseñes.**
   Utiliza el módulo unittest para añadir las pruebas unitarias. Esto en el mismo archivo.

---

**Fuente**  
[Exercism](https://exercism.org/)

**Creado por**  
[BethanyG](https://github.com/BethanyG)


## ¿Cómo participar?

- Clona el repositorio y envía un pull request con tu solución.
- Si no existe una carpeta para el lenguaje en el que implementas la solución, créala.
- Llama al archivo con tu nombre de usuario de github.