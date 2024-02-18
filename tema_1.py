#Fuertemente tipado
#El primer tipo son enteros
numero = 10
print(type(numero))
#Los enteros tienen varias caracteristicas
#El rango, no tiene un limite, aunque si que hay limite duro que en su arquitectura
numero = 2891738921713892739871239873218973219873219873218973128973219873218937219872138913279813279821378932179321798321798321793218712798132789321791327971328
print(numero)
print(type(numero))
#Curiosidad 2
numero = 1_212_122
print(numero)
print(type(numero))
#Soporta trabajar en varias bases
#por defecto trabajamos en decimal, que es base 10, es decir tenemos del 0 al 9
numero = 101
print(numero)
print(type(numero))

#Permite trabajar en binario, base 2, es decir tenemos 2 posibles valores 0 y 1
#para indicar que trabajar en binario le debemos poner 0b al principio
numero = 0b101
print(numero)
print(type(numero))
#Conversion entre bases
#binario a decimal
# 0b101 => 1 + 0 + 1 sumamos cifra a cifra
# 0b101 => 1*2 + 0*2 + 1*2 multiplicamos por la base, en binario la base 2
# 0b101 => 1*2**2 + 0*2**1 + 1*2**0 a las bases empezando de derecha a izquierda la elevamos a la posicion que ocupa comenzao en 0
# 0b101 => 1 * 4 + 0 * 2 + 1 * 1 = 4 + 0 + 1 = 5

#Tambien podemos trabajar en base octal, base 8, tenemos del 0 al 7
#se indica poniendo un 0o al inicio del numero
numero = 0o101
print(numero)
print(type(numero))
#Conversion entre bases
#de octal a decimal
#es igual que en binario solo que cambiamos la base 2 or una base 8
#0o101 = 1 + 0 + 1 #separamos
#0o101 = 1*8 + 0*8 + 1*8 multiplicar por la base
#0o101 = 1*8**2 + 0*8**1 + 1*8**0
#0o101 = 1* 64 + 0*8 + 1*1 = 64 + 0 + 1 = 65

#Tamien permite hexadecimal que es base 16, tenemos del 0 al 9 y de la A-F
#para indicar el hexadeximal ponemos 0x
numero = 0x101
print(numero)
print(type(numero))

#Conversion
#0x101 = 1*16**2 + 0 *16**1 + 1 * 16**0
#0x101 = 1*256 + 0 *16 + 1 * 1 = 256 + 0 + 1 = 257 

#Tenemos flotantes que son numeros con decimales
flotante = 1.5
print(type(flotante))
print(flotante)

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

#En python tenemos 2 tipos de variables o tipos
#los inmutables y los mutables
#los inmutables son aquellos que una vez creados NO se ueden modificar
#los mutables son aquellos que una vez creados SI se pueden modificar
#INMUTABLES: enteros, flotantes, complejos, booleanos, string y las tuplas
#MUTABLES: listas, conjuntos y diccionarios

#INMUTABILIDAD
numero = 10
print(numero)
numero = 100
print(numero)

#Tenemos que todos los objetos en python tienen un identificador unico
#ese identificador no se cambia en toda la ejecucion
#podemos ver ese identificador con la funcion id()
numero = 10
print(numero)
print(id(numero))

#Al ser inmutable "destruye" el anterior objeto y crea uno nuevo
#Esto solo funciona en los inmutables
numero = 10
print(id(numero))
numero = 100
print(id(numero))

#Strings, o cadenas de caracteres
# Son #INMUTABLES
# Pueden contener cualquier caracter alfanumerico
#Tenemos 4 formas distintas de declaralas
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
print(id(cadena))
print(id(cadena_1))
print(id(cadena_2))
print(id(cadena_3))

#La diferecia entre comillas dobles y simples sencillas es ninguna
#lo que si hay diferencia es respecto a las comillas triples
#las triples habilitan un tipo de sintaxis llamada Heredoc
#permite el multilinea
cadena = "En un lugar de la 
mancha de cuyo nombre"
print(cadena)

#Con las triples funciona
cadena = """En un lugar de la 
mancha de cuyo nombre"""
print(cadena)

#Para poner multilinea con simples debo usar el caracter especial \n
cadena = "En un lugar de la \n mancha de cuyo nombre"
print(cadena)

#Tampoco hace falta escapar las comillas
cadena = """En un lugar de la 
'mancha' de "cuyo" nombre"""
print(cadena)

#En las simples debemos escaparlas con \ al principio para indicar que son literals
cadena = "En un lugar de la 'mancha'\n de \"cuyo\" nombre"
print(cadena)

#IMPORTANTE
# NO ES UN COMENTARIO 
"""
ladsjldksajdsa
akldsjdsakj
ldsakjdas
"""

