#1. Imprimir “Hola mundo” por pantalla.
print("Hola Mundo")

#2. Crear dos variables numéricas, sumarlas y mostrar el resultado

numero_1 = 10
numero_2 = 20

resultado = numero_1 + numero_2

print(resultado)

#Opcion B
numero_1 = 10
numero_2 = 20

print(numero_1 + numero_2)

#Opcion C
print(10 + 5)

#3. Mostrar el precio del IVA de un producto con un valor de 100 y su precio final.
importe = 100
iva = 21

importe_iva = importe * (iva/100)
importe_total = importe_iva + importe

print("importe total", importe_total)
print("importe del iva", importe_iva)

#Opcion B
importe = 100
iva = 0.21

importe_total = importe * (1+iva)

print("importe total", importe_total)

#Opcion C
print("importe total", 100 *(1.21))


#4. De dos números, saber cual es el mayor.
numero_1 = 100
numero_2 = 200

if(numero_1 > numero_2):
    print("Numero 1 es mayor")
elif(numero_2 > numero_1):
    print("numero 2 es mayor")
else:
    print("Son iguales")

#Opcion B
numero_1 = 100
numero_2 = 200

if(numero_1 > numero_2):
    print("Numero 1 es mayor")
else:
    print("Numero 2 es mayor o igual")

#Opcion C equivalente a la opcion B
numero_1 = 100
numero_2 = 200

mayor = "Numero 1" if numero_1 > numero_2 else "Numero 2 es mayor o igual"

print(mayor)

#Opcion D equivalente a la A
numero_1 = 100
numero_2 = 200

mayor = "Numero 1" if numero_1 > numero_2 else "Numero 2" if numero_1 != numero_2 else "Son iguales"

print(mayor)

#Opcion E
numero_1 = 100
numero_2 = 200

#Con max y min
print("El mayor es ", max(numero_1, numero_2))


#5. Crea una variable numérica y si esta entre 0 y 10, 
# mostrar un mensaje indicándolo.
numero = 4

if(numero >= 0 and numero <=10):
    print("Esta entre 0 y 10")

#Opcion B
numero = 4
if(0 <= numero <= 10):
    print("Esta entre 0 y 10")

#Opcion C
numero = 4
resultado = "Esta entre 0 y 10" if (0 <= numero <= 10) else ""
print(resultado)

#opcion D
numero = 4

if numero in range(0,11):
    print("Esta entre 0 y 10")

#6. Mostrar con un while los números del 1 al 100.
numero = 1

while numero <=100:
    print(numero)
    numero = numero + 1

#Opcion B
numero = 1

while numero <100:
    print(numero)
    numero = numero + 1
else:
    print(numero)

#Opcion C
numero = 0

while numero < 100:
    numero = numero + 1
    print(numero)

#Reflexecion
numero = 1

while numero <=100:
    print(numero)
    numero += 1 #es equivalente a numero = numero + 1

#7. Mostrar con un for los números del 1 al 100.

for numero in range(1,101):
    print(numero)


#8. Mostrar los números pares entre 1 al 100.

for numero in range(1,101):
    if (numero % 2 == 0):
        print(numero)

#Opcion B
numero = 1

while numero <=100:
    if(numero % 2 ==0):
        print(numero)
    
    numero = numero + 1

#Opcion C
for numero in range(2,101,2):
    print(numero)


#9. Mostrar los caracteres de la cadena “Hola mundo”.
cadena = "hola mundo"

for letra in cadena:
    print(letra)

#Opcion B
cadena = "hola mundo"
posicion = 0

while posicion < len(cadena):
    print(cadena[posicion])
    posicion = posicion + 1

#Opcion C

cadena = "hola mundo"

for posicion in range(0,len(cadena)+1):
    print(cadena[posicion])


#10. Mostrar los caracteres de la cadena “Hola mundo” al reves.
cadena = "hola mundo"

for letra in cadena[::-1]:
    print(letra)

#Opcion B
cadena = "hola mundo"
posicion = len(cadena)

while posicion >= 0:
    print(cadena[posicion])
    posicion = posicion - 1

#Opcion C

cadena = "hola mundo"

for posicion in range(len(cadena),0):
    print(cadena[posicion])

#Opcion D
cadena = "hola mundo"

for posicion in range(-1,-len(cadena),-1):
    print(cadena[posicion])

