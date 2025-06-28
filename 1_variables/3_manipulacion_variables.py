# "Ejercicio 1: Define `a = 10`. Crea `b` copiando el valor de `a` y muestra `b`."
a = 10
b = a
print(b)  # 10

# "Ejercicio 2: Asigna en una sola línea `x = 5` y `y = 8`. Muestra `x` y `y`."
x, y = 5, 8
print(x, y)  # 5 8

# "Ejercicio 3: Asigna el mismo valor `7` a `m`, `n` y `p` (en una línea) y muestra los tres."
m = n = p = 7
print(m, n, p)  # 7 7 7

# "Ejercicio 4: Intercambia los valores de `a = 1` y `b = 2` usando una variable temporal y muestra `a`, `b`."
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)  # 2 1

# "Ejercicio 5: Intercambia `a = 3` y `b = 4` sin usar variable temporal y muestra el resultado."
a = 3
b = 4
a, b = b, a
print(a, b)  # 4 3

# "Ejercicio 6: Inicializa `c = 5`. Súmale 1 usando `c += 1` y muestra `c`."
c = 5
c += 1
print(c)  # 6

# "Ejercicio 7: Define `d = 5`. Réstale 2 usando `d -= 2` y muestra `d`."
d = 5
d -= 2
print(d)  # 3

# "Ejercicio 8: Pon `x = 10`. Reasigna directamente `x = 20` y muestra `x`."
x = 10
x = 20
print(x)  # 20

# "Ejercicio 9: Define `a = 4` y `b = 6`. Crea `suma = a + b` y muestra `suma`."
a = 4
b = 6
suma = a + b
print(suma)  # 10

# "Ejercicio 10: Inicializa `p = 7`, `q = 3`. Crea `producto = p * q` y muestra `producto`."
p = 7
q = 3
producto = p * q
print(producto)  # 21

# "Ejercicio 11: Pon `v1 = 10` y `v2 = 20`. Calcula `promedio = (v1 + v2) / 2` y muestra `promedio`."
v1 = 10
v2 = 20
promedio = (v1 + v2) / 2
print(promedio)  # 15.0

# "Ejercicio 12: Inicializa `n = 5`. Cámbiala con `n = n + 3` y muestra `n`."
n = 5
n = n + 3
print(n)  # 8

# "Ejercicio 13: Define `base = 3` y `altura = 4`. Crea `area = base * altura` y muestra `area`."
base = 3
altura = 4
area = base * altura
print(area)  # 12

# "Ejercicio 14: Pon `original = 8`. Haz `copia = original` y luego `copia += 2`. Muestra `original` y `copia`."
original = 8
copia = original
copia += 2
print(original, copia)  # 8 10

# "Ejercicio 15: Haz una secuencia: `a = 2`, luego `b = a * 3`, luego `c = b + 5`. Muestra `a, b, c`."
a = 2
b = a * 3
c = b + 5
print(a, b, c)  # 2 6 11