#Son inmutables
#Podemos acceder a una posicion de la cadena a traves del opedor [POS]
#las posiciones empiezan en 0
cadena = "Hola Mundo"
print(cadena[0])
print(cadena[1])

#Admite posiciones negativas, que se cuentan desde el FINAL de la cadena
#siendo -1 la ultima posicion
cadena = "Hola Mundo"
print(cadena[-1])
print(cadena[-2])

#Las posiciones deben existir
cadena = "Hola Mundo"
print(cadena[100])

#OJO con la inmutabilidad
cadena = "Hola Mundo"
cadena[0] = "h"
print(cadena)

#Podemos cambiar toda la cadena, pero no una posicion en particular
cadena = "Hola Mundo"
cadena = "h"
print(cadena)

#Las cadenas tiene funciones que se le pueden aplicar
# la primera es len() que nos devuelve la longitud de la cadena
cadena = "Hola Mundo"
print(len(cadena))

#Tenemos el slicing, que es aplicable a elementos iterables, son aquellos
#objetos que estan compuestos por otros elementos, el string esta copuesto de letras
#esto tambien se aplica a listas y a tuplas
# CADENA[POS_INI:POS_FIN:STEP]
# POS_INI => a partir de donde nos muestra el substring, valor por defecto 0
# POS_FIN => posicion final hasta donde llega, es pos_fin -1, valor por defecto la longitud de la cadena
# STEP => paso o salto entre elementos del slice, valor por defecto 1
cadena = "Hola Mundo"
print(cadena[0:4:1])
print(cadena[0:10:1])
print(cadena[5:10:1])
print(cadena[0:10:2])
print(cadena[0:10:5])
#IMPORTANTE n comprueba limites
#si el fin es mas grande que la longitud pilla hasta la lingitud
print(cadena[0:40000:1])
print(cadena[100:10:1]) #cadena vacia
print(cadena[0:10:11010100101010]) #Solo la H

#Admite indices negativos
cadena = "Hola Mundo"
print(cadena[-1:5:1]) #cadena vacia
print(cadena[5:-1:1]) #Mund
print(cadena[-1:-10:-1]) #odnuM alo invierten
print(cadena[::]) #COPIA de la cadena

#Los strings son objetos y tienen metodos
#Comprobacion, que empiezan por is
cadena = "hola"
print(cadena.isupper()) #comprueba si esta toda la cadena en mayusculas
print(cadena.islower()) #con minusculas
print(cadena.isnumeric()) #comprueba si esta compuesta de numeros
#Devuelven copias NO modifican la original
#Tambien tenemos de formato, para eliminar espacios, o centrar textos
cadena = "@@@@@@@@@@@hola@@@@@@@@@@@@"
print(cadena)
print(cadena.strip()) #elimina espacios en blanco a la derecha y a la izquierda
print(cadena.strip("@"))
#Tenemos la version por la derecha y la izquierda
print(cadena.rstrip("@"))
print(cadena.lstrip("@"))

#Metodos de busqueda, find e index que nos devuelven la posicion
#de la primera letra de la cadena que buscamos, y solo de la primera ocurrencia
cadena = "hola que tal hola bien que"
print(cadena.find("que"))
print(cadena.index("que"))
#Aditen mas argumentos, que es la posicion de inicio de busqueda y de fin
cadena = "hola que tal hola bien que"
print(cadena.find("que",6))
print(cadena.index("que",6))

#Tambien podemos poner posicion de fin
print(cadena.find("que",6,100))
print(cadena.index("que",6,100))

#La diferencia es si no encuentra lo que busca
cadena = "hola que tal hola bien que"
print(cadena.find("adios")) #devuelve -1 si no lo encuentra
print(cadena.index("adios")) #devuelve un error si no lo encuentra