#11. Generar un rango entre 0 y 10
rango = range(11)
for numero in rango:
    print(numero)

#Opcion B
rango = range(11)
print(list(rango))

#Opcion C
rango = range(0,11,1)
for numero in rango:
    print(numero)

#Opcion D
rango = range(0,11)
for numero in rango:
    print(numero)

# Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas y 
# con los 2 primeros caracteres intercambiados. 
# Por ejemplo, hola mundo pasaría a mula hondo
# Tips
# 1 => pedir valores por teclado cadena = input("Introduce la cadena "), es 2 inputs
# 2 => tenemos que crear una cadena nueva con los caracteres intercambiados, no vale manipular
# un string existente porque son INMUTABLES, por una lado el operador + está sobrecargado
# y nos permite "unir" dos cadenas
# resultado = cadena_1 + " " + cadena_2
# para intercambiar, pensad en las posiciones
# resultado = cadena_2[0] + cadena_2[1] + RESTO_CARACTERES_DE_CADENA_1
# Resto de caracteres el tip son los slices, debemos tener un slice que pille desde
# el segundo caracter hasta el final: cadena_1[POS_INI:POS_FIN:STEP]
cadena_1 = input("Introduce cadena 1 ")
cadena_2 = input("Introduce cadena 2 ")

resultado_1 = cadena_2[0] + cadena_2[1] + cadena_1[2::]
resultado_2 = cadena_1[0] + cadena_1[1] + cadena_2[2::]

resultado = resultado_1 + " " + resultado_2

print(resultado)

#Opcion B
cadena_1 = input("Introduce cadena 1 ")
cadena_2 = input("Introduce cadena 2 ")

resultado = cadena_2[0] + cadena_2[1] + cadena_1[2::] + " " + cadena_1[0] + cadena_1[1] + cadena_2[2::]

print(resultado)

#Opcion C, no me acuerdo de los slices
cadena_1 = input("Introduce cadena 1 ")
cadena_2 = input("Introduce cadena 2 ")

resultado_1 = cadena_2[0] + cadena_2[1]

for letra in range(2,len(cadena_1)):
    resultado_1 = resultado_1 + letra

resultado_2 = cadena_1[0] + cadena_1[1]

for letra in range(2,len(cadena_2)):
    resultado_2 = resultado_2 + letra

resultado = resultado_1 + " " + resultado_2

print(resultado)

#opcion Pro
cadena_1 = input("Introduce cadena 1 ")
cadena_2 = input("Introduce cadena 2 ")

resultado_1 = cadena_2[0:2:1] + cadena_1[2::]
resultado_2 = cadena_1[0:2:1] + cadena_2[2::]

resultado = resultado_1 + " " + resultado_2

print(resultado)
#Aprovechando los avlores por defecto
cadena_1 = input("Introduce cadena 1 ")
cadena_2 = input("Introduce cadena 2 ")

resultado_1 = cadena_2[:2] + cadena_1[2:]
resultado_2 = cadena_1[:2] + cadena_2[2:]

resultado = resultado_1 + " " + resultado_2

print(resultado)

#Alvaro
cadena1 = input("Introduce la primera palabra: ")
cadena2 = input("Introduce la segunda palabra: ")
cadena_final1 = cadena2[0] + cadena1[1:]
cadena_final2 = cadena1[0] + cadena2[1:]
print(cadena_final1 + " " + cadena_final2)

#13. Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.
#Nuestro objetivo es adivinar el número. 
# Si fallamos nos dirán si es mayor o menor que el número #buscado. 
# También poner el número de intentos requeridos.
#Tips
# 1=> generar un nuemro aleatori
# import random
# numero = random.randint(1,101) #sto gnera un numero entre 1 a 100 de forma aleatoria
# 2 => debemos pedir el numero mientras NO se acierta asi que debemos poner un while
# que compruebe que acertamos o no
# 3 => dentro del while si no acertamos debemos tener un if, para comprobar si es mayor o menor
# y asi con el print() indicar al usuario si es mayor o menor que el numero buscado
# 4 => acordaros que al pedir un numero por teclado lo lee como un string
# asi que debemos convertirlo numero = int(input("Introduce el numero ")) 
import random

numero_a_adivinar = random.randint(1,101)

numero_usuario = int(input("Introduce un numero "))
numero_intentos = 1

