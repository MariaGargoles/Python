#Funciones
#se crean usando la palabra sereveada def
# def NOMBRE_FUNCION(PARAM_1, PARAM_2, ..)
#La funcion mas sencilla, que no hace nada
def foo():
    pass

print(type(foo))

#Las funciones pueden llevar una cadena de documentacion, que NO es un comentario
#en esta cadena de documentacion se suele ncluir una descripcion de la funcion
# y un resumen de los parametros de entrada y salida
#la diferencia con los comenarios es que se pueden consultar
#invocando al metodo magico __doc__ que nos dara acceso a la documentaicon de la funcion
def foo():
    """
        Ejemplo de cadena de documentacion de la funcion que no hace nada
        Parametros de entrada:
            ninguno
        Salida:
            ninguna
    """
    pass

print(foo.__doc__)

#Las propias de python todas tienen documentacion
print(print.__doc__)
print(max.__doc__)

#Las fuciones pueden tener un cuerpo que son las operaciones que se realizan dentro de la funcion
def suma():
    a = 10
    b = 5
    print(a + b)

#Las funciones se deben invocar, es el momento de la invocacion cuando se ejecuta el codigo asociado
suma()

#Las funciones devuelve SIEMPRE, la diferencia es que con la sentencia return definimos que queremos devolver
#si no la indicamos por defecto devuelve un None

def foo():
    a = 10

retorno = foo()
print(retorno)

#Si le ponemos el return definimos que queremos devolver
def foo():
    a = 10
    return a

retorno = foo()
print(retorno)

#En python las funciones pueden devolver multiples valores, simplemente debemos separarlos por comas en
#el return

def foo():
    a = 10
    b = 20
    return a,b
    
retorno = foo()
print(retorno)
print(type(retorno)) 

#en el fondo foo devuelve un valor, lo que hace es juntarlos todos en una tupla
#podemos realizar asignaciones con el packing y unpaking
def foo():
    a = 10
    b = 20
    return a,b
    
retorno_1, retorno_2 = foo()
print(retorno_1, retorno_2)

#Las funciones pueden recibir argumentos, que pueden ser de cualquier tipo
def foo(x,y):
    print(x,y)

#en el momento de la invocacion debemos asignar valores
foo(19,90)

#Por defecto los parametros de las funciones en python, son POSICIONALES y OBLIGATORIOS
def foo(x,y):
    print(x,y)

foo()
foo(90)

#Podemos trabajar con parametros optativos
#en la firma de la funcion le debemos indicar los valores por efecto de los parametros
#solo se aplican si no viene un valor como argumento
#ejemplo de parametro y como optativo
def foo(x,y=10):
    print(x,y)

foo(1)
foo(1,2)

#Importante los parametros optativos siempre deben ir al final de la firma
def foo(x=10,y):
    print(x,y)

#Podemos tener tantos argumentos optativos como queramos
def foo(x=20,y=10):
    print(x,y)

foo()
foo(1)
foo(1,2)

#Los parametros tambien se le puede modificar el tema posicionalidad
#en esta caso diriamos que trabajamos con parametros Nominales
#se definen en el moento de la invocaicon, y deben coincidir con el identificador
#deinido en l firma de la funcion

def foo(x,y):
    print(x,y)

#Nominales
    
foo(y = 10, x = 20)

#Debemos respetar la misma regla que con los optativos, los nominales al final de la invocacion

def foo(x,y):
    print(x,y)

#Nominales

foo(y = 10, x)

#Se pueden combinar ambas ideas
def foo(x,y=100,z=20):
    print(x,y,z)

foo(1)
foo(z=10,x=10)
foo(z=10,x=10,y=100)
foo(1,2,4)

#Ademas de esto, en python las funciones pueden recibir un numero arbitrario de parametros
#como por ejemplo la funcion print
#en este caso en la firma de la funcion debemos indicarlo con el operador *
def foo(*parametros):
    print(parametros)
    print(type(parametros))

foo()
foo(1)
foo(1,2)
foo(1,2,3)
foo(1,2,3,4)

#Tambien podemos tener un numero arbitrario de parametros nominales, para ello en la firma
#usarmeos un **
def foo(**parametros):
    print(parametros)
    print(type(parametros))

foo(x=10)
foo(x=10,y=10)
foo(x=10,z=20,y=987)

#Podemos combinar todo lo anterior
def foo(x,y=100,z=20, *posicionales, **nominales):
    print(x,y,z)
    print(posicionales)
    print(nominales)

foo(1)
foo(1,2)
foo(1,2,3)
foo(1,2,3,2,3,4,5,6)
foo(1,2,3,4,g=10,h=19)

# Funciones recursivas
# Son funciones que se invocan a sí mismas
# Se asemejan un poco a un bucle
# En este caso, es casi un bucle infinito, pero Python tiene un límite de recursividad que ronda las 1000 llamadas
# Y en ese punto, se produce un error de límite máximo de recursividad alcanzado

def contar(numero):
    print(numero)
    contar(numero - 1)

