# EL JSON es uno de los formatos más populares hoy en día para el intercambio de datos. Es un formato de JavaScript.
# Un objeto JSON y un diccionario de Python son casi idénticos.
# Para manipularlos, Python incluye un módulo para trabajar con JSON.

import json

# Aquí creo un diccionario, que es la forma más fácil de trabajar en Python con JSON.
diccionario = [
    {
        "id": 1,
        "Nombre": "Jane",
        "Pais": "USA",
        "Direccion": "Texas"
    },
    {
        "id": 2,
        "Nombre": "James",
        "Pais": "UK",
        "Direccion": "Londres"
    }
]

# Para convertir a JSON, debemos invocar el método dumps que se encuentra dentro del módulo json.
# json.dumps(DATOS)
datos_json = json.dumps(diccionario)
print(datos_json)
print(type(datos_json))

# Ahora lo guardo como un fichero normal de texto.
# Podemos usar el with, que nos permite tener autocierre.
with open("datos.json", "w") as fichero:
    fichero.write(datos_json)

# Para la inversa, es decir, leer los datos de un JSON y convertirlos a Python, no es muy diferente.
with open("datos.json", "r") as fichero:
    datos_json_file = fichero.read()

print(datos_json_file)
# Lee y lógicamente es un str.
print(type(datos_json_file))

# Ahora vendría el proceso de deserialización, que es justo la inversa de antes. Antes, tomábamos un objeto en Python y lo convertíamos en un string.
# Ahora tomamos un string y lo convertimos en un objeto de Python.
# El módulo json incluye una función llamada loads(DATOS) que realiza ese proceso.
datos_dict_json = json.loads(datos_json_file)
print(type(datos_dict_json))
print(datos_dict_json)

# Ahora ya es una lista y podemos iterarla como queramos.
for item in datos_dict_json:
    print(item)
    print(item["id"])
    print(item["Nombre"])
