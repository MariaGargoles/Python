#Ejercicio 1
#Escribir una función que muestre por pantalla el saludo ¡Hola Mundo! cada vez que se la invoque.
def saludar():
    print("Hola Mundo")

saludar()

#Opcion 2
def saludar():
    mensaje = "Hola Mundo"
    print(mensaje)

saludar()

#Ejercicio 2
#Escribir una función a la que se le pase una cadena <nombre> 
# y muestre por pantalla el saludo ¡hola <nombre>!.
def saludo(nombre):
    print("¡hola"  + nombre + "!")

saludo("Esteban")

#Opcion 2
def saludo(nombre):
    mensaje = "¡hola"  + nombre + "!"
    print(mensaje)

saludo("Esteban")

#Opcion 3
def saludo(nombre):
    print("¡hola",nombre,"!")

saludo("Esteban")

#Ejercicio 3
#Escribir una función que reciba un número entero positivo y 
# devuelva su factorial (recordad el factorial se calcula de la siguiente manera, se debe multiplicar por todos los valores inferiores hasta el uno), por ejemplo 5 factorial seria:
#5! = 5 * 4 * 3 * 2 * 1.
def factorial(numero):
    resultado = 1
    for n in range(numero, 1, -1):
        resultado = resultado * n # iteracion 1 = 1 * 5 
        # iteracion 2 resultado = 5 * 4 
        # #iteracion 3 resultado = 20 * 3

    return resultado

print(factorial(5))

#Opcion B
def factorial(numero):
    resultado = 1
    for n in range(1, numero+1):
        resultado = resultado * n 
        # iteracion 1 = 1 * 1 
        # iteracion 2 resultado = 1 * 2 
        # #iteracion 3 resultado = 2 * 3

    return resultado

print(factorial(5))

#Opcion C
def factorial(numero):
    resultado = 1
    
    while numero > 1:
        resultado = resultado * numero
        numero = numero - 1
    
    return resultado

print(factorial(5))

#Ejercicio 4
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. Si se invoca la función sin pasarle 
# el porcentaje de IVA, deberá aplicar un 21%.
def calculo_total(cantidad_sin_iva, porcentaje_iva=0.21):
    return cantidad_sin_iva * (1 + porcentaje_iva)

print(calculo_total(100))
print(calculo_total(100,0.10))



#Ejercicio 5
#Escribir una función que calcule el área de un círculo y otra que calcule el 
# volumen de un cilindro usando la primera función.
#Area del circulo = PI * radio^2
#Volumen cillindro = Area del circulo * Altura

def area_circulo(radio):
    return 3.14 * (radio**2)

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

print(volumen_cilindro(10,5))

#Ejercicio 6
#Escribir una función que reciba una muestra de números en una lista y 
# devuelva su media.
def media(lista):
    return sum(lista)/len(lista)

lista = [1,2,3,4,5]
print(media(lista))

#Opcion B
def media(lista):
    suma = 0
    numero_elementos = 0

    for numero in lista:
        suma = suma + numero
        numero_elementos = numero_elementos + 1

    return suma/numero_elementos

lista = [1,2,3,4,5]
print(media(lista))


#Ejercicio 7
#Escribir una función que reciba una muestra de números en una lista y 
# devuelva otra lista con sus cuadrados.
def cuadrados(lista):
    cuadrados = [numero**2 for numero in lista]
    return cuadrados

lista = [1,2,3,4,5]
print(cuadrados(lista))

#Opcion B
def cuadrados(lista):
    cuadrados = []

    for numero in lista:
        cuadrados.append(numero**2)

    return cuadrados

lista = [1,2,3,4,5]
print(cuadrados(lista))

#Ejercicio 9
#Crear una función que calcule el MCD de dos número por el método de Euclides. 
# El método de Euclides es el siguiente:
#• Se divide el número mayor entre el menor.
#• Si la división es exacta, el divisor es el MCD.
#• Si la división no es exacta, dividimos el divisor entre el resto 
# obtenido y se continúa de esta forma hasta obtener una división exacta, 
# siendo el último divisor el MCD.
#• Crea un programa principal que lea dos números enteros y muestre el MCD.


