# **Agua para Programadores**

Este reto ha sido una adaptación propia del original ubicado en la web [CodeForces](https://codeforces.com) donde hay retos de programación competitiva.

El reto original está en inglés y tiene el identificador [Reto 1118A](https://codeforces.com/problemset/problem/1118/A).  

## Enunciado
Un grupo de amigos programadores necesita comprar **N** litros de agua. En la tienda más cercana solo hay dos tipos de botellas:  
- Botellas de 1 litro  
- Botellas de 2 litros

Las botellas de 1 litro están hechas de un vidrio especial que se puede reciclar, pero es muy **sensible**, por lo que no pueden ser transportadas junto a las botellas de 2 litros. La tienda tiene una cantidad infinita de botellas para el cliente.

La botella del primer tipo cuesta **A** dólares y la botella del segundo tipo cuesta **B** dólares. Además, lamentablemente, el grupo de amigos programadores solo dispone de una mochila en la que deben guardar todas las botellas que compren.  

Su mochila es de la marca "Knaspack", muy conocida entre las personas aficionadas a la tecnología.

Tu tarea es encontrar la cantidad mínima de dinero (dólares) que el grupo de amigos necesita para comprar exactamente **N** litros de agua en la tienda, dado que la botella de 1 litro cuesta **A** dólares y la de 2 litros cuesta **B** dólares.

Los tres datos de entrada que recibe el programa son:
- **N**: un entero entre 1 y 10 elevado a 12 (ambos inclusive).
- **A**: un entero entre 1 y 1000 (ambos inclusive).
- **B**: un entero entre 1 y 1000 (ambos inclusive).

### Ejemplo de entrada y salida

#### Ejemplo 1
```
Ingrese la cantidad de litros (N): 1  
Ingrese el costo de la botella de 1 litro (A): 1000  
Ingrese el costo de la botella de 2 litros (B): 1  
El costo mínimo para comprar 1 litro de agua es: 1000 dólares
```

#### Ejemplo 2
```
Ingrese la cantidad de litros (N): 10  
Ingrese el costo de la botella de 1 litro (A): 1  
Ingrese el costo de la botella de 2 litros (B): 3  
El costo mínimo para comprar 10 litros de agua es: 10 dólares
```

#### Ejemplo 3
```
Ingrese la cantidad de litros (N): 1000000000000  
Ingrese el costo de la botella de 1 litro (A): 42  
Ingrese el costo de la botella de 2 litros (B): 8  
El costo mínimo para comprar 1000000000000 litros de agua es: 42000000000000 dólares
```

## ¿Cómo participar?

- Clona el repositorio y envía un pull request con tu solución.
- Si no existe una carpeta para el lenguaje en el que implementas la solución, créala.
- Llama al archivo con tu nombre de usuario de github.
