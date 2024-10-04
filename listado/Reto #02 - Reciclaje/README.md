# Reciclaje

Este reto ha sido adaptado de un concurso de Euskal Code, una organización vasca que hacía concursos de programación. El reto original lo subieron a [Hacker Rank](https://www.hackerrank.com/), pero no lo encuentro en la plataforma. La organización parece que ya no existe (no tiene web pero sí Twitter, aunque ya no publican).

## Enunciado

¿Sabías que antes se incentivaba al reciclaje devolviendo parte del costo de un producto (cerveza, por ejemplo) devolviéndote parte de su precio cuando devolvías el recipiente vacío? Así, se incentivaba a que la gente devolviese recipientes que luego se reciclaban.

Queremos hacer un programa que imite esto mismo. Para hacerlo puedes usar el lenguaje que quieras.

Te proponemos dos opciones: una, hacer que cada producto cueste dos monedas, que cada recipiente devuelto te devuelvan una, y que tengas 10 monedas al iniciar; o bien, que pidas al usuario que indique estas tres cosas.

Sea como sea, deberás hacer que el programa realice las acciones pertinentes (comprar productos y devolver recipientes vacíos) hasta que no pueda seguir. A continuación, pego una salida del mío (que no tienes por qué imitar siempre que tu salida aclare qué estás haciendo en cada momento), yo lo he hecho con helados porque así me aparecía en el reto original:

```
¿Cuánto vale un helado? 3
¿Cuánto me devuelven por una tarrina? 1
¿Cuánto dinero tengo? 20
He comprado un helado, ahora tengo 1 helados y 17 monedas.
He comprado un helado, ahora tengo 2 helados y 14 monedas.
He comprado un helado, ahora tengo 3 helados y 11 monedas.
He comprado un helado, ahora tengo 4 helados y 8 monedas.
He comprado un helado, ahora tengo 5 helados y 5 monedas.
He comprado un helado, ahora tengo 6 helados y 2 monedas.
He cambiado una tarrina, ahora tengo 5 tarrinas y 3 monedas.
He cambiado una tarrina, ahora tengo 4 tarrinas y 4 monedas.
He cambiado una tarrina, ahora tengo 3 tarrinas y 5 monedas.
He cambiado una tarrina, ahora tengo 2 tarrinas y 6 monedas.
He cambiado una tarrina, ahora tengo 1 tarrinas y 7 monedas.
He cambiado una tarrina, ahora tengo 0 tarrinas y 8 monedas.
He comprado un helado, ahora tengo 1 helados y 5 monedas.
He comprado un helado, ahora tengo 2 helados y 2 monedas.
He cambiado una tarrina, ahora tengo 1 tarrinas y 3 monedas.
He cambiado una tarrina, ahora tengo 0 tarrinas y 4 monedas.
He comprado un helado, ahora tengo 1 helados y 1 monedas.
He cambiado una tarrina, ahora tengo 0 tarrinas y 2 monedas.
```

Si quieres, al final, puedes indicar cuántos productos has comprado, que era, probablemente, lo que en última instancia pedían en el reto original.

## Cómo enviar

* Clona el repositorio y envía una pull request con tu solución.
* Si no existe una carpeta para el lenguaje en el que lo implementas, créala.
* Llama al archivo con tu nombre de usuario.

