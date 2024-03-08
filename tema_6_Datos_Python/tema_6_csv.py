# El formato CSV es un formato columnar, que se usa para el intercambio de información.
# Al igual que JSON, tenemos un módulo que ya viene instalado con Python para la manipulación de los CSV.
import csv

# Como el CSV es un formato columnar, empezamos por definir las columnas.
csv_columnas = ["id", "nombre", "Pais"]

# Para definir datos a guardar es mejor usar una lista de diccionarios.
# OJO: Los nombres de las claves deben coincidir con los nombres de las columnas.
dict_data = [
    {
        "id": 1,
        "nombre": "Jane",
        "Pais": "USA"
    },
    {
        "id": 2,
        "nombre": "James",
        "Pais": "UK"
    }
]

# Procedemos a trabajar con el fichero.
with open("prueba.csv", "w", newline="") as csvfile:
    # Hasta aquí es similar a trabajar con un fichero de texto.
    # Para poder escribir el diccionario en el fichero, debemos crear un objeto del tipo DictWriter.
    # fieldnames se usa para definir el nombre de las columnas.
    writer = csv.DictWriter(csvfile, fieldnames=csv_columnas)
    
    # Debemos invocar el método writeheader en el writter para que escriba las columnas.
    writer.writeheader()
    
    # Ahora hacemos un bucle para escribir cada dato.
    for dato in dict_data:
        writer.writerow(dato)

# Para leer es parecido, solo que debemos crear un objeto del tipo DictReader.
with open("prueba.csv", "r") as fichero:
    datos = csv.DictReader(fichero)
    
    # Ya tenemos el contenido cargado.
    print(type(datos))
    print(datos)
    
    # El objeto DictReader es iterable.
    for fila in datos:
        print(fila)
        print(type(fila))
        print(fila["nombre"])