def mcd(numero_1, numero_2):
    #ordenamos
    if numero_1 > numero_2:
        mayor = numero_1
        menor = numero_2
    else:
        mayor = numero_2
        menor = numero_1

    if(mayor % menor == 0):
        return menor
    else:
        mayor, menor = menor, mayor % menor
        if(mayor % menor == 0):
            return menor

#Ponemos un bucle
# 

def mcd(numero_1, numero_2):
    #ordenamos
    if numero_1 > numero_2:
        mayor = numero_1
        menor = numero_2
    else:
        mayor = numero_2
        menor = numero_1

    while (mayor % menor != 0):
            mayor, menor = menor, mayor % menor
    else:
        return menor


#Opcion B

def mcd(numero_1, numero_2):
    #ordenamos
    mayor, menor = max(numero_1,numero_2), min(numero_1,numero_2)
    
    while (mayor % menor != 0):
            mayor, menor = menor, mayor % menor
    else:
        return menor

#Opcion C
def mcd(numero_1, numero_2):
    #ordenamos
    mayor = numero_1 if numero_1 > numero_2 else numero_2
    menor = numero_1 if numero_1 < numero_2 else numero_2
    
    while (mayor % menor != 0):
            mayor, menor = menor, mayor % menor
    else:
        return menor

print(mcd(18,24))

#Ejercicio 10
#Escribir una función que convierta un número decimal en binario.
#Para hacer la conversión de decimal a binario, hay que ir dividiendo el número decimal entre
#dos y anotar en una columna a la derecha el resto (un 0 si el resultado de la división es par y un
#1 si es impar).
#La lista de ceros y unos leídos de abajo a arriba es el resultado.
#Ejemplo: vamos a pasar a binario 79
#79 1 (impar). Dividimos entre dos:
#39 1 (impar). Dividimos entre dos:
#19 1 (impar). Dividimos entre dos:
#9 1 (impar). Dividimos entre dos:
#4 0 (par). Dividimos entre dos:
#2 0 (par). Dividimos entre dos:
#1 1 (impar).
#Por tanto, 79 = 1001111

def binario(numero):
    return (str(bin(numero))[2:])

print(binario(10))


def binario(numero):

    restos = []
    while numero // 2 != 0:
        resto = numero % 2
        restos.append(str(resto))
        numero = numero // 2
    else:
        resto = numero % 2
        restos.append(str(resto))

    restos = restos[::-1]
    return "".join(restos)

print(binario(10))


#Ejercicio 11
#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado
#con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia
#primera funcion
#   recibe = "hola que hola bien tal adios"
#   devuelve = {"hola":2,"que":1,"bien":1,"tal":1,"adios":1}
#tip: usar el metodo split() de la cadena para dividir los elemtnos en una lista
# lista = recibe.split(" ")
# lista[0] = hola
# lista[1] = que
# lista[2] = hola
# recorrer la lista y contar cuantos datos tenemos de cada tipo 

def diccionario(cadena):
    lista = cadena.split(" ")
    vuelta = {}

    for palabra in lista:
        if(palabra != "," and palabra != ""):
            vuelta[palabra]=vuelta.get(palabra,0) + 1
    
    return vuelta


recibe = "hola que hola bien tal adios"
print(diccionario(recibe))

#Opcion B
def diccionario(cadena):
    lista = cadena.split(" ")
    vuelta = {}

    for palabra in lista:
        if palabra in vuelta:
            vuelta[palabra]=vuelta[palabra] + 1
        else:
            vuelta[palabra]=1
    return vuelta


recibe = "hola que hola bien tal adios"
print(diccionario(recibe))

#segunda funcion
#   recibe = {"hola":2,"que":1,"bien":1,"tal":1,"adios":1}
#   devuelve = ("hola",2)
#tip es recorrer todos los alores y cuando el encontremos le mas grande quedarnos con la clae y montar la tupla

