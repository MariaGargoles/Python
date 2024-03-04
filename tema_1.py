
#Fuertemente tipado:
#Python es un lenguaje fuertemente tipado, lo que significa que las variables deben ser declaradas con un tipo de dato específico y no pueden cambiar de tipo durante la ejecución del programa.
#Enteros: se pueden representar números enteros en Python. Por ejemplo, asignar el valor 10 a la variable "numero" y mostrar su tipo:

numero = 10
print(type(numero))

#Rango de enteros:
#Python no tiene un límite definido para el rango de los enteros. Se puede asignar un número grande a una variable, siempre que la arquitectura lo permita:

numero = 2891738921713892739871239873218973219873219873218973128973219873218937219872138913279813279821378932179321798321798321793218712798132789321791327971328
print(numero)
print(type(numero))

#Curiosidad 2
#Se pueden utilizar guiones bajos para mejorar la legibilidad de los números:

numero = 1_212_122
print(numero)
print(type(numero))

#Bases numéricas:
#Python permite trabajar con distintas bases numéricas. 
#Por defecto, se trabaja en decimal (base 10), pero también se pueden usar binario (base 2), octal (base 8), y hexadecimal (base 16):

# Decimal (base 10)
numero_decimal = 101
print(numero_decimal)

# Binario (base 2)
numero_binario = 0b101
print(numero_binario)

# Octal (base 8)
numero_octal = 0o101
print(numero_octal)

# Hexadecimal (base 16)
numero_hexadecimal = 0x101
print(numero_hexadecimal)

#Conversion entre bases
#Binario a decimal
# 0b101 => 1 + 0 + 1 sumamos cifra a cifra
# 0b101 => 1*2 + 0*2 + 1*2 multiplicamos por la base, en binario la base 2
# 0b101 => 1*2**2 + 0*2**1 + 1*2**0 a las bases empezando de derecha a izquierda la elevamos a la posicion que ocupa comenzao en 0
# 0b101 => 1 * 4 + 0 * 2 + 1 * 1 = 4 + 0 + 1 = 5

#Octal a decimal
#es igual que en binario solo que cambiamos la base 2 or una base 8
#0o101 = 1 + 0 + 1 #separamos
#0o101 = 1*8 + 0*8 + 1*8 multiplicar por la base
#0o101 = 1*8**2 + 0*8**1 + 1*8**0
#0o101 = 1* 64 + 0*8 + 1*1 = 64 + 0 + 1 = 65

#Conversion
#0x101 = 1*16**2 + 0 *16**1 + 1 * 16**0
#0x101 = 1*256 + 0 *16 + 1 * 1 = 256 + 0 + 1 = 257 

# Binario a Decimal
binario = 0b101
decimal = int(binario, 2)
print(decimal)

# Octal a Decimal
octal = 0o101
decimal = int(octal, 8)
print(decimal)

# Hexadecimal a Decimal
hexadecimal = 0x101
decimal = int(hexadecimal, 16)
print(decimal)


#Flotantes y Características:
#Los flotantes en Python son números con decimales. A continuación, se describen algunas características y operaciones relacionadas con los flotantes:

# Flotantes
flotante = 1.5
print(type(flotante))
print(flotante)

# Características
# Rango, tiene un límite de 17 posiciones, y redondea sin avisar.
flotante_grande = 1.12398739217321897934287938217389217321832179832798231798213793821793821798213798321721379832179832179321798321798327198372178321
print(type(flotante_grande))
print(flotante_grande)

# Notación científica
flotante_notacion_positiva = 1.2e2  # 10**2 = 100
print(type(flotante_notacion_positiva))
print(flotante_notacion_positiva)

flotante_notacion_negativa = 1.2e-2  # divide por 10**2, es decir, divide entre 100
print(type(flotante_notacion_negativa))
print(flotante_notacion_negativa)

# Operaciones
print(1.2 + 1.1)  # 2.3
print(1.1 + 2.2)  # 3.000000000003 (ojo: redondeo)
print(0.1 + 0.1 + 0.1 - 0.3)  # NO DA CERO, es muy cercano pero no es 0

# Números complejos
# Tienen una parte real y una parte imaginaria (la raíz cuadrada de menos uno)
complejo = 4 + 5j
print(type(complejo))
print(complejo)