while(numero_a_adivinar != numero_usuario):
    if numero_a_adivinar > numero_usuario:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    numero_usuario = int(input("Introduce un numero "))
    numero_intentos = numero_intentos + 1
    
else:
    print("Felicidades has acertado")
    print("Has necesitado",numero_intentos)

#Opcion B
import random

numero_a_adivinar = random.randint(1,101)
numero_usuario = 200
numero_intentos = 0

while(numero_a_adivinar != numero_usuario):
    numero_usuario = int(input("Introduce un numero "))
    numero_intentos = numero_intentos + 1

    if numero_a_adivinar > numero_usuario:
        print("El numero es mayor")
    else:
        print("El numero es menor")  
else:
    print("Felicidades has acertado")
    print("Has necesitado",numero_intentos)

#Si tuvieramos un numero maximo de intentos
import random

numero_a_adivinar = random.randint(1,101)

numero_usuario = int(input("Introduce un numero "))
numero_maximo_intentos = 3
numero_intentos = 1

while((numero_a_adivinar != numero_usuario) and (numero_maximo_intentos != numero_intentos)):
    if numero_a_adivinar > numero_usuario:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    numero_usuario = int(input("Introduce un numero "))
    numero_intentos = numero_intentos + 1
    
if numero_maximo_intentos == numero_intentos:
    print("No has acertado en el numero maximo")
else:
    print("Felicidades has acertado")
    print("Has necesitado",numero_intentos)

#Solucion "creativos"
import random

numero_a_adivinar = random.randint(1,101)

numero_usuario = int(input("Introduce un numero "))
numero_intentos = 1
numero_maximo_intentos = 3

while(numero_a_adivinar != numero_usuario):
    if numero_a_adivinar > numero_usuario:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    numero_usuario = int(input("Introduce un numero "))
    numero_intentos = numero_intentos + 1
    if numero_intentos == numero_maximo_intentos:
        print("loooser has perdido")
        break
else:
    print("Felicidades has acertado")
    print("Has necesitado",numero_intentos)

#Andres

intentos=5
numero=randint(1, 100)
print(numero)
res="Fallaste"
while(intentos>0):
    print(f"Tienes {intentos} intentos")
    data=int(input("Introduce el numero que creas: "))
    if data==numero:
        res="Acertaste"
        intentos=-1
    if data>numero:
        print("El numero es mas pequeño")
    else:
        print("El numero es más grande")
    intentos-=1
print(res)

#Juan
import random
num = random.randint(1,101)
cont = 1
adivinado = False
print(num)
intentos = input("Introduce numero de intentos: ")
while ((cont <= int(intentos)) and (adivinado != True)):
    numAdivina = input("Introduce un numero: ")
    if (int(numAdivina) == num):
        print("Has adivinado el numero")
        adivinado = True
    else:
        print("No es el numero correcto")
    cont = cont + 1
else:
    if (adivinado != True):
        print("No has logrado adivinar el número") 
        print("El número generado era: " + str(num))

#14. Escribir un programa que guarde en una variable el diccionario 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o 
# un mensaje de aviso si la #divisa no está en el diccionario.
# Tips 
# dccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# 1 - pide el nombre "Euro", "Dollar" o "Yen" y devuelve el simbilo
# 2 - ojo con las mayusculas y minusculas "euro", "DOLLAR", asi que debeso usar el capitalize()
# 3 - decidir si usamos directamente la clave (obligados a poner un if con el operador in)
#  o el get del diccionario
diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

nombre = input("Introduce el nombre de la divisa")

nombre = nombre.capitalize() 

if nombre in diccionario:
    print(diccionario[nombre])
else:
    print("La divisa no esta")

#Opcion B
diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

nombre = input("Introduce el nombre de la divisa")

nombre = nombre.capitalize() 

resultado = diccionario.get(nombre,"La divisa no existe")
print(resultado)

#15. Escribir un programa que pregunte al usuario su 
# nombre, edad, dirección y teléfono y lo 
# guarde en un diccionario. Después debe mostrar por 
# pantalla el mensaje <nombre> tiene <edad> #años, vive en <dirección> 
# y su número de teléfono es <teléfono>.
# Tips:
# 1 => debemos tener tantos inputs como campos, nombre, edaad, direccion
# nombre = input("Dime tu nombre ")
# 2 => creadmos el diccionario y como valor de cada clave ponemos lo leido por teclado
# diccionario["nombre"] = nombre
# 3 => una ve< tenemos todo debemos usar el print, para imprimir todos los valors en el formato indicado
#print(diccionario["nombre","tiene", diccionario["edad"],)
# la opcion B es crear un string que junto todo y para eso usarias el +

