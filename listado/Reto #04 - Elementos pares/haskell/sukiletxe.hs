-- Como veréis esto es muy corto pero bastante lioso.
import Data.List -- Aquí están las funciones sort y group.

-- Un aviso sobre los tipos: no es necesario ponerlos, pero si se ponen ayuda a que el programador y el compilador estén de acuerdo. Se puede también hacer que el programa funcione sin anotaciones de tipos y mirar qué le ha asignado ghc y tirar de ahí.
-- El siguiente tipo se lee: elementosPares recibe una lista de elementos de tipo a (cualquier tipo) que deriven de Ord (es decir que se puedan ordenar).
elementosPares :: Ord a => [a] -> [a]
-- Vamos ahora con lo más difícil, explicando qué hace cada función que se usa.
-- Primero, agrupamos los elementos iguales con (group $ sort) xs, que nos genera una lista de listas de elementos iguales (es decir si tenemos [1,1,2], esto genera [[1,1],[2]]. Esto se lee primero ordena xs y luego agrúpalo. Se ordena primero porque si no no saldría bien, porque group solo agrupa elementos continuos (así que si la entrada estuviese desordenada, podría haber dos grupos para un mismo elemento). El signo de dólar nos permite ahorrarnos paréntesis, tal que group (sort xs) es lo mismo que group $ sort xs.
-- Este agrupamiento se lo pasamos a filter. Filter filtra los elementos de una lista que satisfacen una condición. En este caso, nuestra condición es even.length. Esto se lee de derecha a izquierda, es decir: para que la condición se satisfaga, el elemento tiene que tener una longitud par (pasamos el elemento a length, el resultado lo pasamos a even, y si da True se filtra, si no no).
-- (Lo siento, no sé explicar la diferencia entre el punto y el dólar, sé que a veces son intercambiables y otras no. Sé que el dólar simplemente aplica funciones (f(x) = f $ x) mientras que el punto las une (f(g(x) = (f.g) x), pero no consigo entender las diferencias).
-- Vale, pero esto nos genera una lista de listas (los grupos que decíamos antes), y queremos una lista de elementos que no se repitan. Si sabemos que las sublistas son iguales, podemos coger el primer elemento de cada sublista y devolver eso por cada lista. Así que hacemos eso mismo. Head es una función que devuelve el primer elemento de la sublista que se le pasa, y map lo aplica a cada lista.
elementosPares xs = map head (filter (even.length) (group $ sort xs))
-- Y ya está. Bueno, no. Te preguntarás por qué esto funciona si faltan cosas, en concreto argumentos a funciones, como even . length. Sí, las sublistas que recibe filter. ¿Cómo funcionan? Lo único relacionado  es group xs, que agrupa los elementos, pero ese es el segundo argumento de filter. ¿Entonces? Básicamente porque Haskell admite usar funciones parciales, por lo cual filter se encarga ya de pasar cada elemento a la función que filtra. Si tuviésemos una lista de números y escribiésemos (> 5) como función que filtra iría igual, filtrando solo los elementos mayores que 5.
-- Al hilo de faltar cosas, en pointfree.io se puede convertir cualquier función en este estilo (point-free, es decir, quitando la mayoría de argumentos explícitos). A veces las cosas quedan bastante legibles, otras no tanto. Esta quedaría así (que no está mal):
-- elementosPares = map head . filter (even . length) . group . sort

-- Como quiero ejecutar todos los tests, voy a hacer una función para mostrar los pares.
-- Este tipo, se lee: mostrarPares recibe una lista de elementos de tipo a (cualquier tipo, de nuevo) que derive de Ord (que se puede ordenar) y Show (que se pueda mostrar).
mostrarPares :: (Show a, Ord a) => [a] -> String
mostrarPares xs = "Los elementos pares de " ++ show xs ++ "son " ++ show (elementosPares xs) ++ "."

-- Función principal:
main :: IO()
main = do
     putStrLn $ mostrarPares ["A","B","A","C","C","C","C"]
     putStrLn $ mostrarPares [1,2,3,1,2] 