# Booleanos
# Pueden ser verdadero (True) o falso (False).
# Python es case sensitive, es decir, diferencia mayúsculas de minúsculas.
verdadero = True
print(type(verdadero))
print(verdadero)

falso = False
print(type(falso))
print(falso)

#Caracteristicas
#Rango, si tiene limite 17 posiciones, y redondea, sin AVISAR.
flotante = 1.12398739217321897934287938217389217321832179832798231798213793821793821798213798321721379832179832179321798321798327198372178321
print(type(flotante))
print(flotante)

#Tambien la notacion cientifica
flotante = 1.2e2 # 10**2 = 100
print(type(flotante))
print(flotante)

flotante = 1.2e-2 #divide por 10**2 es decir divide entre 100
print(type(flotante))
print(flotante)

#operacion
print(1.2 + 1.1) #2.3
print(1.1 + 2.2) #3.000000000003 OJO es el redondeo
print(0.1 + 0.1 + 0.1 - 0.3) #NO DA CERO es muy cercano pero no es 0

#Numeros complejos
#Tienen una parte real y una parte imaginaria (es la raiz de caudrada de menos uno)
complejo = 4 + 5j
print(type(complejo))
print(complejo)

#tenemos booleanos que pueden ser veradero o falso (true o false).
#Python es case sensitive es decir diferencia mayusculas de minusculas
# NO es lo mismo true que True.
verdadero = True
print(type(verdadero))
print(verdadero)

falso = False
print(type(falso))
print(falso)

#Variables y Tipos:
#En Python, existen dos tipos principales de variables o tipos de datos: inmutables y mutables. A continuación, se describen estos conceptos:
# Inmutables: enteros, flotantes, complejos, booleanos, string y las tuplas
# Mutables: listas, conjuntos y diccionarios
# Ejemplo de inmutabilidad con enteros

numero = 10
print(numero)
numero = 100
print(numero)

# Identificador único
# Todos los objetos en Python tienen un identificador único que no cambia durante la ejecución

print(id(numero))

#Al ser inmutable "destruye" el anterior objeto y crea uno nuevo
#Esto solo funciona en los inmutables

numero = 10
print(id(numero))
numero = 100
print(id(numero))

# Tuplas (inmutables)
# Una vez creadas, no se pueden modificar, pero se pueden concatenar para crear nuevas
tupla = (1, 2, 3)
print(tupla)

# Intentar modificar la tupla generaría un error
# tupla[0] = 0  # Esto generaría un error
# Pero podemos crear una nueva tupla basada en la original

nueva_tupla = tupla + (4, 5, 6)
print(nueva_tupla)

# Listas (mutables)
# Pueden ser modificadas después de su creación

lista = [1, 2, 3]
print(lista)

# Modificar la lista

lista[0] = 0
print(lista)

# Diccionarios (mutables)
# Colección de pares clave-valor

diccionario = {"clave1": "valor1", "clave2": "valor2"}
print(diccionario)

# Añadir un nuevo par clave-valor

diccionario["clave3"] = "valor3"
print(diccionario)

# Conjuntos (mutables)
# Colección no ordenada de elementos únicos

conjunto = {1, 2, 3}
print(conjunto)

# Añadir un elemento al conjunto

conjunto.add(4)
print(conjunto)

# Strings, o cadenas de caracteres
# Son INMUTABLES
# Pueden contener cualquier carácter alfanumérico

cadena = "Hola mundo"
print(type(cadena))
print(cadena)

cadena_1 = 'Hola Mundo'
print(type(cadena_1))
print(cadena_1)

cadena_2 = """Hola Mundo"""
print(type(cadena_2))
print(cadena_2)

cadena_3 = '''Hola Mundo'''
print(type(cadena_3))
print(cadena_3)

# Identificadores únicos
print(id(cadena))
print(id(cadena_1))
print(id(cadena_2))
print(id(cadena_3))


#Todas las formas de declarar cadenas son válidas en Python, y puedes elegir la que mejor se adapte a tus necesidades. 
#Las comillas simples ('), comillas dobles ("), triples comillas simples ('''), y triples comillas dobles (""") se utilizan para definir cadenas de diferentes maneras, y pueden ser útiles en situaciones específicas, como incluir saltos de línea o comillas dentro de la cadena.

