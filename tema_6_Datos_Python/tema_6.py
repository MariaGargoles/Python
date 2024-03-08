# Manejo de ficheros en Python
# Tenemos una serie de funciones que nos permiten la manipulación de ficheros.
# Son algo un poco "antiguo", pero se siguen usando sin ningún problema.
# La primera función es la función open("RUTA", "MODO") y devuelve un objeto que nos permite manipular el fichero.
# RUTA => la ruta donde se almacena el fichero
# MODO => modo de apertura
#    r => lectura
#    w => crea el fichero y si existe lo sobrescribe
#    a => append, es apertura para incluir contenido al final
# Los modos se pueden combinar y además le podemos indicar con una 'b' si vamos a trabajar en binario, sino por defecto trabajamos con ficheros de texto.

fichero = open("mi_fichero.txt", "w")
# El primer método es el método write(CONTENIDO)
fichero.write("Hola Mundo\n")
fichero.write("Adios Mundo")
# Siempre que los abrimos, cuando acabemos de trabajar con ellos, los debemos cerrar.
fichero.close()

# Una vez creado, podemos leerlo.
fichero = open("mi_fichero.txt", "r")
# Para leer, si tenemos varias alternativas.
# Con el método read() lee toda la información del fichero.
datos = fichero.read()
print(datos)
fichero.close()

print("*************************** Leer línea a línea ************************************")
# Podemos también leer línea a línea.
# El método .readline() lee una línea y mueve el cursor.
fichero = open("mi_fichero.txt", "r")
print(fichero.readline(), end="")
print(fichero.readline(), end="")
# Si intentamos leer más líneas de las que hay, no hace nada.
print(fichero.readline(), end="")
fichero.close()

print("*************************** El objeto file es iterable ************************************")
fichero = open("mi_fichero.txt", "r")

for linea in fichero:
    print(linea, end="")

fichero.close()

print("*************************** Tenemos un cursor ************************************")
fichero = open("mi_fichero.txt", "r")

# tell() nos devuelve la posición del cursor en bytes.
print(fichero.tell())
print(fichero.readline(), end="")
print(fichero.tell())
# Para modificar la posición del cursor, podemos usar el seek() que recibe el desplazamiento que le queremos dar al cursor.
fichero.seek(5)
print(fichero.tell())
# El método read lee a partir de ese punto.
print(fichero.read())

fichero.close()
