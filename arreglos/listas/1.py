numeros = [1,2,3,4]

def sumatoria_lista(lista):
    sumatoria = 0
    for i in lista:
        sumatoria += i
    return sumatoria

llamada = sumatoria_lista(numeros)
         
print('Print de llamada', llamada)