# Cadena multilinea con salto de línea
cadena = "En un lugar de la \nmancha de cuyo nombre"
print(cadena)

# Cadena multilinea con triples comillas dobles
cadena = """En un lugar de la 
mancha de cuyo nombre"""
print(cadena)

# Cadena multilinea con salto de línea usando triples comillas simples
cadena = 'En un lugar de la \nmancha de cuyo nombre'
print(cadena)

# No es necesario escapar las comillas dentro de triples comillas
cadena = """En un lugar de la 
'mancha' de "cuyo" nombre"""
print(cadena)

# Escapando comillas simples en cadenas con comillas simples
cadena = "En un lugar de la 'mancha'\n de \"cuyo\" nombre"
print(cadena)

#Usar triples comillas (simples o dobles) es especialmente útil para cadenas multilínea
#IMPORTANTE
# NO ES UN COMENTARIO 
"""
ladsjldksajdsa
akldsjdsakj
ldsakjdas
"""

#Acceso a Posiciones en Cadenas en Python:
#En Python, puedes acceder a caracteres individuales en una cadena utilizando corchetes [ ]. Aquí hay un ejemplo:


cadena = "Hola Mundo"
print(cadena[0])  # Accede al primer carácter, 'H'
print(cadena[1])  # Accede al segundo carácter, 'o'

#Las posiciones en Python empiezan en 0, por lo que cadena[0] devuelve el primer carácter de la cadena y cadena[1] devuelve el segundo carácter. 
#Esto se aplica tanto para acceder a caracteres específicos como para realizar operaciones de segmentación (slicing) en cadenas.
#Admite posiciones negativas, que se cuentan desde el FINAL de la cadena, siendo -1 la ultima posicion

cadena = "Hola Mundo"
print(cadena[-1])  # Accede al último carácter, 'o'
print(cadena[-2])  # Accede al penúltimo carácter, 'd'


#Las posiciones deben existir
cadena = "Hola Mundo"
print(cadena[100])

#! Esto dara un error de IndexError

#Inmutabilidad de las Cadenas en Python:
#Las cadenas en Python son inmutables, lo que significa que no puedes modificar individualmente los caracteres de la cadena después de que se ha creado. 
#Intentar hacerlo resultará en un error. Aquí está tu código:

cadena = "Hola Mundo"
cadena[0] = "h"
print(cadena)

#Este código generará un error de tipo TypeError porque estás intentando asignar un nuevo valor a un carácter específico de la cadena, y las cadenas en Python no admiten esta operación. 
#Si necesitas modificar una cadena, debes crear una nueva. Por ejemplo, podrías hacer algo como:

cadena = "Hola Mundo"
cadena = "h" + cadena[1:]
print(cadena)

#Cambio de Toda la Cadena en Python:
#En Python, puedes asignar un nuevo valor completo a una variable, incluida una cadena. 
#Sin embargo, ten en cuenta que al hacer esto, estás creando una nueva cadena y haciendo que la variable apunte a ella, en lugar de modificar la cadena existente.

cadena = "Hola Mundo"
cadena = "h"
print(cadena)

#Función len() en Python:
#La función len() en Python se utiliza para obtener la longitud (número de caracteres) de una cadena o la cantidad de elementos en una colección (como listas, tuplas, etc.). 

cadena = "Hola Mundo"
print(len(cadena))

#Este código imprimirá 11, ya que la cadena "Hola Mundo" tiene 11 caracteres, incluyendo espacios y letras.

#Slicing en Python:
#El slicing en Python se refiere a la técnica de extraer una parte (subcadena) de una secuencia, como una cadena, lista o tupla. 
#Se utiliza la notación inicio:fin:paso para especificar los índices.

cadena = "Hola Mundo"
print(cadena[0:4:1])   # Obtiene los caracteres desde el índice 0 hasta el 3 (4 no incluido) con paso 1
print(cadena[0:10:1])  # Obtiene toda la cadena ya que el paso es 1
print(cadena[5:10:1])  # Obtiene los caracteres desde el índice 5 hasta el 9 con paso 1
print(cadena[0:10:2])  # Obtiene cada segundo carácter desde el índice 0 hasta el 9
print(cadena[0:10:5])  # Obtiene cada quinto carácter desde el índice 0 hasta el 9

