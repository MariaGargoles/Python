#Estructuras de control
# La primera if - elif -else

variable = 10

#para indicar los bloques con identacion
if variable == 10:
    print("Es 10")

print("Despues")

#Podemos tener elif para evaluar mas condiciones, y su evaluacion es en cascada.
#si encuentra una que cumple no evalua las demas.
variable = 20

#para indicar los bloques con identacion.
if variable == 10:
    print("Es 10")
elif variable == 20:
    print("variable es 20")
elif variable == 30:
    print("variable es 30")

#pueden existir un else al final de todo
variable = 10

#para indicar los bloques con identacion
if variable == 10:
    print("Es 10")
else:
    print("no es 10")


variable = 209

#para indicar los bloques con identacion
if variable == 10:
    print("Es 10")
elif variable == 20:
    print("variable es 20")
elif variable == 30:
    print("variable es 30")
else:
    print("No es ninguna de las anteriores")

#Python soporta el estilo de comparacion matematico para la pertenencia de rangos

variable = 2

if(1 <= variable <= 10):
    print("esta entre 1 y 10")

#Esto seria equivalente a una condicion compuesta
variable = 2
if ((variable >= 1) and (variable <=10)):
     print("esta entre 1 y 10")

#Operadores de comparacion
print(1 == 1) #igualdad
print(1 != 11) #distinto
print(1 > 11) #mayor
print(1 >= 11) #mayor o igual
print(1 < 11) #menor
print(1 <= 11) #menor o igual

#La evaluacion de los if, en python esta cortocircuitada
a = 10
b = 0
#si puede inferir el resultado final no sigue evaluando
print( a != 10 and a/b)


#If ternario mas o menos, se usa para inicializacion de variables
# valor = VALOR_EN_CASO_TRUE if CONDICION else VALOR_EN_CASO_FALSO
variable = 10
valor = "Si es 10" if variable == 10 else "No es 10"
print(valor)

#Se pueden concatenar todos los que quieras, pero no es recomendable
variable = 10
valor = "Si es mayor que 10" if variable > 10 else "Es menor de 10" if variable != 10 else "Es 10"
print(valor)

#Equivalente con if "normal"
variable = 10
if variable != 10:
    if variable > 10: 
        valor = "Si es mayor que 10"
    else:
        valor = "Es menor de 10"
else:
    valor = "Es 10"

print(valor)

#Bucles
#While se ejecuta mientas se cumple la condicion, IMPORTANTE que la condicion deje de cumplirse en algun momento

variable = 10
#No se ejecuta porque ya no se cumple la primera vez
while variable < 10:
    print(variable)


variable = 1
#Esto es infito porque la condicion nunca deja de cumplirse
while variable < 10:
    print(variable)

#la forma correcta
variable = 1

while variable < 10:
    print(variable)
    variable = variable + 1

#Los while en pytjon pueden llevar un else
#este bloque else se ejecuta cuando al condicion es alcanzada
variable = 1

while variable < 10:
    print(variable)
    variable = variable + 1
else:
    print("Ha terminado con exito")

#Ojo la diferencia se vera cuando usemos break
variable = 1

while variable < 10:
    print(variable)
    variable = variable + 1
print("Ha terminado con exito")

#Otro bucle es el for que se usa para iterar sobre elmentos iterables (listas, strings, diccionarios, tuplas..)
#for TEMPORAL in ITERABLE:

lista = [1,2,3,4]
for numero in lista:
    print(numero)

cadena = "hola mundo"
for letra in cadena:
    print(letra)

tuplas = (1,2,3,4)
for numero in tuplas:
    print(numero)

diccionarios = {"nombre": "James", "apellido":"Bond"}
for clave in diccionarios:
    print(clave)
    print(diccionarios[clave])

diccionarios = {"nombre": "James", "apellido":"Bond"}
for valores in diccionarios.values():
    print(valores)

diccionarios = {"nombre": "James", "apellido":"Bond"}
for clave,valor in diccionarios.items():
    print("La clave es", clave,"El valor es", valor)

#Tenemos la funcion range(INICIO, FIN, STEP) para generar rangos de nuemeros enteros
#que podemos usar con el for
#INICIO => valor de inicio, por defecto 0
#FIN => valor de fin, obligatorio, igual que en el slice no se inclue
#STEP => el numero de saltos entre numeros consecutivos, por defecto es 1

for numero in range(10):
    print(numero)

for numero in range(5,10):
    print(numero)

for numero in range(1,10,2):
    print(numero)

#El for tambien admite un else que se ejecutara al finalizar la iteracion

for numero in range(10):
    print(numero)
else:
    print("He acabado")

#Tenemos 3 palabras reservadas
# pass => que es la instruccion vacia no hace nada
if True:
    pass
print("ola")

#break, que solo funciona dentro de un bucle while o for, y le fuerza la salida incondicional
for numero in range(10):
    print(numero)
    break
else:
    print("si el bucle sale con un break este else no se ejecuta")

#Normalmegte este break se ponde dento de un if
for numero in range(10):
    print(numero)
    if numero > 4:
        break

#continue, devuelve el control del flujo del bucle while a la condicion

variable = 10
while variable > 0:
    print(variable)
    continue
    variable = variable - 1


#igual que el break se puede poner dentro de un if
variable = 10
while variable > 0:
    variable = variable - 1
    if variable < 5:
        continue
    print(variable)
    

#Introduccion de valores por teclado
#python tiene una funcion input
# variable = input(PROMT)
nombre = input("Introduce tu nombre ")
print(nombre)

#Siempre devuelve un string
numero = input("Introduce tu numero ")
print(numero)
print(type(numero))

#Para leer numero debemos convertirlo, para ello podemos usar las funciones float(), int(), bool()
numero = int(input("Introduce tu numero "))
print(numero)
print(type(numero))

#o bien
entrada = input("Introduce tu numero ")
if entrada.isnumeric():
    numero = int(entrada)
    print(numero)
    print(type(numero))
else:
    print("Has metido mal el numero")

#Podemos insistir
entrada = input("Introduce tu numero ")
while not entrada.isnumeric():
    entrada = input("Error introduce tu numero ")
numero = int(entrada)
print(numero)
print(type(numero))