recibe = {"hola":2,"que":1,"bien":1,"tal":1,"adios":1}

def tupla_repetida(diccionario):
    valor_mas_alto = 0
    clave_mas_alta = ""

    for clave,valor in diccionario.items():
        if valor > valor_mas_alto:
            valor_mas_alto = valor
            clave_mas_alta = clave

    return (clave_mas_alta, valor_mas_alto)

print(tupla_repetida(recibe))

#Opcion B
recibe = {"hola":2,"que":1,"bien":1,"tal":1,"adios":1}

def tupla_repetida(diccionario):
    valor_mas_alto = 0
    clave_mas_alta = ""

    for clave in diccionario:
        if diccionario[clave] > valor_mas_alto:
            valor_mas_alto = diccionario[clave]
            clave_mas_alta = clave

    return (clave_mas_alta, valor_mas_alto)

print(tupla_repetida(recibe))

#Ejercicio 12
#Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en
#pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2
#espacios antes del texto).
# recibe ="hola mundo"
# devolver = "                              hola mundo                              "
#tip usar el operador * con un strinf " " y un entero

def EscribirCentrado(texto):
    espacios_anadir = (80 - len(texto))//2
    return (espacios_anadir * " ") + texto + (espacios_anadir * " ") + " " if  (len(texto)%2)!=0 else ""

recibe ="hola mundo"
print(EscribirCentrado(recibe))

#Ejercicio 13
#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo
#del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve True si el primero es
#múltiplo del segundo.
#tip: para saber si un numero es multiplo de otro operador % que si el resultado es 0 es multiplo

def EsMultiplo(numero_1, numero_2):
    if numero_1 % numero_2 == 0:
        return True
    else:
        return False


#Opcion B

def EsMultiplo(numero_1, numero_2):
    return (numero_1 % numero_2 == 0)

#Opcion C
def EsMultiplo(numero_1, numero_2):
    return True if numero_1 % numero_1 == 0 else False

numero_1 = int(input("Introdice el numero 1 "))
numero_2 = int(input("Introdice el numero 2 "))

if EsMultiplo(numero_1, numero_2):
    print("numero 1 es multiplo de numero 2")
elif EsMultiplo(numero_2, numero_1):
    print("numero 2 es multiplo de numero 1")
else:
    print("No son multiplos uno del otro")

#Ejercicio 14
#Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima
#y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la
#temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el
#número de días que se van a introducir.
# tip 
# primero pedir cuantos dias
# hacer un bucle que pida los datos maxima y minima
#tenemos que tener la funcion que hace la media, (maxima + minima)/2
#ir mostrando el resultado

def media(maximo, minimo):
    return (maximo+minimo)/2

numero_dias = int(input("Introduce el numero de dias "))

for i in range(numero_dias):
    maxima = float(input("Introduce la temperatura maxima "))
    minima = float(input("Introduce la temperatura minima "))
    print(media("La media es:", maxima,minima))


#Ejercicio 15
#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
#cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú
#“. Crea un programa principal donde se use dicha función.
#tip: convertir el string en una lista con un bucle
# y una vez que tenga la lista la vuelvo a unir usando " ".join(lista)

def ConvertirEspaciado(texto):
    resultado = []

    for letra in texto:
        if letra != " ":
            resultado.append(letra)
            
    return " ".join(resultado)

entrada = "Hola, tú"
print(ConvertirEspaciado(entrada))



#Ejercicio 16
#Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y
#  devuelve el valor máximo y el mínimo. Crea un programa que pida números por 
# teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista):
    return max(lista),min(lista)


#Opcion B

def calcularMaxMin(lista):
    mayor = 0
    menor = 0

    for numero in lista:
        if numero >= mayor:
            mayor = numero
        if numero <= menor:
            menor = numero

    return mayor,menor

lista = []
numero = input("Introduce un numero (pon s para salir)")

while numero != "s":
    lista.append(float(numero))
    numero = input("Introduce un numero (pon s para salir)")

print(calcularMaxMin(lista))