#Ten en cuenta que el índice fin especifica hasta dónde se quiere llegar, pero el carácter en ese índice no está incluido en el resultado. 
#Además, si no se especifica inicio o fin, se toma el valor predeterminado según se menciona en el comentario.


#Importancia de los límites en el slicing:
#Es esencial tener en cuenta que al realizar slicing en Python, el lenguaje maneja automáticamente los límites para evitar errores relacionados con índices fuera de rango. 

cadena = "Hola Mundo"
print(cadena[0:40000:1])          # Toma hasta la longitud de la cadena si el índice de fin es mayor
print(cadena[100:10:1])            # Resultado vacío porque el índice de inicio es mayor que el de fin
print(cadena[0:10:11010100101010]) # Solo toma el primer carácter (índice 0)

#En el primer caso, cuando el índice de fin es mayor que la longitud de la cadena, Python simplemente toma la cadena hasta su longitud, evitando un error de índice fuera de rango.
#En el segundo caso, el índice de inicio (100) es mayor que el de fin (10), lo que resulta en una cadena vacía.
#Admite indices negativos

cadena = "Hola Mundo"
print(cadena[-1:5:1]) #cadena vacia
print(cadena[5:-1:1]) #Mund
print(cadena[-1:-10:-1]) #odnuM lo invierten
print(cadena[::]) #COPIA de la cadena

#Métodos de comprobación en cadenas:
#Los métodos de comprobación en cadenas son útiles para verificar ciertas propiedades de la cadena. Aquí tienes algunos ejemplos:

cadena = "hola"
print(cadena.isupper())   # Comprueba si todos los caracteres están en mayúsculas (False en este caso)
print(cadena.islower())   # Comprueba si todos los caracteres están en minúsculas (True en este caso)
print(cadena.isnumeric())  # Comprueba si todos los caracteres son numéricos (False en este caso)

#isupper(): Devuelve True si todos los caracteres de la cadena están en mayúsculas, de lo contrario, devuelve False.

#islower(): Devuelve True si todos los caracteres de la cadena están en minúsculas, de lo contrario, devuelve False.

#isnumeric(): Devuelve True si todos los caracteres de la cadena son numéricos, de lo contrario, devuelve False.


#Métodos de formato y eliminación de espacios:

cadena = "@@@@@@@@@@@hola@@@@@@@@@@@@"

# Eliminar espacios en blanco a la derecha y a la izquierda
print(cadena.strip())

# Eliminar caracteres específicos a la derecha y a la izquierda
print(cadena.strip("@"))

# Eliminar espacios en blanco a la derecha
print(cadena.rstrip("@"))

# Eliminar espacios en blanco a la izquierda
print(cadena.lstrip("@"))

#strip(): Elimina los espacios en blanco a la derecha y a la izquierda de la cadena.
#strip(characters): Elimina los caracteres especificados (en este caso, "@") a la derecha y a la izquierda de la cadena.
#rstrip(characters): Elimina los caracteres especificados (en este caso, "@") solo a la derecha de la cadena.
#lstrip(characters): Elimina los caracteres especificados (en este caso, "@") solo a la izquierda de la cadena.

#Recuerda que estos métodos no modifican la cadena original; en cambio, devuelven una nueva cadena con las modificaciones aplicadas.

#Métodos de búsqueda find() e index():

cadena = "hola que tal hola bien que"

# Encontrar la posición de la primera ocurrencia de "que" usando find()
print(cadena.find("que"))

# Encontrar la posición de la primera ocurrencia de "que" usando index()
print(cadena.index("que"))

#find(substring): Devuelve la posición de la primera ocurrencia del subtring en la cadena. Si no se encuentra, devuelve -1.
#index(substring): Similar a find(), pero si el substring no se encuentra, en lugar de devolver -1, arroja un error (ValueError).

#Ambos métodos devuelven la posición de la primera ocurrencia del substring en la cadena


#Búsqueda con inicio y fin especificados:

cadena = "hola que tal hola bien que"

# Especificar posición de inicio para la búsqueda con find()
print(cadena.find("que", 6))

# Especificar posición de inicio para la búsqueda con index()
print(cadena.index("que", 6))

