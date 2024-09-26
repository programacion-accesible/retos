-- Esta función divide números naturales sin usar el signo de división. No se comprueba la división por cero, y se hace división entera.
-- Forma de ejecutar:
-- runghc sukiletxe.hs ejecutará la función Main, directamente.
-- ghci sukiletxe.hs compilará temporalmente y cargará el código en una sesión interactiva, y ahí podremos ejecutar divide con los dos argumentos o main. estando en ghci, podemos salir con :q, y si cambiamos el código podemos recargarlo con :r.
-- ghc sukiletxe.hs compilará el código en ./sukiletxe(.exe), y si ejecutamos eso se ejecutará la función main. Ojo, ghc genera archivos .o y .hi también.
-- Esto no sería necesario, pero explicitamos que la función divide tome dos argumentos enteros y devuelva un entero.
divide :: Int -> Int -> Int
-- Los argumentos de divide son el dividendo y el divisor. Les llamaremos a y b, respectivamente.
divide a b
              -- Si b es 1, devolvemos a, para no dar b vueltas inútilmente.
              | b == 1 = a
              -- Si a es mayor que 0, volvemos a aplicar divide recursivamente, dividiendo (a-b) por b, y sumamos uno al resultado.
              | a > 0 = 1 + (divide (a - b) b)
              -- Si no, devolvemos 0 porque ya hemos acabado de dividir, y el cociente ya se ha calculado en el paso anterior.
              | otherwise= 0

-- La función main es el punto de entrada de nuestro programa, donde se realiza toda la entrada y salida. Lamentablemente no soy capaz de explicar por qué hay que usar let y do, pero el caso es que así funciona bien.
-- Probemos dividiendo dos valores cualquiera. 
main = do
     let a = 6
     let b = 3
     -- show convierte lo que sea a una cadena, ++ concatena cadenas, y putStrLn imprime la cadena completa.
     putStrLn (show a ++ " entre " ++ show b ++ " es " ++ show (divide a b))
