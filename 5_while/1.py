"""
Ejercicio 1: Imprime los números del 0 al 4.
"""
i = 0
while i < 5:
    print(i)
    i += 1

"""
Ejercicio 2: Imprime los números del 1 al 5.
"""
i = 1
while i <= 5:
    print(i)
    i += 1

"""
Ejercicio 3: Imprime los números del 3 al 7.
"""
i = 3
while i <= 7:
    print(i)
    i += 1

"""
Ejercicio 4: Imprime los números pares del 0 al 8.
"""
i = 0
while i <= 8:
    print(i)
    i += 2

"""
Ejercicio 5: Suma los números del 1 al 5 y muestra el resultado.
"""
total = 0
i = 1
while i <= 5:
    total += i
    i += 1
print(total)

"""
Ejercicio 6: Multiplica los números del 1 al 4 y muestra el resultado.
"""
producto = 1
i = 1
while i <= 4:
    producto *= i
    i += 1
print(producto)

"""
Ejercicio 7: Concatena la palabra "Hola" tres veces usando while y muestra la cadena.
"""
texto = ""
i = 0
while i < 3:
    texto += "Hola"
    i += 1
print(texto)

"""
Ejercicio 8: Realiza una cuenta regresiva desde 5 hasta 1.
"""
i = 5
while i >= 1:
    print(i)
    i -= 1

"""
Ejercicio 9: Realiza una cuenta regresiva desde 10 hasta 0.
"""
i = 10
while i >= 0:
    print(i)
    i -= 1

"""
Ejercicio 10: Comienza en 2 y, mientras sea menor que 20, imprime el valor y multiplícalo por 2.
"""
n = 2
while n < 20:
    print(n)
    n *= 2

"""
Ejercicio 11: Comienza en 64 y, mientras sea mayor que 1, imprime el valor y divídelo entre 2.
"""
n = 64
while n > 1:
    print(n)
    n //= 2

"""
Ejercicio 12: Usa while para imprimir cada carácter de la cadena "Python".
"""
s = "Python"
i = 0
while i < len(s):
    print(s[i])
    i += 1

"""
Ejercicio 13: Usa while para imprimir los caracteres de la cadena "Python" en orden inverso.
"""
s = "Python"
i = len(s) - 1
while i >= 0:
    print(s[i])
    i -= 1

"""
Ejercicio 14: Comienza en 0 y, mientras sea menor que 10, imprime el número y súmale 3.
"""
i = 0
while i < 10:
    print(i)
    i += 3

"""
Ejercicio 15: Comienza en 5 y, mientras sea mayor que 0, imprime el número y réstale 2.
"""
i = 5
while i > 0:
    print(i)
    i -= 2
