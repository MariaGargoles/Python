# Ejercicio 1
class Persona():
    def __init__(self, nombre="", edad=0, DNI=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI

    def mostrar(self):
        print("Nombre:", self.__nombre, "Edad:", self.__edad, "DNI:", self.__DNI)

    def esMayorDeEdad(self):
        return self.__edad >= 18

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre == "":
            print("No puede ser vacío el nombre")
        else:
            self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa")

    @property
    def DNI(self):
        return self.__DNI

    @DNI.setter
    def DNI(self, DNI):
        if len(DNI) != 9:
            print("El DNI debe tener longitud 9")
        else:
            self.__DNI = DNI


# Ejercicio 2
class Cuenta():
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad

    def mostrar(self):
        print("El titular es", self.titular.nombre, "y el saldo es", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        if isinstance(titular, Persona):
            self._titular = titular
        else:
            print("Debe ser una persona")

    @property
    def cantidad(self):
        return self.__cantidad


# Ejercicio 3
class CuentaJoven(Cuenta):
    def __init__(self, titular, bonificacion, cantidad=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def esTitularValido(self):
        return 18 <= self.titular.edad < 25

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)

    def mostrar(self):
        print("Cuenta joven y la bonificación", self.bonificacion)
        super().mostrar()

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion


# Crear objetos
persona = Persona("Paco", 20, "123456789")
cuenta = Cuenta(persona, 90.1)
cuenta_joven = CuentaJoven(persona, 10, 50.0)

# Probando los métodos
persona.mostrar()
print("¿Es mayor de edad?", persona.esMayorDeEdad())

cuenta.mostrar()
cuenta.ingresar(20.0)
cuenta.retirar(10.0)
print("Saldo después de operaciones:", cuenta.cantidad)

cuenta_joven.mostrar()
cuenta_joven.ingresar(30.0)
cuenta_joven.retirar(15.0)
print("Saldo después de operaciones:", cuenta_joven.cantidad)