nombre = input("Dime tu nombre ")
edad = int(input("Dime tu edad "))
direccion = input("Dime tu direccion ")
telefono = input("Dime tu telefono ")

diccionario = {}
diccionario["nombre"] = nombre
diccionario["edad"] = edad
diccionario["direccion"] = direccion
diccionario["telefono"] = telefono


print(diccionario["nombre"],"tiene", diccionario["edad"],"años", "vive en", 
diccionario["direccion"], "y su número de teléfono es", diccionario["telefono"])


#Opcion B
nombre = input("Dime tu nombre ")
edad = int(input("Dime tu edad "))
direccion = input("Dime tu direccion ")
telefono = input("Dime tu telefono ")

diccionario = {
    "nombre":nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}

salida =diccionario["nombre"] + " tiene " + str(diccionario["edad"]) + "años, vive en " + diccionario["direccion"] + "y su número de teléfono es " + diccionario["telefono"]
print(salida)

#16. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y 
# muestre por pantalla la #misma fecha en formato dd de <mes> de aaaa donde 
# <mes> es el nombre del mes.
#Tip
#1 => solo pedimos un string dd/mm/aaaa
#2 => NO se puede usar el module date de python
#3 => usaremos el split("/") del string para qudarnos con la parte de dia mes y año
#4 => para imprimir el mes, debeis o crear un diccionario o una lista con los meses
# meses = ["Enero","Febrero"..]
# diccioanrio_meses = {0:"Enero",1:"Febrero"}

fecha = input("Introduce la fehca en formato dd/mm/aaaa")
parte_fecha = fecha.split("/")

dia = int(parte_fecha[0])
mes = int(parte_fecha[1])
ano = int(parte_fecha[2])