#Ejercicio 18
#Crear una función llamada “Login”, que recibe un nombre de usuario y una contraseña 
#y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
# Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido 
# hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y 
# se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

def Login(usuario, contrasena, intentos):
    if ((usuario == "usuario1")and (contrasena == "asdasd")):
        return True
    else:
        intentos = intentos + 1
        return intentos

numero_intentos = 0

while numero_intentos < 3:
    usuario = input("Introduce nombre de usuario ")
    password = input("Introduce password ")

    retorno = Login(usuario,password,numero_intentos)

    if retorno == True:
        print("has acertado")
        break
    else:
        numero_intentos = retorno


#Opcion B
def Login(usuario:str, contrasena:str, intentos)->bool:
    if ((usuario == "usuario1")and (contrasena == "asdasd")):
        return True, intentos
    else:
        return False, intentos + 1

numero_intentos = 0
acertar = False

while numero_intentos < 3 and acertar != True:
    usuario = input("Introduce nombre de usuario ")
    password = input("Introduce password ")

    acertar,numero_intentos = Login(usuario,password,numero_intentos)

    
#Ejercicio 19
#Crear una función recursiva que permita calcular el factorial de un número. Realiza 
# un programa principal donde se lea un entero y se muestre el resultado del factorial.

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return factorial(numero - 1) * numero


print(factorial(5))

#Ejercicio 20
#Escribir dos funciones que permitan calcular:
#• La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#• La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#Escribe un programa principal con un menú donde se pueda elegir la opción de convertir 
# a segundos, convertir a horas, minutos y segundos o salir del programa.

def segundos(horas,minutos,segundos):
    total = 0
    total = total +(horas * 60 * 60)
    total = total + (minutos * 60)
    total = total + segundos

    return total

def cantidad_horas(segundos):
    horas = segundos // (60 * 60)
    segundos = segundos - (60 * 60 * horas)
    minutos = segundos // 60
    segundos = segundos % 60

    return horas,minutos,segundos

opcion = ""

while opcion!="s":
    print("1 - Convertir a horas")
    print("2 - Convertir segundos")
    print("s - Salir")

    opcion = input(" ")
    if opcion == "1":
        horas = int(input("introduce las hroas "))
        minutos = int(input("introduce los minutos "))
        sgeundos = int(input("introduce kos egundos "))
        print(segundos(horas, minutos,sgeundos))

    elif opcion == "2":
        seg = input("Introduce segundos ")
        print(cantidad_horas(seg))
    elif opcion == "s":
        print("Adios ")
    else:
        print("opcion innvalida")

#Ejercicio 21
#El día juliano correspondiente a una fecha es un número entero que indica los días que 
# han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa 
# principal que al introducir una fecha nos diga el día juliano que corresponde. 
# Para ello podemos hacer las siguientes subrutinas:
#• LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#• DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#• EsBisiesto: Recibe un año y nos dice si es bisiesto.
#• Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.

def LeerFecha():
    dia = input("Introduce el dia ")
    while not dia.isnumeric() and (1 <= dia <= 31):
        dia = input("Introduce el dia ")
    else:
        dia = int(dia)

    mes = leerDato("Introduce el mes ",1,12)
    ano = leerDato("Introduce el año ",-5000,5000)
    return dia,mes,ano


def DiasDelMes(mes, ano):
    if mes == 2:
        if EsBisiesto(ano)==True:
            return 29
        else:
            return 28
    elif(mes in (1,3,5,7,9,12)):
        return 31
    else:
        return 30

def EsBisiesto(ano):
    if (ano % 4 == 0) or ((ano % 100 ==0) and (ano % 400 == 0)):
        return True
    else:
        return False

def Calcular_Dia_Juliano(dia,mes,ano):
    dias = 0
    for i in range(1,mes):
        dias = dias + DiasDelMes(i,ano)
    else:
        dias = dias + dia
    
    return dias


def leerDato(mensaje,inferior, superior):
    dato = input(mensaje)
    while not dato.isnumeric() and (inferior <= dato <= superior):
        dato = input("Introduce el dia ")
    else:
        dato = int(dia)
    return dato


