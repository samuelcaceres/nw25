"""
Ejercicio 1: Crear archivos tabla-1.txt ... tabla-9.txt con la tabla de multiplicar del 1 al 9.
"""
for n in range(1, 10):
    archivo = open("tabla-" + str(n) + ".txt", "w")
    for i in range(1, 11):
        archivo.write(str(n) + " x " + str(i) + " = " + str(n * i) + "\n")
    archivo.close()

"""
Ejercicio 2: Pedir un número entre 1 y 9, leer el archivo tabla-n.txt y mostrar su contenido.
"""
n = int(input("Introduce un número (1-9): "))
archivo = open("tabla-" + str(n) + ".txt", "r")
lineas = archivo.readlines()
archivo.close()
for linea in lineas:
    print(linea, end="")

"""
Ejercicio 3: Pedir dos números n (1-9) y m (1-10), leer tabla-n.txt y mostrar solo la línea m.
"""
n = int(input("Introduce n (1-9): "))
m = int(input("Introduce m (1-10): "))
archivo = open("tabla-" + str(n) + ".txt", "r")
lineas = archivo.readlines()
archivo.close()
print(lineas[m-1], end="")

"""
Ejercicio 4: Pedir la ruta de un archivo y mostrar cuántas líneas contiene.
"""
ruta = input("Introduce la ruta del archivo: ")
archivo = open(ruta, "r")
lineas = archivo.readlines()
archivo.close()
print("Número de líneas:", len(lineas))