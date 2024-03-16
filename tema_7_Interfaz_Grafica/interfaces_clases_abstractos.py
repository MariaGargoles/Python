#Las clases abstractas en Python permiten definir estructuras y comportamientos comunes que deben ser implementados por las clases concretas. 
#Esto se logra utilizando el módulo abc de la #biblioteca estándar de Python. Las clases abstractas no pueden ser instanciadas directamente, 
#sino que se utilizan como modelos o esquemas para otras clases que las heredan.
#Para crear una clase abstracta en Python, debemos hacer dos cosas:
#
#Hacer que la clase herede de ABC.
#Marcar los métodos que deben ser implementados en las subclases con el decorador @abstractmethod.
#A continuación, un ejemplo de cómo usar clases abstractas en Python:
#
#
#
#
#Un interfaz se puede definir como un contrato de obligado cumplimiento entre las partes
from abc import ABC
from abc import abstractmethod

#Debemos hacer 2 cosas, la primera hacer que herede de ABC
class Mando(ABC):
#Lo segundo debemos marcar las clases de obligada implementacion con el decorador @abstractmethod
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def subirVolumen(self):
        pass

    def otroMetodo(self):
        print("Otro metodo")

class MandoLG(Mando):
    def encender(self):
        print("Enciendde LG")
    
    def apagar(self):
        print("Apagar LG")
    
    def subirVolumen(self):
        print("Sube Volumen")

class MandoSony(Mando):
    def encender(self):
        print("Enciendde Sony")
    
    def apagar(self):
        print("Apagar Sony")
    
    def subirVolumen(self):
        print("Sube Volumen")

    def botonNetflix(self):
        print("Boton Netflix")

mando = MandoSony()

mando.apagar()
mando.encender()
mando.subirVolumen()

#En este ejemplo, Mando es una clase abstracta que define tres métodos abstractos: 
#encender, apagar y subirVolumen. Las subclases concretas MandoLG y MandoSony heredan de Mando y proporcionan implementaciones concretas para estos métodos.
#
#Al crear una instancia de MandoSony, podemos llamar a los métodos definidos en la clase base abstracta, y también a cualquier método adicional definido en las subclases. 
#Esto ilustra cómo las clases abstractas pueden definir un conjunto común de métodos y comportamientos que deben ser implementados por las subclases, permitiendo la extensión y modularidad del #código.