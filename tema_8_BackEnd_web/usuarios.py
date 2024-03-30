#Ejercicio 1
#Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá cumplir con los 
#siguientes criterios de aceptación:
#• El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
#• El nombre de usuario debe ser alfanumérico.
#• Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de 
#usuario debe contener al menos 6 caracteres".
#• Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario 
#no puede contener más de 12 caracteres".
#• Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El 
#nombre de usuario puede contener solo letras y números".
#• Nombre de usuario válido, retorna True.

def longitud(nombre, minimo, maximo):
    if len(nombre) > maximo:
        return "El nombre de usuario no puede contener mas de " + str(maximo) + " caracteres"
    elif len(nombre) < minimo:
        return "El nombre de usuario debe contener al menos " + str(minimo) + " caracteres"
    else:
        return True

def alfanumericos(nombre):
    if not nombre.isalpha():
        return "El nombre de usuario puede contener solo letras y números"
    else:
        return True

def valido(nombre):
    lon = longitud(nombre,6,12)
    if lon == True:
        alfa = alfanumericos(nombre):
        if alfa == True:
            return True
        else:
            print(alfa)
            return False
    else:
        print(lon)
        return False