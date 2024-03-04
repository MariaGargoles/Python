# Estructuras de control
# La primera if - elif - else

variable = 10

# para indicar los bloques con identación
if variable == 10:
    print("Es 10")

print("Después")

# Podemos tener elif para evaluar más condiciones, y su evaluación es en cascada.
# si encuentra una que cumple no evalúa las demás.
variable = 20

# para indicar los bloques con identación.
if variable == 10:
    print("Es 10")
elif variable == 20:
    print("variable es 20")
elif variable == 30:
    print("variable es 30")

#En Python, la estructura if - elif - else se utiliza para tomar decisiones basadas en condiciones. 
#La ejecución del código en cada bloque está determinada por la condición asociada a ese bloque. 
#Si se encuentra una condición que es verdadera, se ejecuta el bloque de código correspondiente y se omite el resto de las condiciones.


# pueden existir un else al final de todo
variable = 10

# para indicar los bloques con identación

if variable == 10:
    print("Es 10")
else:
    print("No es 10")

variable = 20

#En este caso, si variable es igual a 10, se ejecutará el bloque de código dentro del primer if. 
#Si no es igual a 10, se ejecutará el bloque dentro del else. En este ejemplo, dado que variable es 10, se imprimirá "Es 10".

# para indicar los bloques con identación
if variable == 10:
    print("Es 10")
elif variable == 20:
    print("Variable es 20")
elif variable == 30:
    print("Variable es 30")
else:
    print("No es ninguna de las anteriores")

# Python soporta el estilo de comparación matemático para la pertenencia de rangos
variable = 2

if 1 <= variable <= 10:
    print("Está entre 1 y 10")

# Esto sería equivalente a una condición compuesta
variable = 2
if 1 <= variable <= 10:
    print("Está entre 1 y 10")

#En este ejemplo, la primera serie de if-elif-else verifica en orden si variable es igual a 10, 20 o 30, y si ninguna de estas condiciones es verdadera, ejecutará el bloque de código en el else.

#Luego, se presenta el uso del estilo de comparación matemático para verificar si variable está entre 1 y 10, utilizando la expresión 1 <= variable <= 10. 
#Esta es una forma más concisa y legible de expresar la condición.

# Operadores de comparación
print(1 == 1)  # igualdad
print(1 != 11)  # distinto
print(1 > 11)  # mayor
print(1 >= 11)  # mayor o igual
print(1 < 11)  # menor
print(1 <= 11)  # menor o igual

#Estos operadores de comparación te permiten evaluar condiciones y generar resultados booleanos (True o False).

# La evaluación de los if en Python está cortocircuitada
a = 10
b = 0
# si puede inferir el resultado final no sigue evaluando
print(a != 10 and a/b)

#En este caso, la expresión a != 10 evalúa como False ya que a es igual a 10. 
#En una expresión and, si el primer operando es False, la expresión completa se evalúa como False sin evaluar el segundo operando. 
#Por lo tanto, a/b no se evaluará en este caso, evitando posibles errores de división por cero


# If ternario más o menos, se usa para inicialización de variables
# valor = VALOR_EN_CASO_TRUE if CONDICION else VALOR_EN_CASO_FALSO
variable = 10
valor = "Si es 10" if variable == 10 else "No es 10"
print(valor)

#En este ejemplo, valor tomará el valor "Si es 10" si la condición variable == 10 es verdadera, y tomará el valor "No es 10" en caso contrario.

# Se pueden concatenar todos los que quieras, pero no es recomendable
variable = 10
valor = "Si es mayor que 10" if variable > 10 else "Es menor de 10" if variable != 10 else "Es 10"
print(valor)

# Equivalente con if "normal"
variable = 10
if variable != 10:
    if variable > 10: 
        valor = "Si es mayor que 10"
    else:
        valor = "Es menor de 10"
else:
    valor = "Es 10"

print(valor)

#En este ejemplo, el operador ternario se ha encadenado para evaluar múltiples condiciones. Sin embargo, el código puede volverse difícil de leer y entender a medida que se encadenan más condiciones. 
#Es preferible utilizar estructuras de control más claras y expresivas cuando la lógica se complica.

