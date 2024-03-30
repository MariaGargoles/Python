#Ejercicio 3
#Crear un módulo que solicite al usuario el ingreso de un nombre de usuario y contraseña y que 
#los valide utilizando los módulos generados en los dos ejercicios anteriores.

import contrasenas as c
import usuarios as u

def solicitar(mensaje):
    return (input(mensaje))

def validacion():
    usuario = solicitar("Introduce un nombre de usuario ")
    password = solicitar("Introduce un password ")

    if c.condicion(password) and u.valido(usuario):
        print("Todo OK")
        return True
    else:
        print("Error al introducir")
        return False
