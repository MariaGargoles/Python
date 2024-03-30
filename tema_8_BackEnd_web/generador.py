
#Crea un script llamado generador.py que cumpla las siguientes necesidades:
#• Debe incluir una función llamada leer_numero(). 
#Esta función tomará 3 valores: ini, fin y mensaje. 
#El objetivo es leer por pantalla un número >= que ini y <= que fin. 
#Además a la hora de hacer la lectura se mostrará en el input 
#el mensaje enviado a la función. Finalmente se devolverá el valor. Esta función 
#tiene que devolver un número, y tiene que repetirse hasta que el usuario no lo 
#escriba bien (lo que incluye cualquier valor que no sea un número del ini al fin).

import random
import math

#Función para leer un número entre ini y fin
def leer_numero(ini, fin, mensaje):
    # Leer el número del usuario
    numero = int(input(mensaje))
    # Repetir hasta que el usuario ingrese un número válido
    while not (ini <= numero <= fin):
        numero = int(input(mensaje))
    else:
        return numero

#Función para generar números y redondearlos
def generador():
    # Preguntar al usuario cuántos números desea generar
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    # Preguntar al usuario cómo desea redondear los números
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    # Lista para almacenar los números redondeados
    lista = []
    # Generar y redondear los números
    for i in range(numeros):
        aleatorio = random.uniform(0, 100)  # Generar un número aleatorio entre 0 y 100
        if modo == 1:  # Redondear hacia abajo (al alza)
            redondeado = math.floor(aleatorio)
        elif modo == 2:  # Redondear hacia arriba (a la baja)
            redondeado = math.ceil(aleatorio)
        else:  # Redondear normalmente
            redondeado = round(aleatorio)
        # Mostrar el número generado y su versión redondeada
        print("El número es", aleatorio, "y redondeado", redondeado)
        # Agregar el número redondeado a la lista
        lista.append(redondeado)

    return lista

# Llamar a la función 
generador()

#Primer número (numeros): Este número representará la cantidad de números que el usuario desea generar. 
#Debe estar entre 1 y 20, ambos inclusive. 
#El programa mostrará el mensaje "¿Cuantos números quieres generar? [1-20]:" para solicitar al usuario que ingrese esta cantidad.

#Segundo número (modo): Este número representará el modo de redondeo deseado por el usuario. 
#Debe ser un número entre 1 y 3, ambos inclusive. 
#El programa mostrará el mensaje "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:" para que el usuario elija el modo de redondeo.

#Una vez que se conozcan la cantidad de números a generar y el modo de redondeo, el programa hará lo siguiente:
#Generará una lista de números aleatorios decimales entre 0 y 100. 
#La cantidad de números generados será la indicada por el usuario.
#Redondeará cada uno de esos números según el modo de redondeo seleccionado por el usuario.
#Para cada número, mostrará tanto el número generado originalmente como su versión redondeada.
#Y devolverá una lista con los números redondeados.