# Ejemplo con estructuras de control más claras
variable = 10

if variable == 10:
    valor = "Es 10"
elif variable > 10:
    valor = "Es mayor que 10"
else:
    valor = "Es menor de 10"

print(valor)

# Bucles
# While se ejecuta mientras se cumple la condición, IMPORTANTE que la condición deje de cumplirse en algún momento

variable = 10
# No se ejecuta porque ya no se cumple la primera vez
while variable < 10:
    print(variable)

variable = 1
# Esto es infinito porque la condición nunca deja de cumplirse
while variable < 10:
    print(variable)

# La forma correcta
variable = 1

while variable < 10:
    print(variable)
    variable = variable + 1

# Los while en Python pueden llevar un else
# este bloque else se ejecuta cuando la condición es alcanzada
variable = 1

while variable < 10:
    print(variable)
    variable = variable + 1
else:
    print("Ha terminado con éxito")

# Ojo la diferencia se vera cuando usemos break
variable = 1

while variable < 10:
    print(variable)
    variable = variable + 1
print("Ha terminado con éxito")

# Otro bucle es el for que se usa para iterar sobre elementos iterables (listas, strings, diccionarios, tuplas..)
# for TEMPORAL in ITERABLE:

lista = [1, 2, 3, 4]
for numero in lista:
    print(numero)

cadena = "hola mundo"
for letra in cadena:
    print(letra)

tuplas = (1, 2, 3, 4)
for numero in tuplas:
    print(numero)

diccionarios = {"nombre": "James", "apellido": "Bond"}
for clave in diccionarios:
    print(clave)
    print(diccionarios[clave])

diccionarios = {"nombre": "James", "apellido": "Bond"}
for valores in diccionarios.values():
    print(valores)

diccionarios = {"nombre": "James", "apellido": "Bond"}
for clave, valor in diccionarios.items():
    print("La clave es", clave, "El valor es", valor)

# Tenemos la función range(INICIO, FIN, STEP) para generar rangos de números enteros
# que podemos usar con el for
# INICIO => valor de inicio, por defecto 0
# FIN => valor de fin, obligatorio, igual que en el slice no se incluye
# STEP => el número de saltos entre números consecutivos, por defecto es 1

for numero in range(10):
    print(numero)

for numero in range(5, 10):
    print(numero)

for numero in range(1, 10, 2):
    print(numero)

# El for también admite un else que se ejecutará al finalizar la iteración

for numero in range(10):
    print(numero)
else:
    print("He acabado")

# Tenemos 3 palabras reservadas
# pass => que es la instrucción vacía, no hace nada
if True:
    pass
print("hola")

# break, que solo funciona dentro de un bucle while o for, y le fuerza la salida incondicional
for numero in range(10):
    print(numero)
    break
else:
    print("si el bucle sale con un break este else no se ejecuta")

# Normalmente este break se pone dentro de un if
for numero in range(10):
    print(numero)
    if numero > 4:
        break

# continue, devuelve el control del flujo del bucle while a la condición
variable = 10
while variable > 0:
    print(variable)
    continue
    variable = variable - 1

# Igual que el break se puede poner dentro de un if
variable = 10
while variable > 0:
    variable = variable - 1
    if variable < 5:
        continue
    print(variable)


# Introducción de valores por teclado
# Python tiene una función input
# variable = input(PROMPT)
nombre = input("Introduce tu nombre ")
print(nombre)

# Siempre devuelve un string
numero = input("Introduce tu número ")
print(numero)
print(type(numero))

# Para leer números debemos convertirlos, para ello podemos usar las funciones float(), int(), bool()
numero = int(input("Introduce tu número "))
print(numero)
print(type(numero))

# O bien
entrada = input("Introduce tu número ")
if entrada.isnumeric():
    numero = int(entrada)
    print(numero)
    print(type(numero))
else:
    print("Has metido mal el número")

# Podemos insistir
entrada = input("Introduce tu número ")
while not entrada.isnumeric():
    entrada = input("Error, introduce tu número ")
numero = int(entrada)
print(numero)
print(type(numero))
