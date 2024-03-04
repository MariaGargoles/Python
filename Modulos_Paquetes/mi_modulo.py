#Paquetes en Python:
#En Python, un paquete es una forma de organizar y estructurar módulos relacionados entre sí. 
#Un paquete se crea mediante la agrupación de varios módulos en un directorio y colocando un archivo especial llamado __init__.py en ese directorio. 
#Este archivo puede estar vacío o contener código de inicialización para el paquete.

#Estructura básica de un paquete:

#    Directorio del Paquete:
#        Creas un directorio que actuará como el paquete y le das un nombre significativo. Este directorio contendrá varios módulos.


#mi_primer_paquete/
#├── __init__.py
#├── modulo_1.py
#└── modulo_2.py

#__init__.py:
#Este archivo indica que el directorio debe considerarse un paquete de Python. Puede estar vacío o contener código de inicialización del paquete.


# En mi_primer_paquete/__init__.py
"""
Este es mi primer paquete
"""

#Módulos:
#Los módulos son archivos individuales que contienen funciones, variables, o cualquier código de Python. Puedes tener tantos módulos como desees en tu paquete.


    # En mi_primer_paquete/modulo_1.py
    def saludar():
        print("Hola")

    # En mi_primer_paquete/modulo_2.py
    variable = 1000

#Uso del Paquete:
#Una vez que has creado tu paquete, puedes importarlo y usar sus módulos en otros scripts o programas Python.

# En otro script o programa
from mi_primer_paquete import modulo_1, modulo_2

modulo_1.saludar()  # Imprime: Hola
print(modulo_2.variable)  # Imprime: 1000

#Ventajas de los Paquetes:
#Organización: Permite organizar y estructurar el código de una manera más modular y comprensible.
#Reusabilidad: Facilita la reutilización de código. Puedes utilizar tu paquete en varios proyectos sin tener que copiar y pegar el mismo código.
#Mantenimiento: Mejora el mantenimiento del código, ya que los cambios realizados en un paquete afectarán automáticamente a todos los lugares donde se utiliza.
#Colaboración: Facilita la colaboración en equipos de desarrollo, ya que diferentes desarrolladores pueden trabajar en diferentes módulos del paquete.

#Importante: el uso de __init__.py es opcional, pero es recomendable usarlo.