contar(10)

# Debemos definir lo que se conoce como caso base, que es esencialmente la condición de parada
# de la recursividad. En otras palabras, es el momento en el cual dejamos de invocar la función recursiva.

def contar(numero):
    
    print(numero)

    if numero == 1:
        return 1
    else:
        contar(numero - 1)

contar(10)

#Factorial en recursivo
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return factorial(numero - 1) * numero


print(factorial(5))

# Apila las llamadas en la pila del programa y cuando llega al caso base, desapila.
# Para el cálculo del factorial:
# factorial(5) = factorial(4) * 5
# factorial(4) = factorial(3) * 4
# factorial(3) = factorial(2) * 3
# factorial(2) = factorial(1) * 2
# factorial(1) = 1
# factorial(2) = 1 * 2 = 2
# factorial(3) = 2 * 3 = 6
# factorial(4) = 6 * 4 = 24
# factorial(5) = 24 * 5 = 120

# Para la Serie de Fibonacci:
# Comienza en 1, 1 y el siguiente valor es la suma de los dos anteriores.
# 1, 1, 2, 3, 5, 8, 13, ...
# Posición 0 => 1
# Posición 1 => 1
# Posición 2 => 2
# Posición 3 => 3
# Posición 4 => 5
# Posición 5 => 8
# Posición 6 => 13

# Queremos calcular el valor de una posición específica en la serie de Fibonacci.
def fibonacci(posicion):
    if ((posicion == 0) or (posicion == 1)):
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

print(fibonacci(6)) #devolver 13

#Explicacion
#fibonacci(6) = fibonacci(5) + fibonacci(4)
#fibonacci(5) = fibonacci(4) + fibonacci(3)
#fibonacci(4) = fibonacci(3) + fibonacci(2)
#fibonacci(3) = fibonacci(2) + fibonacci(1)
#fibonacci(2) = fibonacci(1) + fibonacci(0)
#fibonacci(1) = 1
#fibonacci(0) = 1
#fibonacci(2) = 1 + 1 = 2
#fibonacci(3) = 2 + 1 = 3
#fibonacci(4) = 3 + 2 = 5
#fibonacci(5) = 5 + 3 = 8
#fibonacci(6) = 8 + 5 = 13

#Alcances de variables en las funciones
# tenemos 2 tipos de variables las globales y las locales
# ademas de las que pasamos por parametro
#Alcance variables de parametro
# por valor y por referencia, siendo el primero una copia mientrasque por referencia es la misma variable
def foo(x):
    print(x)
    #Por defecto es una copia y los cambios no le afectan
    x = 10
    print(x)

x = 100
foo(x)
#aqui sigue valiendo 100
print(x)


def cuadrados(lista):
    retorno = []
    for numero in lista:
        retorno.append(numero**2)
    lista = retorno
    print(lista)

lista = [1,2,3]
print(lista)
cuadrados(lista)
print(lista)

#Otro ejemplo 
#OJO con lo de paso por valor y referencia
#las variables INMUTABLES (enteros, flotantes, complejos, tuplas, string, boolean)las pasa como una copia
#Las variables MUTABLES (listas, diccionarios, conjuntos), pasa la propia variable
def suma(lista):
    for posicion in range(len(lista)):
        lista[posicion] = lista[posicion] + 100
    print(lista)

lista = [1,2,3]
print(lista)
suma(lista)
print(lista)

#OJo no tiene que ver con el identificador
def suma(paco):
    for posicion in range(len(paco)):
        paco[posicion] = paco[posicion] + 100
    print(paco)

lista = [1,2,3]
print(lista)
suma(lista)
print(lista)

#Globales vs locales
#Una variable global es comun a todo el codigo
#Una variable local solo tiene el alcance de su bloque

def foo():
    variable = 10

foo()
#Esta variable no existe, porque es local a la funcion
print(variable)

#globales, son de solo lectura
variable = 100

def foo():
    print(variable)

foo()
print(variable)

#OJO son globales de solo lectura por defecto
variable = 100

def foo():
    #en el momento que creo una variable aun que tenga el mismo nombre que la global
    #crea una nueva variable local a la funcion
    variable = 200
    print(variable)

foo()
print(variable)

#Otro mas CUIDADO
variable = 100

def foo():
    #en el momento que ponemos la igualdad crea la variable y pierde el acceso a la blobal
    variable = variable + 200
    print(variable)

foo()
print(variable)

#para poder modificar valores globales dentro de la funcion
#tenemos la palabra reservada global
#que debemos usar ANTES de hacer referencia a la funcion
variable = 100

def foo():
    global variable
    variable = variable + 200
    print(variable)

foo()
print(variable)

#OJO si la variable no existe la crea
def foo():
    global x
    x = 10000

foo()
print(x)

#Certificacion

def foo():
    global x
    x = 10

def foo_2(x):
    x = x

def foo_3():
    x = 3000

x = "hola"
foo()
foo_2(x)
foo_3()
print(x)


