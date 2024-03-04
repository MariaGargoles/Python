#Importar Partes Específicas de un Módulo en Python:
#Cuando solo necesitas utilizar una función, objeto o variable específica de un módulo en lugar de importar todo, puedes hacerlo utilizando la sintaxis from MODULO import ELEMENTO. 
#Esto es útil para evitar posibles colisiones de nombres y mejorar la eficiencia importando solo lo que necesitas.

#Ejemplo:

# Importar solo la función 'saludar' del módulo 'mi_modulo'
from Modulos_Paquetes.Paquetes import saludar

# Puedes usar la función directamente sin el nombre del módulo
saludar()

#En este caso, solo la función saludar se importa del módulo mi_modulo. 
#Ten en cuenta que, si hay otra función o variable con el mismo nombre en tu programa, no habrá conflictos
#ya que solo la función importada con la sentencia from ... import ... estará disponible en el espacio de nombres actual.

#Importar Todo de un Módulo (Desaconsejado):


# Importar todo del módulo (mala práctica, puede causar colisiones de nombres)
from Modulos_Paquetes.Paquetes import *

#Importante: Importar todo un módulo con el asterisco * no se recomienda, ya que puede causar colisiones de nombres y hacer que tu código sea menos legible. 
#Es preferible importar solo lo necesario para evitar posibles conflictos.