diccionario_meses = {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril"}

print(dia,"de",diccionario_meses[mes],"de",ano)

#Opcion B
fecha = input("Introduce la fehca en formato dd/mm/aaaa")
parte_fecha = fecha.split("/")

dia = int(parte_fecha[0])
mes = int(parte_fecha[1])
ano = int(parte_fecha[2])

tupla_meses = {"Enero","Febrero","Marzo","Abril"}

print(dia,"de",tupla_meses[mes -1],"de",ano)

#Opcion C slicing
fecha = input("Introduce la fehca en formato dd/mm/aaaa")

dia = int(fecha[0:2])
mes = int(fecha[3:5])
ano = int(fecha[6:])

tupla_meses = {"Enero","Febrero","Marzo","Abril"}

print(dia,"de",tupla_meses[mes -1],"de",ano)

#17. Escribir un programa que cree un diccionario vacío y lo vaya 
# llenado con información sobre #una persona (por ejemplo nombre, edad, sexo, 
# teléfono, correo electrónico, etc.) que se le pida #al usuario. Cada vez que se añada 
# un nuevo dato debe imprimirse el contenido del diccionario.
#Tip,
# 1=> el diccionario debe estar vacio
# 2 => tener 2 inputs, uno que pida la clave y otro el valor
# 3 => los almacenamos y mostramos

diccionario = {}
while clave == "salir":
    clave = input("Introduce que tipo de dato vas a guardar (nombre, telefono, etc..) pon salir para terminar ")
    if clave!="salir":
        valor = input("Introduce el valor a almacenar")
        diccionario[clave] = valor
        print(diccionario)


#18. Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, #Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.
#Simplemente perdir nombres de aignatoras y guardarlas en una lista, en principio bucle infinito
#se puede poner condicion de fin, pero no es obligatorio
lista_asignaturas = []

while True:
    asignatura = input("Introduce el nombre de la asignatura ")
    lista_asignaturas.append(asignatura)
    print(lista_asignaturas)


#Sin bucle infinito

lista_asignaturas = []
asignatura = input("Introduce el nombre de la asignatura (salir para terminar) ")

while asignatura != "salir":
    lista_asignaturas.append(asignatura)
    asignatura = input("Introduce el nombre de la asignatura (salir para terminar) ")
else:
    print(lista_asignaturas)

#19. Escribir un programa que pregunte al usuario los números 
# ganadores de la lotería primitiva, #
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

#Tip
# Vamos a pedir 6 numeros, debemos usar un bucle, while o un for
# se guardan en una lista
# se ordena y finalmente se imprime

lista_numeros = []

for i in range(6):
    numero = int(input("introduce el numero "))
    lista_numeros.append(numero)

lista_numeros.sort()

print(lista_numeros)



#20. Escribir un programa que almacene en una lista los números del 1 al 10 y 
# los muestre por #pantalla en orden inverso separados por comas.
# Tips:
# 1 => generar la lista con un range
# 2 => invertir orden, recordad el uso [::-1]
# 3 => juntarlo todo en un unico string ",".join(lista), ver metodo join en los apuntes
lista_numeros = list(range(1,11))
lista_numeros = lista_numero[::-1]
print(",".join(str(lista_numeros)))

#En una sola linea
print(",".join(str(list(range(1,11))[::-1])))

#Ojo con el join solo funciona con listas de strings
lista_numeros = []

for numero in range(1,11):
    lista_numeros.append(str(numero))

print(",".join(lista_numeros[::-1]))

#insertar por el principio
lista_numeros = []

for numero in range(1,11):
    lista_numeros.insert(0,str(numero))

print(",".join(lista_numeros))

#Reverse
lista_numeros = []

for numero in range(1,11):
    lista_numeros.append(str(numero))

lista_numeros.reversed()

print(",".join(lista_numeros))

#Tambien se ouede hacer juntanto todo en un string de salida, lo veremos el proximo dia

#21. Escribir un programa que almacene el abecedario en una lista, 
# elimine de la lista las #letras que ocupen posiciones múltiplos de 3, y 
# muestre por pantalla la lista resultante.
#Tip:
# 1=> se puede generar el abecedario con un for usando las funciones ord() chr()
abecedario = ["a","b","c"]

#Generamos el abecedario
abecedario = []

for numero in range(ord("a"),ord("z")+1):
    abecedario.append(chr(numero))
#No funciona porque el rango se crea la primera vez y al ir borrando elementos
#la logutd del diccionar es mas pequeña y llega un momento que rompe
for posicion in range(len(abecedario)):
    if posicion % 3 == 0:
        del abecedario[posicion]

print(abecedario)


#Posibles soluciones
abecedario = []

for numero in range(ord("a"),ord("z")+1):
    abecedario.append(chr(numero))

#Recorrer del final al principio mismo error pero en negativo
for posicion in range(-1,-len(abecedario),-1):
    if posicion % 3 == 0:
        del abecedario[posicion]

print(abecedario)

#Cambiamos el orden del rngo
abecedario = []

for numero in range(ord("a"),ord("z")+1):
    abecedario.append(chr(numero))

#Recorrer del final al principio 
for posicion in range(-len(abecedario),-1-1):
    if posicion % 3 == 0:
        del abecedario[posicion]

print(abecedario)

#Opcion B
abecedario = []

for numero in range(ord("a"),ord("z")+1):
    abecedario.append(chr(numero))

#lista de posiciones a borrar
posiciones_a_borrar = range(3,len(abecedario),3)
valores_a_borrar = []
for posicion in posiciones_a_borrar:
    valores_a_borrar.append(abecedario[posicion])

for letra in valores_a_borrar:
    abecedario.remove(letra)

print(abecedario)




#22. Escribir un programa que pida al usuario una palabra y muestre por 
# pantalla si es un #palíndromo.

palabra = input("Introduce la palabra ")

if(palabra == palabra[::-1]):
    print("es un palindromo")
else:
    print("no es un palindromo")

#Opcion B
palabra = input("Introduce la palabra ")

palabra = list(palabra)
palabra_inversa = palabra[::]
palabra_inversa.reversed()

if(palabra == palabra_inversa):
    print("es un palindromo")
else:
    print("no es un palindromo")

#23. Escribir un programa que almacene en una lista los siguientes 
# precios, 50, 75, 46, 22, 80, #65, 8, y 
# muestre por pantalla el menor y el mayor de los precios.
precios = [50, 75, 46, 22, 80, 65, 8]

print("El menor es ", min(precios))
print("El mayor es ", max(precios))

#24. Escribir un programa que pregunte al usuario su edad y muestre p
# or pantalla todos los años #que ha cumplido (desde 1 hasta su edad).

edad = int(input("Introduce tu edad "))

for numero in range(1,edad+1):
    print(numero)


#25. Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla #todos los números impares 
# desde 1 hasta ese número separados por comas.

numero = int(input("Introduce un numero entero positivo "))
lista = []
for valor in range(1,numero+1):
    if valor % 2 == 1:
        lista.append(str(valor))
        
print(",".join(lista))

#Opcion B con strng
numero = int(input("Introduce un numero entero positivo "))
cadena = ""
for valor in range(1,numero+1):
    if valor % 2 == 1:
        cadena = cadena + str(valor) + ","
        
print(cadena[:len(cadena)-1:])

#Opcion B
numero = input("Introduce un numero entero positivo ")

while not numero.isdecimal(): #si el string tiene carateres del 0 al 9
    numero = input("Error, introduce un numero entero positivo ")
else:
    numero = int(numero)

for valor in range(1,numero+1):
    if valor % 2 == 1:
        print(valor)

#26. Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
# #triángulo rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****

altura = int(input("Introice la altura "))
estrellas = "*"
for nivel in range(1,altura+1):
    print(estrellas)
    estrellas = estrellas + "*"

#Opcion B

altura = int(input("Introice la altura "))

for nivel in range(1,altura+1):
    print(nivel * "*")

#27. Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
# triángulo rectángulo como el de más abajo (con primos).
#1
#2 1
#3 2 1
#5 3 2 1
#7 5 3 2 1

#Descomponer el problema
# Como saber si un numero es primo, si solo puede dividir por 1 y el mismo
numero = 15

esPrimo = True

for divisor in range(numero-1,1,-1):
    if(numero % divisor == 0):
        esPrimo = False
        break

if(esPrimo == True):
    print("es primo")
else:
    print("no es primo")

#debo generar numeros primos se que como maximo debo generar tantos numeros primos como altura tengo

altura = 5
lista_primos = []
numero = 1

while altura != len(lista_primos):
    esPrimo = True

    for divisor in range(numero-1,1,-1):
        if(numero % divisor == 0):
            esPrimo = False
            break

    if(esPrimo == True):
        lista_primos.append(numero)

    numero = numero + 1

print(lista_primos)

#Ahora debemos imprimir en cada altura un determinado numero de ellos, nivel 1 imprimos 1, en el 2 imprimos dos
altura = 5
lista_primos = []
numero = 1

while altura != len(lista_primos):
    esPrimo = True

    for divisor in range(numero-1,1,-1):
        if(numero % divisor == 0):
            esPrimo = False
            break

    if(esPrimo == True):
        lista_primos.append(numero)

    numero = numero + 1

for nivel in range(1,altura+1):
    print(lista_primos[:nivel:])

#debemso imprimirlo como texto
altura = 5
lista_primos = []
numero = 1

while altura != len(lista_primos):
    esPrimo = True

    for divisor in range(numero-1,1,-1):
        if(numero % divisor == 0):
            esPrimo = False
            break

    if(esPrimo == True):
        lista_primos.append(str(numero))

    numero = numero + 1

for nivel in range(1,altura+1):
    print(" ".join(lista_primos[:-nivel:-1]))

#Añadimos los retoqeus finales
altura = int(input("Introice la altura "))
lista_primos = []
numero = 1

while altura != len(lista_primos):
    esPrimo = True

    for divisor in range(numero-1,1,-1):
        if(numero % divisor == 0):
            esPrimo = False
            break

    if(esPrimo == True):
        lista_primos.append(str(numero))

    numero = numero + 1

lista_primos.reverse()

for nivel in range(1,altura+1):
    print(" ".join(lista_primos[nivel:len(lista_primos)]))


#Andres
lista=['1','2']
number=int(input("Introducte un numero: "))
primos=2
for num in range(3, 50000):
    primo = True
    for i in range(2,num):
        if (num%i==0):
            primo = False
            break
    if primo:
        primos+=1
        lista.append(str(num))
    if primos==number:
        break
lista.reverse()
elementos=len(lista)-1
while(elementos>=0):
    print(" ".join(lista[elementos:len(lista)]))
    elementos-=1

#28. Escribir un programa que almacene la cadena de caracteres 
# contraseña en una variable, 
# #pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "abracadabra"

introduce = input("Introdue la contraseña ")
while introduce != contraseña:
    introduce = input("Error introdue la contraseña ")
else:
    print("Felicidades has acertado")