# Módulo de Validación de Nombres de Usuario

#Este módulo cumple con los siguientes criterios de aceptación:

#- El nombre de usuario debe tener entre 6 y 12 caracteres.
#- El nombre de usuario debe ser alfanumérico.
#- Si el nombre de usuario tiene menos de 6 caracteres, devuelve "El nombre de usuario debe contener al menos 6 caracteres".
#- Si el nombre de usuario tiene más de 12 caracteres, devuelve "El nombre de usuario no puede contener más de 12 caracteres".
#- Si el nombre de usuario contiene caracteres no alfanuméricos, devuelve "El nombre de usuario puede contener solo letras y números".
#- Si el nombre de usuario es válido, devuelve True.


def longitud(nombre, minimo, maximo):
    
    if len(nombre) > maximo:
        return "El nombre de usuario no puede contener más de " + str(maximo) + " caracteres"
    elif len(nombre) < minimo:
        return "El nombre de usuario debe contener al menos " + str(minimo) + " caracteres"
    else:
        return True
    
    #Función para verificar la longitud del nombre de usuario.
    #Parameters:
    #nombre (str): El nombre de usuario a verificar.
    #minimo (int): Longitud mínima permitida para el nombre de usuario.
    #maximo (int): Longitud máxima permitida para el nombre de usuario.
    
    #Returns:
    #str or bool: Mensaje de error si la longitud no está dentro del rango especificado, 
    #o True si la longitud es válida.

def alfanumericos(nombre):
    
    if not nombre.isalnum():
        return "El nombre de usuario puede contener solo letras y números"
    else:
        return True
    
    #Función para verificar si el nombre de usuario contiene solo caracteres alfanuméricos.
    #Parameters:
    #nombre (str): El nombre de usuario a verificar.
    
    #Returns:
    #str or bool: Mensaje de error si el nombre contiene caracteres no alfanuméricos, 
    #o True si el nombre es válido.

def valido(nombre):
    
    
    # Verificar longitud del nombre
    lon = longitud(nombre, 6, 12)
    if lon == True:
        # Si la longitud es válida, verificar caracteres alfanuméricos
        alfa = alfanumericos(nombre)
        if alfa == True:
            # Si también es alfanumérico, el nombre es válido
            return True
        else:
            # Si no es alfanumérico, imprimir mensaje de error y devolver False
            print(alfa)
            return False
    else:
        # Si la longitud no es válida, imprimir mensaje de error y devolver False
        print(lon)
        return False
    #Función para validar el nombre de usuario según los criterios especificados.
    #Parameters:
    #nombre (str): El nombre de usuario a validar.
    
    #Returns:
    #bool: True si el nombre de usuario es válido, False si no lo es.