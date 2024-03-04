#Uso de un Paquete en Python:
#Para utilizar un paquete en Python, necesitas seguir algunos pasos específicos. Vamos a ver cómo importar un paquete y acceder a sus elementos internos.

    #Importar el Paquete:
    #Utilizamos la sentencia import seguida del nombre del paquete.

   

import mi_primer_paquete

#Esto carga el paquete y ejecuta el código de inicialización si hay un archivo __init__.py.
#Acceder a los Elementos Internos:
#Puedes acceder a los módulos, funciones, variables, etc., dentro del paquete utilizando la notación de punto.


mi_primer_paquete.modulo_1.saludar()  # Llama a la función saludar del modulo_1
print(mi_primer_paquete.modulo_2.variable)  # Imprime la variable del modulo_2

#Documentación del Paquete:
#La cadena de documentación (docstring) del paquete se puede acceder utilizando .__doc__.



    print(mi_primer_paquete.__doc__)

#Esto imprimirá la documentación que hayas agregado en el archivo __init__.py.
#Ejemplo Completo:
#Supongamos que el paquete está organizado como se describió anteriormente.


# Estructura del paquete
# mi_primer_paquete/
# ├── __init__.py
# ├── modulo_1.py
# └── modulo_2.py


# Contenido de __init__.py
"""
Este es mi primer paquete
"""


# Contenido de modulo_1.py
def saludar():
    print("Hola")


# Contenido de modulo_2.py
variable = 1000


# Uso del paquete
import mi_primer_paquete

mi_primer_paquete.modulo_1.saludar()  # Imprime: Hola
print(mi_primer_paquete.modulo_2.variable)  # Imprime: 1000
print(mi_primer_paquete.__doc__)  # Imprime la documentación del paquete

#Con estos pasos, puedes importar y utilizar paquetes en Python, facilitando la organización y reutilización de tu código.