dia, mes, ano = LeerFecha()
print(Calcular_Dia_Juliano(dia,mes,ano))

# Ejercicio 22
# Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción, vamos a utilizar dos enteros: numerador y denominador.
# Vamos a crear las siguientes funciones para trabajar con fracciones:
# • Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. 
# Cuando leas una fracción, debes simplificarla.
# • Escribir_fracción: Esta función escribe en pantalla la fracción. Si el denominador es 1, se 
# muestra sólo el numerador.
# • Calcular_mcd: Esta función recibe dos números y devuelve el máximo común divisor.
# • Simplificar_fracción: Esta función simplifica la fracción. Para ello, hay que dividir
# numerador y denominador por el MCD del numerador y denominador.
# • Sumar_fracciones: Función que recibe dos fracciones n1/d1 y n2/d2, y calcula la suma 
# de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador = n1 * d2 + d1 * n2 y denominador = d1 * d2. Se debe simplificar la fracción resultado.
# • Restar_fracciones: Función que resta dos fracciones: numerador = n1 * d2 - d1 * n2 y 
# denominador = d1 * d2. Se debe simplificar la fracción resultado.
# • Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, 
# para ello numerador = n1 * n2 y denominador = d1 * d2. Se debe simplificar la fracción resultado.
# • Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, 
# para ello numerador = n1 * d2 y denominador = d1 * n2. Se debe simplificar la fracción resultado.
# Crear un programa que, utilizando las funciones anteriores, muestre el siguiente menú:
# • Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
# • Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
# • Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el producto.
# • Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra el cociente.
# • Salir

#Para mi una fraccion va a ser una tupla de valores, donde el primer valor es el numerador y el segundo el denominador
#(NUMERADOR, DENOMINADOR)

def Leer_fraccion():
    numerador = int(input("Introduce el numerador "))
    denominador = int(input("Introduce el denominador "))

    return Simplificar_fraccion(numerador,denominador)

def Escribir_fraccion(fraccion):
    print("La fraccion es:")
    numerador, denominador = fraccion
    if numerador == 1:
        print(denominador)
    else:
        print(numerador,"/",denominador)

def Calcular_mcd(numero_1, numero_2):
    mayor, menor = max(numero_1,numero_2), min(numero_1,numero_2)
    
    while (mayor % menor != 0):
            mayor, menor = menor, mayor % menor
    else:
        return menor

def Simplificar_fraccion(fraccion):
    numerador, denominador = fraccion
    maximo_comun_divisor = Calcular_mcd(numerador, denominador)
    
    numerador_simplificado = numerador // maximo_comun_divisor
    denominador_simplificado = denominador // maximo_comun_divisor

    return (numerador_simplificado, denominador_simplificado)


def Sumar_fracciones(fraccion_1, fraccion_2):
    #pass
    #numerador=n1*d2+d1*n2 y denominador=d1*d2
    n1,d1 = fraccion_1
    n2, d2 = fraccion_2

    numerador = (n1 * d2) + (d1 * n2)
    denominador=d1*d2

    return Simplificar_fraccion((numerador,denominador))

def Restar_fracciones(fraccion_1, fracciones_2):
    n1,d1 = fraccion_1
    n2, d2 = fraccion_2
    #numerador=n1*d2-d1*n2 y 
    # denominador=d1*d2
    numerador=n1*d2-d1*n2
    denominador=d1*d2

    return Simplificar_fraccion((numerador,denominador))

def Multiplicar_fracciones(fraccion_1, fracciones_2):
    n1,d1 = fraccion_1
    n2, d2 = fraccion_2
    
    numerador=n1*n2  
    denominador=d1*d2

    return Simplificar_fraccion((numerador,denominador))

def Dividir_fracciones(fraccion_1, fracciones_2):
    n1,d1 = fraccion_1
    n2, d2 = fraccion_2
    
    numerador=n1*d2 
    denominador=d1*n2

    return Simplificar_fraccion((numerador,denominador))