#Al agregar dos argumentos adicionales a find() e index(), especificamos la posición de inicio y de fin para la búsqueda en la cadena. 
#Esto permite buscar la ocurrencia de "que" dentro de un rango específico de la cadena.

#Búsqueda con inicio y fin especificados (con posición de fin):

cadena = "hola que tal hola bien que"

# Especificar posición de inicio y fin para la búsqueda con find()
print(cadena.find("que", 6, 100))

# Especificar posición de inicio y fin para la búsqueda con index()
print(cadena.index("que", 6, 100))

#Diferencia entre find() e index() cuando no encuentran la subcadena:

cadena = "hola que tal hola bien que"

# find() devuelve -1 si no encuentra la subcadena
print(cadena.find("adios"))

# index() devuelve un error (ValueError) si no encuentra la subcadena
# print(cadena.index("adios"))

#La diferencia clave es que find() devuelve -1 si la subcadena no se encuentra, mientras que index() genera un error (ValueError) en esa situación.
#En términos de manejo de errores, find() es más tolerante, ya que permite que el programa continúe ejecutándose incluso si la subcadena no está presente.

#Operadores en Python: Aritméticos y de Cadena
# Aritméticos

print(2 + 1)  # Suma
print(2 - 1)  # Resta
print(2 * 1)  # Multiplicación
print(2 / 1)  # División
print(2 // 1) # Cociente de la división entera
print(2 % 1)  # Resto de la división entera

# Operadores sobrecargados (concatenación y repetición)
print("hola " + "que")  # Concatenación de cadenas
print("hola" * 10)      # Repetición de la cadena 10 veces

#Estos son ejemplos de operadores aritméticos y cómo se sobrecargan para operar en cadenas, como en el caso de la concatenación (+) y la repetición (*).

#Operadores Lógicos en Python
# Operadores lógicos (and, or, not)

# AND
print(False and False)
print(False and True)
print(True and False)
print(True and True)

# OR
print(False or False)
print(False or True)
print(True or False)
print(True or True)

# NOT
print(not False)
print(not True)

#Estos son ejemplos de operadores lógicos en Python, que aplican la lógica booleana (True y False). 
#and devuelve True solo si ambos operandos son True. or devuelve True si al menos uno de los operandos es True. not invierte el valor booleano.


#Operadores Binarios en Python

# Operadores binarios (&, |, ~, ^)
# AND (&)
print(0 & 0)
print(0 & 1)
print(1 & 0)
print(1 & 1)

# OR (|)
print(0 | 0)
print(0 | 1)
print(1 | 0)
print(1 | 1)

# NOT (~)
print(~1)
print(~0)

# XOR (^)
print(0 ^ 0)
print(0 ^ 1)
print(1 ^ 0)
print(1 ^ 1)

# Operaciones a nivel de bits
print(5 & 4)
# 5 => 101
# 4 => 100
# & => 100 => 4

#Estos son ejemplos de operadores binarios en Python. & realiza la operación AND a nivel de bits, | realiza la operación OR a nivel de bits, ~ realiza la operación NOT a nivel de bits, 
#y ^ realiza la operación XOR a nivel de bits.


print(5 | 4)

#5 => 101
#4 => 100
#| => 101

print(~1)  # Resultado: -2

# Representación de Números Negativos
# Signo Magnitud
# 1 => -
# 0 => +
# 5  => 0 0101
# -5 => 1 0101

# Complemento a Uno
# 5 => 0 0101
# -5 => 1 1010

# Complemento a Dos
# 5 => 0 0101
# C2 => 1 1010 + 1 = 1 1011

# Operador XOR (^)
print(0 ^ 0)  # Resultado: 0
print(0 ^ 1)  # Resultado: 1
print(1 ^ 0)  # Resultado: 1
print(1 ^ 1)  # Resultado: 0

# Cifrado y Descifrado
mensaje = 5
clave = 4
cifrado = mensaje ^ clave
descifrado = cifrado ^ clave
print(cifrado)     # Resultado: 1
print(descifrado)  # Resultado: 5


# Desplazamientos a la derecha (>>) y a la izquierda (<<)
print(2 >> 1)  # Resultado: 1
# 2 => 10, desplazado a la derecha 1 vez => 01 (equivalente a una división por 2)

print(2 << 1)  # Resultado: 4
# 2 => 10, desplazado a la izquierda 1 vez => 100 (equivalente a una multiplicación por 2)

# Listas
# Conjunto ORDENADO de elementos que pueden ser de cualquier tipo
# Pueden ser heterogéneas, es decir, pueden mezclar diferentes tipos de datos
# Son MUTABLES, lo que significa que cuando las modificas, NO cambia el ID
# Para crear una lista vacía hay 2 formas:
# Con la función list()
lista = list()
print(type(lista))
print(lista)


# Usando []
lista = []
print(type(lista))
print(lista)

# Para crearla con elementos, basta con ponerlos separados por comas
lista = [1, 2, 3, 4, 5]
print(type(lista))
print(lista)

# Heterogéneas
lista = [1, 2, 3, 4, 5, "hola", [1, 2], 3.4]
print(type(lista))
print(lista)

# Mutables
# Podemos hacer lo que en informática se conoce como CRUD (Crear, Leer, Actualizar y Borrar)
# Para acceder a los elementos, igual que en los strings, y también se le aplican igual los slices
lista = [1, 2, 3, 4, 5]
print(lista[2])
print(lista[0:2:1])

# Para añadir, tenemos 2 métodos
# El primero es append(ELEM), que añade el elemento al final
lista = [1, 2, 3, 4, 5]
lista.append("hola")
print(lista)

# El método insert(POS, ELEM), esto inserta en la posición que le pasamos como primer argumento
lista = [1, 2, 3, 4, 5]
lista.insert(1, "hola")
print(lista)

# Para modificar se hace a través de la posición
lista = [1, 2, 3, 4, 5]
lista[2] = "hola"
print(lista)

# Podemos borrar, para ello tenemos 2 formas
# La primera es el operador del y la posición
lista = [1, 2, 3, 4, 5]
del lista[2]
print(lista)

# Es el método remove(ELEM), que elimina la primera ocurrencia que encuentra del elemento
lista = [1, 2, 3, 4, 5]
lista.remove(3)
print(lista)

# Tenemos 2 operadores muy útiles
# El operador in nos devuelve True o False si un determinado elemento está o no en un elemento iterable (lista, string, tupla, etc.)
lista = [1, 2, 3, 4, 5]
print(1 in lista)
print("hola" in lista)

# El operador is comprueba si dos objetos son el mismo (mira los ids)
numero = 10
numero_2 = 10
print(numero is numero_2)
lista = [1, 2, 3]
lista_2 = [1, 2, 3]
print(lista is lista_2)

# Tenemos funciones para listas numéricas
lista = [1, 2, 3, 4, 5]
print(max(lista))  # devuelve el valor más alto
print(min(lista))  # devuelve el valor más pequeño
print(sum(lista))  # nos devuelve la suma de todos los elementos

# También tienen métodos, estos métodos SÍ modifican la lista
lista = [1, 2, 3, 4, 5]
lista.reverse()  # esto invierte el orden
print(lista)

lista = [1, 3, 20, 4, 0, 5]
lista.sort()  # ordena la lista
print(lista)

# La función de orden
lista = ["d", "a", "c", "b"]
lista.sort()
print(lista)

# Algunas a medio camino con los strings
cadena = "hola que tal"
# el método split(CARACTER), que divide la cadena en una lista usando como referencia el caracter que se le pasa como argumento
lista = cadena.split(" ")
print(lista)

# Y tenemos la inversa que es el "PEGAMENTO".join(lista)
# unir una lista de strings en un único string
lista = ["hola", "que", "tal"]
print(",".join(lista))


# Tuplas
# Son como una lista pero inmutables, es decir tienen todas las características
# y métodos y funciones de una lista, menos la parte de que se pueden modificar
# para crear una tupla 2 formas
tupla = tuple()
print(type(tupla))
print(tupla)

# usando ()
tupla = ()
print(type(tupla))
print(tupla)

# Parametrizar valores igual que una lista
tupla = (1, 2, "hola")
print(type(tupla))
print(tupla)

# Todo igual salvo la modificación
tupla = (1, 2, "hola")
print(tupla[1])
print(tupla[0:2:1])
tupla[1] = "ERROR"  # Error

#Las tuplas en Python son similares a las listas, pero con la principal diferencia de que son inmutables. 
#Esto significa que no puedes modificar sus elementos una vez que se han asignado. 
#A pesar de su inmutabilidad, las tuplas son útiles cuando deseas crear colecciones de elementos que no deben cambiar durante la ejecución del programa.

# Diccionarios
# Es un conjunto de elementos, que no tienen orden, y que vienen definidos por
# un conjunto de pares clave:valor
# la clave puede ser cualquier objeto serializable (que se pueda convertir en string)
# y el valor cualquier tipo de dato de Python
# Son MUTABLES, al igual que las listas podremos hacer operaciones CRUD
# para definir un diccionario 2 formas
# función dict
diccionario = dict()
print(type(diccionario))
print(diccionario)

# O la segunda con llaves
diccionario = {}
print(type(diccionario))
print(diccionario)

# Podemos crearlo con elementos siguiendo el concepto de clave:valor
diccionario = {"nombre": "Jane", "telefono": 782732823}
print(type(diccionario))
print(diccionario)

# Para acceder a los elementos hay 2 formas
# la primera a través de la clave
diccionario = {"nombre": "Jane", "telefono": 782732823}
print(diccionario["nombre"])

# La segunda forma es el método get("CLAVE")
diccionario = {"nombre": "Jane", "telefono": 782732823}
print(diccionario.get("nombre"))

# La diferencia es si no existe la clave
diccionario = {"nombre": "Jane", "telefono": 782732823}
print(diccionario["apellido"])  # esto da error si no existe
print(diccionario.get("apellido"))  # devuelve un None

# Además, el get nos permite poner un segundo parámetro para definir ese valor por defecto
# si no queremos que sea None
print(diccionario.get("apellido", "VALOR POR DEFECTO"))

# Podemos añadir nuevos elementos y editar elementos existentes
diccionario = {"nombre": "Jane", "telefono": 782732823}

# Editar con la clave
diccionario["nombre"] = "Paco"
print(diccionario)

# Para añadir es poner una clave que no existe
diccionario["apellido"] = "Rambo"
print(diccionario)

# Podemos borrar una clave, tenemos 2 formas
# con del y la clave
diccionario = {"nombre": "Jane", "telefono": 782732823}
del diccionario["nombre"]
print(diccionario)

# Es el método pop(CLAVE), este método devuelve el valor
diccionario = {"nombre": "Jane", "telefono": 782732823}
diccionario.pop("nombre")
print(diccionario)

# podemos recuperarlo
diccionario = {"nombre": "Jane", "telefono": 782732823}
valor = diccionario.pop("nombre")
print(diccionario)
print(valor)

#Los diccionarios en Python son estructuras de datos que permiten almacenar pares clave-valor. 
#Son mutables, lo que significa que puedes añadir, editar y eliminar elementos.


# Tenemos que los métodos len(), operador in y el is
diccionario = {"nombre": "Jane", "telefono": 782732823}
print(len(diccionario))
print("nombre" in diccionario)  # Aquí comprueba con las claves

# también tiene 3 métodos más para manipular las claves y los valores
diccionario = {"nombre": "Jane", "telefono": 782732823}
print(list(diccionario.keys()))
print(list(diccionario.values()))
print(list(diccionario.items()))

# Conjuntos
# Es una colección de elementos, SIN duplicados, SIN orden y puede ser de cualquier tipo
# soporta el álgebra de conjuntos (unión, intersección, ...)
# dos formas o con set()
conjunto = set()
print(type(conjunto))
print(conjunto)
# no vacío con {}
conjunto = {1, 2, 3, 4}
print(type(conjunto))
print(conjunto)

# No duplicados
conjunto = {1, 2, 3, 4, 1, 1, 1, 1, 1}
print(type(conjunto))
print(conjunto)

# Álgebra de conjuntos
automoviles = {"BMW", "SEAT", "FERRARI"}
motocicletas = {"BMW", "DUCATTI", "KAWA"}

print(automoviles & motocicletas)  # intersección, los fabricantes de motos y coches
print(automoviles - motocicletas)  # diferencia fabricantes de coches que no hacen motos

#Los conjuntos en Python son colecciones de elementos únicos sin orden. 
#Puedes realizar operaciones de álgebra de conjuntos como unión, intersección y diferencia. También son útiles para eliminar duplicados de una lista.




