#Renombrar Funciones o Elementos Importados en Python:
#Cuando estás importando elementos de un módulo, puedes asignarles un nuevo nombre localmente utilizando la sintaxis import ELEMENTO as NUEVO_NOMBRE 
#o from MODULO import ELEMENTO as NUEVO_NOMBRE. Esto es útil para evitar colisiones de nombres o para darles nombres más cortos o descriptivos en tu código.
#Ejemplo:


# Renombrar la función 'saludar' del módulo 'mi_modulo' a 'saludar_modulo'
from Modulos_Paquetes.Paquetes import saludar as saludar_modulo

# Definir una función 'saludar' en el programa principal
def saludar():
    print("¡Hola, función del programa principal!")

# Ahora podemos usar ambas funciones sin colisiones de nombres
saludar_modulo()  # Llama a la función del módulo
saludar()         # Llama a la función del programa principal

#En este ejemplo, la función saludar en el programa principal y la función saludar importada del módulo mi_modulo no entran en conflicto gracias al uso de nombres distintos. 