# Importar los módulos de validación de contraseñas y de nombres de usuario
import contrasenas as c
import usuarios as u

# Función para solicitar una entrada al usuario
def solicitar(mensaje):
    return input(mensaje)

# Función para validar un nombre de usuario y contraseña
def validacion():
    # Solicitar al usuario que ingrese un nombre de usuario y una contraseña
    usuario = solicitar("Introduce un nombre de usuario: ")
    password = solicitar("Introduce un password: ")

    # Verificar si la contraseña cumple con los criterios de aceptación
    # y si el nombre de usuario es válido utilizando los módulos previamente importados
    if c.condicion(password) and u.valido(usuario):
        print("Todo OK")
        return True  # Devolver True si ambos son válidos
    else:
        print("Error al introducir")
        return False  # Devolver False si al menos uno de ellos es inválido
