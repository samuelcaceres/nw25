"""
Ejercicio 1: Define s = "Python". Usa un bucle for para imprimir cada carácter de s.
"""
s = "Python"
for c in s:
    print(c)

"""
Ejercicio 2: Define s = "Hola". Usa un bucle for para imprimir cada carácter en mayúscula.
"""
s = "Hola"
for c in s:
    print(c.upper())

"""
Ejercicio 3: Define s = "Mundo". Usa un bucle for para imprimir cada carácter en minúscula.
"""
s = "Mundo"
for c in s:
    print(c.lower())

"""
Ejercicio 4: Define s = "abc". Usa un bucle for para imprimir cada carácter repetido 2 veces.
"""
s = "abc"
for c in s:
    print(c * 2)

"""
Ejercicio 5: Define s = "12345". Usa un bucle for para imprimir cada carácter seguido de un guión.
"""
s = "12345"
for c in s:
    print(c + "-")

"""
Ejercicio 6: Define s = "AEIOU". Usa un bucle for para imprimir cada vocal en minúscula.
"""
s = "AEIOU"
for c in s:
    print(c.lower())

"""
Ejercicio 7: Define s = "python". Usa un bucle for y un contador para imprimir índice y carácter.
"""
s = "python"
index = 0
for c in s:
    print(index, c)
    index += 1

"""
Ejercicio 8: Define s = "Hola". Usa un bucle for para construir una cadena invertida y muéstrala.
"""
s = "Hola"
reversa = ""
for c in s:
    reversa = c + reversa
print(reversa)

"""
Ejercicio 9: Define s = "abracadabra". Usa un bucle for para contar cuántas veces aparece "a" y muestra el recuento.
"""
s = "abracadabra"
contador = 0
for c in s:
    if c == "a":
        contador += 1
print(contador)

"""
Ejercicio 10: Define s = "clonTA". Usa un bucle for y un contador para formar una cadena con caracteres en posiciones pares.
"""
s = "clonTA"
resultado = ""
index = 0
for c in s:
    if index % 2 == 0:
        resultado += c
    index += 1
print(resultado)

"""
Ejercicio 11: Define s = "Hola Mundo". Usa un bucle for para imprimir solo los caracteres que no sean espacios.
"""
s = "Hola Mundo"
for c in s:
    if c != " ":
        print(c)

"""
Ejercicio 12: Define s = "¡Hola!". Usa un bucle for para imprimir "Signo!" cuando el carácter sea "!" y el carácter en otros casos.
"""
s = "¡Hola!"
for c in s:
    if c == "!":
        print("Signo!")
    else:
        print(c)

"""
Ejercicio 13: Define s = "Test". Usa un bucle for para construir una cadena donde cada carácter vaya seguido de un espacio y muéstrala.
"""
s = "Test"
resultado = ""
for c in s:
    resultado += c + " "
print(resultado)

"""
Ejercicio 14: Define s = "Loop". Usa un bucle for para construir una cadena con caracteres separados por guiones y muéstrala.
"""
s = "Loop"
resultado = ""
for c in s:
    resultado += c + "-"
# Eliminar el último guión
resultado = resultado[:-1]
print(resultado)

"""
Ejercicio 15: Define s = "Data". Usa un bucle for para imprimir cada carácter en una línea separada.
"""
s = "Data"
for c in s:
    print(c)
