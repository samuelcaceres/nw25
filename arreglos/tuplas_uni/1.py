# Ejercicio 1:
# Suma de elementos: Escribe una función que reciba una tupla de números y retorne
# la suma de todos los elementos.
def suma_tupla(t):
    total = 0
    i = 0
    while i < len(t):
        total = total + t[i]
        i = i + 1
    return total

# Ejercicio 2:
# Valor máximo y mínimo: Escribe una función que reciba una tupla de números y
# retorne una tupla con el valor máximo y mínimo.
def valor_max_min_tupla(t):
    maximo = t[0]
    minimo = t[0]
    i = 1
    while i < len(t):
        if t[i] > maximo:
            maximo = t[i]
        if t[i] < minimo:
            minimo = t[i]
        i = i + 1
    return (maximo, minimo)

# Ejercicio 3:
# Concatenación de tuplas: Escribe una función que reciba dos tuplas y devuelva una
# nueva tupla que contenga todos los elementos de ambas tuplas concatenadas.
def concat_tuplas(t1, t2):
    resultado = ()
    i = 0
    while i < len(t1):
        resultado = resultado + (t1[i],)
        i = i + 1
    j = 0
    while j < len(t2):
        resultado = resultado + (t2[j],)
        j = j + 1
    return resultado

# Ejercicio 4:
# Conteo de elementos: Escribe una función que reciba una tupla y un elemento, y
# devuelva la cantidad de veces que aparece el elemento en la tupla. No uses count.
def contar_elemento_tupla(t, e):
    contador = 0
    i = 0
    while i < len(t):
        if t[i] == e:
            contador = contador + 1
        i = i + 1
    return contador

# Ejercicio 5:
# Tupla invertida: Escribe una función que reciba una tupla y devuelva una nueva tupla
# con los elementos en orden inverso.
def tupla_invertida(t):
    resultado = ()
    i = len(t) - 1
    while i >= 0:
        resultado = resultado + (t[i],)
        i = i - 1
    return resultado

# Ejercicio 6:
# Ubicar un elemento: Escribe una función que reciba una tupla ordenada y un elemento,
# y devuelva otra tupla con el elemento insertado en orden en la tupla.
def insertar_en_tupla_ordenada(t, e):
    resultado = ()
    inserted = False
    i = 0
    while i < len(t):
        if not inserted and e <= t[i]:
            resultado = resultado + (e,)
            inserted = True
        resultado = resultado + (t[i],)
        i = i + 1
    if not inserted:
        resultado = resultado + (e,)
    return resultado

# Ejercicio 7:
# Comparación de tuplas: Escribe una función que compare dos tuplas y devuelva True
# si son iguales (misma longitud y mismos elementos) y False en caso contrario.
def tuplas_iguales(t1, t2):
    if len(t1) != len(t2):
        return False
    i = 0
    while i < len(t1):
        if t1[i] != t2[i]:
            return False
        i = i + 1
    return True

# Ejercicio 8:
# Tuplas anidadas: Crea una función que reciba 2 tuplas y retorne otra tupla con
# ambas tuplas dentro de ella.
def anidar_tuplas(t1, t2):
    return (t1, t2)

# Ejercicio 9:
# Eliminación de elementos duplicados: Escribe una función que tome una tupla y
# elimine los elementos duplicados, devolviendo una nueva tupla sin duplicados.
def eliminar_duplicados(t):
    resultado = ()
    i = 0
    while i < len(t):
        elem = t[i]
        j = 0
        existe = False
        while j < len(resultado):
            if resultado[j] == elem:
                existe = True
            j = j + 1
        if not existe:
            resultado = resultado + (elem,)
        i = i + 1
    return resultado

# Ejercicio 10:
# Ordenamiento de tuplas: Escribe una función que tome una lista de tuplas,
# donde cada tupla contiene un nombre y una edad, y devuelva una nueva lista de tuplas
# ordenada por edad de forma ascendente.
def ordenar_por_edad(lista):
    copia = []
    i = 0
    while i < len(lista):
        copia = copia + [lista[i]]
        i = i + 1
    n = len(copia)
    m = 0
    while m < n - 1:
        j = 0
        while j < n - 1 - m:
            if copia[j][1] > copia[j + 1][1]:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp
            j = j + 1
        m = m + 1
    return copia