#Operadores en python
#Aritmeticos
print(2 + 1) #suma
print(2 - 1) #resta
print(2 * 1) #multiplicacion
print(2 / 1) #division
print(2 // 1) #cociente de la division entera
print(2 % 1) # resto de la division entera

#Los operadores estan sobrecargados
print("hola "+ "que") #concatena, es decir las une
print("hola" * 10) #repite la cadena tantas veces como le indica la multiplicacion

#Operadores logicos que aplican el algebra de Bool es decir true y False
# and, or y not
#and
print(False and False)
print(False and True)
print(True and False)
print(True and True)

#or
print(False or False)
print(False or True)
print(True or False)
print(True or True)

#not
print(not False)
print(not True)

#Operadores binarios, hago referencia a trabajar a nivel de 0 y 1
#OJO NO es lo mismo qu los logicos
# & (and), | (or), ~ (not), ^ (exor)
#and &
print(0 & 0)
print(0 & 1)
print(1 & 0)
print(1 & 1)

#not |
print(0 | 0)
print(0 | 1)
print(1 | 0)
print(1 | 1)

#not ~
print(~1)
print(~0)

#Los operadores a nivel de bit trabajan a bajo nivel
print(5 & 4)
#5 => 101
#4 => 100
#& => 100 => 4

print(5 | 4)
#5 => 101
#4 => 100
#| => 101

print(~1) # -2
#En binario no hay forma de representar numeros negativos, hubo que inventarla
#El primero es Signo Magnitud
#es supersencillo, lo que hacemos le añadimos un bit mas a la izquiera
#que es el bit de signo si es 1 es un valor negativo y si es 0 positivo
# 1 => - 
# 0 =>+
# 5  => 0 101
# -5 => 1 101
#Es malo para los pcs, y hay un problema el doble 0
# +0 => 0000
# -0 => 1000

#Complemento a uno
#es facil para el ordenador pero mas dificl para el ser humano
#se trata de complementar bit a bit los elementos del numero
# 5 => 0101
#-5 => 1010
#seguimos con el problema del 0
# +0 => 0000
# -0 => 1111

#Complemento a dos
#hacer el complemento a uno y al resultado sumarle uno
# 5 => 0101
# c2 => 1010 + 1  = 1011
#Ventaja facil para el pc y no hay problema del 0
# +0 => 0000
# -0 => 1111 + 0001 = 0000

#Operador exor ^, es el or exclusivo

print(0 ^ 0)
print(0 ^ 1)
print(1 ^ 0)
print(1 ^ 1)

#Es un operador muy usado para el cifrado
mensaje = 5
clave = 4
cifrado = mensaje ^ clave
print(cifrado)
descifrado = cifrado ^ clave
print(descifrado)

#Hay dos mas que son << y >>, los deplazamientos
print(2 >> 1)
#2 = 10
#2 >> 1 => 10 >> 1 => 01 
#division en base 2 binario

print(2 << 1)
#2 => 10
#2 << 1 => 10 << 1 => 100
#equivalente a haer una potencia de 2

#Listas
#Es un conjunto ORDENADO de elementos que pueden ser de cualquier tipo
#Puedes ser heterogeneas, es decir se puden mezclar diferentes tipos de datos
#Son MUTABLES, esto quiere decir que cuando lo modificacion NO cambia el id
#para crear una lista vacia 2 formas
#con la funcion list
lista = list()
print(type(lista))
print(lista)

#Usando []
lista = []
print(type(lista))
print(lista)

#Para creala con elemento basta con ponerlos separados por comas
lista = [1,2,3,4,5]
print(type(lista))
print(lista)

#Heterogeneas
lista = [1,2,3,4,5,"hola",[1,2],3.4]
print(type(lista))
print(lista)

#Mutables
#Podemos hacer lo que en informatica se conoce como CRUD (Crear Leer Actualizar y Borrar)
#Para acceder a los elementos igual que en los strings, y tambien se le aplican igual los slice
lista = [1,2,3,4,5]
print(lista[2])
print(lista[0:2:1])

#Para añadir tenemos 2 metodos
# el primer es append(ELEM), que añade el elemento al final
lista = [1,2,3,4,5]
lista.append("hola")
print(lista)

#El metodo insert(POS,ELEM), esto inserta en la posicion que le pasamos que le pasamos como primer agumento
lista = [1,2,3,4,5]
lista.insert(1,"hola")
print(lista)

#Para modificar se hace a traves de la posicion
lista = [1,2,3,4,5]
lista[2]="hola"
print(lista)

#Podemos borrar para ello tenemos 2 formas
# la primera el operador del y la posicion
lista = [1,2,3,4,5]
del lista[2]
print(lista)

#Es el metodo remove(ELEM),que eliminar la primera ocurrencia que encuentra del elemento
lista = [1,2,3,4,5]
lista.remove(3)
print(lista)

#Tenemos 2 operadores muy utiles
# el operador in nos devuelve True o False si un determinado elemento esta o no en un elemento iterab (lista, string, tupla..)
lista = [1,2,3,4,5]
print(1 in lista)
print("hola" in lista)

#Tenemos el operador is que comprueba si dos objetos son el mismo (mira los ids)
numero = 10
numero_2 = 10
print(numero is numero_2)
lista = [1,2,3]
lista_2 = [1,2,3]
print(lista is lista_2)

#Tenemos funciones para listas numericas
lista = [1,2,3,4,5]
print(max(lista)) #devuelve el valor mas alto
print(min(lista)) # devuelve el valor mas pequeño
print(sum(lista))#nos devuelve la suma de todos los elementos

#Tambien tiene metodos, estos metodos SI modifican la lista
lista = [1,2,3,4,5]
lista.reverse() #esto invierte el orden
print(lista)

lista = [1,3,20,4,0,5]
lista.sort() #ordena la lista
print(lista)

#La funcion de orden
lista = ["d","a","c","b"]
lista.sort() 
print(lista)

#algunas a medio camino con los strings
cadena = "hola que tal"
#el metodo split(CARACTER), que divide la cadena en una lista usando como referencia el caracter que se le pasa como arguemnto
lista = cadena.split(" ")
print(lista)

#Y tenemos la inversa que es el "PEGAMENTO".join(lista)
#unir una lista de strings en un unico string
lista = ["hola","que","tal"]
print(",".join(lista))


#Tuplas
#Son como una lista pero inmutables, es decir tienen todas las caracteristicas
#y metodos y funciones de una lista, menos la parte de que se pueden modificar
#para crear una tupla 2 formas
tupla = tuple()
print(type(tupla))
print(tupla)

#usando ()
tupla = ()
print(type(tupla))
print(tupla)

#Parametre valore igual que una lista
tupla = (1,2,"hola")
print(type(tupla))
print(tupla)

#Todo igual salvo la modiciacion
tupla = (1,2,"hola")
print(tupla[1])
print(tupla[0:2:1])
tupla[1] = "ERROR" #Error

#Diccionarios
#Es un conjunto de elementos, que no tienen orden, y que vienen definidos por
#un conjunto de pares clave:valor
#la clave puede ser cualqueir objeto serializable (que se pueda convertir en string)
#y el valor cualquier tipo de dato de python
#Son MUTABLES, al igual que las listas podremos hacer operaciones CRUD
#para definir un diccionario 2 formas
# funcion dict
diccionario = dict()
print(type(diccionario))
print(diccionario)

#O la segunda con llaves
diccionario = {}
print(type(diccionario))
print(diccionario)

#Podemos crearlo con elementos siguiendo el concepto de clave:valor
diccionario = {"nombre": "Jane", "telefono":782732823}
print(type(diccionario))
print(diccionario)

#Para acceder a los elementos hay 2 formas
# la primera a traves de la clave
diccionario = {"nombre": "Jane", "telefono":782732823}
print(diccionario["nombre"])

#La segunda forma el metodo get("CLAVE")
diccionario = {"nombre": "Jane", "telefono":782732823}
print(diccionario.get("nombre"))

#La diferencia es si no existe la clave
diccionario = {"nombre": "Jane", "telefono":782732823}
print(diccionario["apellido"]) #esto da error si no existe
print(diccionario.get("apellido")) #devuele un None

#Ademas el get nos permite poner un segundo parametro para definr ese valro por defecto
#si no queremos que sea None
print(diccionario.get("apellido","VALOR POR DEFECTO"))

#Podemos añadir nuevos elementos y editar elementos existentes
diccionario = {"nombre": "Jane", "telefono":782732823}

#Editar con la clave
diccionario["nombre"] = "Paco"
print(diccionario)

#Para añadir es poner una clave que no existe
diccionario["apellido"] = "Rambo"
print(diccionario)

#Podemos borrar una clave, tenemos 2 formas
# con del y la clave
diccionario = {"nombre": "Jane", "telefono":782732823}
del diccionario["nombre"]
print(diccionario)

#Es el metodo pop(CLAVE), este metodo devuelve el valor
diccionario = {"nombre": "Jane", "telefono":782732823}
diccionario.pop("nombre")
print(diccionario)

#podemos recuperarlo
diccionario = {"nombre": "Jane", "telefono":782732823}
valor = diccionario.pop("nombre")
print(diccionario)
print(valor)

#Tenemos que los metodos len(), operador in y el is
diccionario = {"nombre": "Jane", "telefono":782732823}
print(len(diccionario))
print("nombre" in diccionario) #Aqui comprueba con las claves

#tambien tiene 3 metodos mas para manipular las claves y los valores
diccionario = {"nombre": "Jane", "telefono":782732823}
print(list(diccionario.keys()))
print(list(diccionario.values()))
print(list(diccionario.items()))

#Conjuntos
#Es una coleccion de elementos, SIN duplicacos, SIN orden, y puede ser de cualqueir tipo
#soporta el algebra de conjuntos (union, interesccion, ..)
#dos formas o con set()
conjunto = set()
print(type(conjunto))
print(conjunto)
#no vacio con {}
conjunto = {1,2,3,4}
print(type(conjunto))
print(conjunto)

#No duplicados
conjunto = {1,2,3,4,1,1,1,1,1}
print(type(conjunto))
print(conjunto)

#Algebra de conjuntos
automoviles = {"BMW", "SEAT", "FERRARI"}
motociclestas = {"BMW","DUCATTI", "KAWA"}

print(automoviles & motociclestas) #interseccion, los fabricantes e motos y coches
print(automoviles - motociclestas) #diferencia fabricantes de coches que no hacen motos




