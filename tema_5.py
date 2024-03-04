
#Objetos en Python:
#En Python, los objetos son instancias de clases. Una clase es un plano o plantilla para crear objetos, 
#y un objeto es una instancia única de una clase. Aquí hay algunos conceptos clave:

#Declaración de Clase:


class MiObjeto():
    pass

#Puedes pensar en una clase como un molde para crear objetos. 
#Aquí, MiObjeto es la clase.


#Instanciación:

mi_objeto = MiObjeto()

#La instanciación crea un objeto a partir de la clase. Ahora, mi_objeto es una instancia de MiObjeto.

#Docstring:


class MiObjeto():
    """
    Ejemplo de documentación de nuestro objeto.
    """
    pass

#Puedes incluir una cadena de documentación (docstring) para describir tu clase.


#Atributos:


class MiObjeto():
    numero = 0

#Puedes definir atributos en la clase, y cada instancia de la clase tendrá esos atributos.
#Atributos de Clase e Instancia:


class Foo():
    numero = 0

foo_1 = Foo()
foo_2 = Foo()

Foo.numero = 2

print(foo_1.numero)  # Imprime 2
print(foo_2.numero)  # Imprime 2

#Los atributos de clase son compartidos por todas las instancias, mientras que los atributos de instancia son únicos para cada objeto.

#Métodos:

class MiObjeto():
    def mi_metodo(self):
        print("Mi método 1")

    def mi_metodo_2(self):
        print("Mi método 2")

#Los métodos son funciones definidas en una clase. Se accede a ellos a través de las instancias de la clase.

#Constructor (__init__):


class Alumno():
    def __init__(self, nombre, apellido=""):
        self.nombre = nombre
        self.apellido = apellido

#El método __init__ es el constructor y se llama automáticamente cuando se crea una nueva instancia de la clase.
#Métodos Mágicos (__str__):


class Foo():
    def __str__(self):
        return "Así es como quiero convertir a string"

#Los métodos mágicos son métodos especiales que Python utiliza en circunstancias específicas. __str__ se llama al intentar convertir un objeto a cadena.
#Privacidad de Atributos:


class Alumno():
    def __init__(self):
        self.__nombre = ""

#En Python, la privacidad se indica convencionalmente colocando dos guiones bajos (__) antes del nombre del atributo. Sin embargo, no es una característica de privacidad completa.
#Getter y Setter Alternativos:


class Alumno():
    def __init__(self):
        self.__nombre = ""

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

#Puedes utilizar decoradores como @property y @nombre.setter para crear getters y setters de una manera más pythonic.