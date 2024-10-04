# **Ocultando números**

Este reto es una adaptación propia y se utiliza en los cursos de Programación de [Capacitadero](https://www.facebook.com/capacitadero), su referencia más cercana es un ejercicio utilizado en el curso de Programación 1 para las carreras de ingenieria de la UTEC en Perú. Se desconoce el origen real de la propuesta. 

## Enunciado
Usted es un programador con experiencia y quiere obtener un trabajo siendo parte de algún equipo tecnológico en la área de investigación. Es por ello que encontró una oportunidad del **Technion – Israel Institute of Technology** . Este instituto viene reclutando programadores que quieran dar el primer paso a la investigación en tecnologia y algoritmos. Israel viene teniendo conflictos politicos y sociales con sus vecinos paises, es por ello que desea desarrollar algoritmos que oculten los mensajes. Como sabemos, el sonido, las imágenes y los videos son representados por números para las computadoras. Es por ello que el gobierno de Israel viene desarrollando algoritmos matemáticos que tienen tres fases:
- Fase 1: consiste en convertir un elemento digital a su valor numérico conocido. Ejemplo: si tienes una imagen, cada pixel es representado por un conjunto de números.
- Fase 2: consiste en convertir cada unidad numérica (pixel) en un número desconocido.
- Fase 3: transformación de la unidad numérica por medio de funciones de hash criptográficas. En esta fase trabajan los cientificos de mayor experiencia. 

Usted, dado que usted es una persona con demostrada responsabilidad y honestidad, esta postulando para ser parte de los nuevos cientificos que se integraran a la Fase 2. 

Entonces, al asistir a su primera entrevista virtual, el área de recursos humanos le ha solicitado que analice el siguiente algoritmo y lo desarrolle en su lenguaje favorito. Su computadora se encuentra compartiendo pantalla. **Usted comienza con 100 puntos, por cada búsqueda que realice en internet, para solucionar su desafio, se le va a descontar 20 puntos**. Los programadores que ingresan a trabajar con frecuencia, sólo realizan una consulta como máximo, por internet. No hay limite de tiempo pero su honestidad es muy importante, si algo extraño sucede sera automaticamente rechazado y no podra postular a ningún equipo del Technion durante 10 años. 

El algoritmo usado para esta entrevista se le llama **Ocultando números**. Este algoritmo recibe como valor de entrada un número entero, lo procesa y devuelve otro número entero llamado R. 

R es una suma, donde cada par de dígitos del valor de entrada contribuye con la suma de sus divisores propios excepto 1 y el mismo número. 
Por ejemplo, para el número 341511:
- 34 tiene 2 divisores propios (2 y 17), por lo que su contribución es 19.
- 15 tiene 2 divisores 3 y 5, por lo que su contribución es 8.
- 11 tiene 0 divisores, por lo que su contribución es 0
Por tanto, el mensaje oculto en 341511 es 27 (19 + 8 + 0).

Para este algoritmo se asume que siempre los valores de entrada seran números enteros positivos con una cantidad par de dígitos. El número no comenzará con 0. Además, para esta etapa de la entrevista la complejidad algoritmica no es evaluada. 

### Ejemplo de entrada y salida

#### Ejemplo 1
```
Input: 
341511  
Output:
27
```

#### Ejemplo 2
```
Input:
341516
Output:
41
```

#### Ejemplo 3
```
Input:
3445
Output:
51
```

## ¿Cómo participar?

- Clona el repositorio y envía un pull request con tu solución.
- Si no existe una carpeta para el lenguaje en el que implementas la solución, créala.
- Llama al archivo con tu nombre de usuario de github.
