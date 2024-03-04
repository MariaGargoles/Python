#La tercera forma de inportar algo es 
# la sintaxis from MODULO inport FUNCION/OBJETO/VARIABLE
# esto se usa cuando queremos importar una parte no todo
from mi_modulo import saludar
#OJO mala practica, importa todo, pero teneis peligro con las colisiones
from mi_modulo import *

#Ejemplo de colision pilla el ultimo
def saludar():
    print("hola 2")

#aqui solo hemos importado saludar, nada mas
# es para el uso con el from import invocamos el elemento como si no estuviera dentro del modulo
saludar()
