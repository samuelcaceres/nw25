"""
Dada una lista de diccionarios, donde cada diccionario representa un alumno con su nombre y email, escriba una función eliminar_por_email(lista, email) que elimine de la lista al alumno cuyo email coincida con uno dado.
alumnos = [
    {"nombre": "Ana", "email": "ana@gmail.com"},
    {"nombre": "Luis", "email": "luis@gmail.com"},
    {"nombre": "María", "email": "maria@gmail.com"}
]
email_a_eliminar = "luis@gmail.com"

>> eliminar_por_email(alumnos, email_a_eliminar)
.[
    {"nombre": "Ana", "email": "ana@gmail.com"},
    {"nombre": "María", "email": "maria@gmail.com"}
]

"""


"""
  for clave, valor_actual in diccionario.items():
    if valor_actual == valor:
      return clave
  return None
"""


alumnos = [
    {"nombre": "Ana", "email": "ana@gmail.com"},
    {"nombre": "Luis", "email": "luis@gmail.com"},
    {"nombre": "María", "email": "maria@gmail.com"}
]

correo_eliminar = "maria@gmail.com"

elemento_eliminar = ''

for i in alumnos:
    for clave, valor in i.items():
        if i[clave] == correo_eliminar:
            elemento_eliminar = i

print(alumnos)
alumnos.remove(elemento_eliminar)
print(alumnos)