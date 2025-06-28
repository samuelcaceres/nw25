"""
Ejercicio 1: Define s = "Hola Mundo". Reemplaza "Mundo" por "Python" y muestra el resultado.
"""
s = "Hola Mundo"
print(s.replace("Mundo", "Python"))  # Hola Python

"""
Ejercicio 2: Define s = "   Hola   ". Usa strip() para eliminar espacios al inicio y al final y muestra el resultado.
"""
s = "   Hola   "
print(s.strip())  # Hola

"""
Ejercicio 3: Define s = "---Ejercicio---". Usa replace() para eliminar guiones y muestra el resultado.
"""
s = "---Ejercicio---"
print(s.replace("-", ""))  # Ejercicio

"""
Ejercicio 4: Define s = "abracadabra". Usa replace() para cambiar todas las 'a' por 'o' y muestra el resultado.
"""
s = "abracadabra"
print(s.replace("a", "o"))  # obrocodobro

"""
Ejercicio 5: Define s = "Python123". Elimina '1', '2', '3' usando replace() y muestra el resultado.
"""
s = "Python123"
s = s.replace("1", "")
s = s.replace("2", "")
s = s.replace("3", "")
print(s)  # Python

"""
Ejercicio 6: Define s = "(hola)". Usa replace() para eliminar '(' y ')' y muestra el resultado.
"""
s = "(hola)"
print(s.replace("(", "").replace(")", ""))  # hola

"""
Ejercicio 7: Define s = "A B C". Usa replace() para eliminar espacios y muestra el resultado.
"""
s = "A B C"
print(s.replace(" ", ""))  # ABC

"""
Ejercicio 8: Define s = "Por favor". Usa replace() para cambiar espacios por guiones bajos y muestra el resultado.
"""
s = "Por favor"
print(s.replace(" ", "_"))  # Por_favor

"""
Ejercicio 9: Define s = "a-b-c-d-e". Usa replace() para cambiar '-' por '*' y muestra el resultado.
"""
s = "a-b-c-d-e"
print(s.replace("-", "*"))  # a*b*c*d*e

"""
Ejercicio 10: Define s = "banana". Usa replace() para cambiar "na" por "NA" y muestra el resultado.
"""
s = "banana"
print(s.replace("na", "NA"))  # baNANA

"""
Ejercicio 11: Define s = "email@example.com". Usa replace() para cambiar '@' por ' [at] ' y muestra el resultado.
"""
s = "email@example.com"
print(s.replace("@", " [at] "))  # email [at] example.com

"""
Ejercicio 12: Define s = "E-mail: usuario@dominio.com". Usa replace() para eliminar "E-mail: " y muestra el resultado.
"""
s = "E-mail: usuario@dominio.com"
print(s.replace("E-mail: ", ""))  # usuario@dominio.com

"""
Ejercicio 13: Define s = "NoErrorsHere". Usa replace() para cambiar "Errors" por "Problems" y muestra el resultado.
"""
s = "NoErrorsHere"
print(s.replace("Errors", "Problems"))  # NoProblemsHere

"""
Ejercicio 14: Define s = "  trim  ". Usa lstrip() para eliminar espacios a la izquierda y muestra el resultado.
"""
s = "  trim  "
print(s.lstrip())  # "trim  "

"""
Ejercicio 15: Define s = "  trim  ". Usa rstrip() para eliminar espacios a la derecha y muestra el resultado.
"""
s = "  trim  "
print(s.rstrip())  # "  trim"
