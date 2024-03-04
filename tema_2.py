#Estructuras de Control:
#Las estructuras de control son herramientas que nos permiten manejar el flujo de ejecución de un programa. 
#En Python, contamos principalmente con las estructuras de control if-elif-else y los bucles while y for.

#1. if-elif-else:
#if: Permite ejecutar un bloque de código si una condición es verdadera.

variable = 10
if variable == 10:
    print("Es 10")

#elif: Se utiliza para evaluar condiciones adicionales si la primera condición no es verdadera. Solo se evalúa si la condición anterior fue falsa.


variable = 20
if variable == 10:
    print("Es 10")
elif variable == 20:
    print("Variable es 20")

#else: Se ejecuta si ninguna de las condiciones anteriores es verdadera.


    variable = 20
    if variable == 10:
        print("Es 10")
    elif variable == 20:
        print("Variable es 20")
    else:
        print("No es ninguna de las anteriores")

#2. Operadores de Comparación:
#Permiten evaluar condiciones y generar resultados booleanos (True o False).

    print(1 == 1)  # Igualdad
    print(1 != 11)  # Distinto
    print(1 > 11)  # Mayor
    print(1 >= 11)  # Mayor o igual
    print(1 < 11)  # Menor
    print(1 <= 11)  # Menor o igual

#3. Cortocircuito en la Evaluación de if:
#Si puede inferir el resultado final de la expresión, no evalúa las partes restantes.

    a = 10
    b = 0
    print(a != 10 and a/b)

#4. Operador Ternario:
#Forma concisa de escribir un bloque if-else, útil para inicializar variables.

variable = 10
valor = "Si es 10" if variable == 10 else "No es 10"
print(valor)

#Se pueden concatenar, pero es recomendable mantener la claridad.

variable = 10
valor = "Si es mayor que 10" if variable > 10 else "Es menor de 10" if variable != 10 else "Es 10"
print(valor)

#Equivalente con if "normal".

    variable = 10
    if variable != 10:
        if variable > 10:
            valor = "Si es mayor que 10"
        else:
            valor = "Es menor de 10"
    else:
        valor = "Es 10"

    print(valor)

#5. Bucles:
#5.1. while:
#Ejecuta un bloque de código mientras una condición sea verdadera. 
#Es importante que la condición deje de cumplirse en algún momento para evitar bucles infinitos.

variable = 1

while variable < 10:
    print(variable)
    variable = variable + 1

#Pueden llevar un bloque else que se ejecuta cuando la condición no es verdadera.


    variable = 1
    while variable < 10:
        print(variable)
        variable = variable + 1
    else:
        print("Ha terminado con éxito")

#5.2. for:
#Se utiliza para iterar sobre elementos iterables como listas, cadenas, diccionarios o tuplas.

lista = [1, 2, 3, 4]
for numero in lista:
    print(numero)

#También se puede usar la función range() para generar rangos de números.


for numero in range(10):
    print(numero)

#Admite un bloque else que se ejecuta al finalizar la iteración.

    for numero in range(10):
        print(numero)
    else:
        print("He acabado")

#6. Palabras Reservadas:
#pass: Instrucción vacía que no hace nada. Se utiliza cuando la sintaxis requiere alguna declaración, pero no se necesita código.

if True:
    pass
print("Hola")

#break: Funciona dentro de bucles while o for, y fuerza la salida incondicional del bucle.

for numero in range(10):
    print(numero)
    break
else:
    print("Si el bucle sale con un break, este else no se ejecuta")

#continue: Devuelve el control del flujo del bucle while a la condición.

variable = 10
while variable > 0:
    print(variable)
    continue
    variable = variable - 1

#global: Permite modificar variables globales dentro de funciones.


    variable = 100

    def foo():
        global variable
        variable = variable + 200
        print(variable)

    foo()
    print(variable)

#7. Introducción de Valores por Teclado:
#La función input() se utiliza para recibir datos desde el teclado, pero siempre devuelve un string.


nombre = input("Introduce tu nombre ")
print(nombre)

#Para leer números, es necesario convertirlos con las funciones float(), int(), bool().


numero = int(input("Introduce tu número "))
print(numero)
print(type(numero))

#Se puede validar la entrada utilizando un bucle while y condicionales.


entrada = input("Introduce tu número ")
while not entrada.isnumeric():
    entrada = input("Error, introduce tu número ")
numero = int(entrada)
print(numero)
print(type(numero))

