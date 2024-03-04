#Importar Módulos con Alias en Python:
#En Python, al importar módulos, puedes asignarles alias para hacer más corto o legible su nombre en tu código. 
#Esto se logra utilizando la palabra clave as seguida del alias que deseas asignar al módulo.

#Ejemplo:


# Importar un módulo con alias
import mi_modulo as modulillo

# Ahora puedes acceder a las funciones y variables del módulo utilizando el alias
modulillo.saludar()

# Intentar acceder por el nombre original del módulo resultará en un error
mi_modulo.saludar()  # Esto generará un NameError

#Ventajas de Usar Alias:

#Legibilidad: Puedes asignar alias más cortos o descriptivos, mejorando la legibilidad del código.
#Evitar Conflictos: En situaciones donde podrían existir nombres de módulos similares, los alias ayudan a evitar conflictos.
#Importante: Al utilizar alias, asegúrate de usar el alias en lugar del nombre original del módulo al acceder a sus funciones y variables. 
#En el ejemplo proporcionado, el alias modulillo se usa en lugar del nombre original mi_modulo.