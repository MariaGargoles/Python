#Question 1
#Write a Python function student_data () which will print the id of a student (student_id). If the 
#user passes an argument student_name or student_class the function will print the student 
#name and class. 

def student_data(student, student_name=None, student_class=None):
    print(id(student)) # aqui debemos imprimir el resultado del id, del objeto que recibe
    if student_name != None:    
        print(student.__name__) #tenemos un metodo magico que es __name__
    if student_class != None:
        print(type(student)) #se hace con la funcion type(objeto)

class Student:
    pass

estudiante = Student()
student_data(estudiante, True,True)

#Question 2
#Write a simple Python class named Student and display its type. Also, display the __dict__ 
#attribute keys and the value of the __module__ attribute of the Student class. 
class Student():
    pass

print(type(Student))
print(Student.__dict__)
print(Student.__module__)

#Question 3
#Write a Python program to crate two empty classes, Student and Marks. Now create some 
#instances and check whether they are instances of the said classes or not. Also, check whether 
#the said classes are subclasses of the built-in object class or not. 
class Student:
    pass

class Marks:
    pass

estudiante_1 = Student()
estudiante_2 = Student()

notas_1 = Marks()
notas_2 = Marks()

print(isinstance(estudiante_1, Student))
print(isinstance(estudiante_2, Student))

print(isinstance(notas_1, Marks))
print(isinstance(notas_2, Marks))

print(isinstance(notas_1, Student))

#Todos los objetos en Python igual que en Java y en otros POO, heredan de un objeto generico llamado object
print(issubclass(Student, object))
print(issubclass(Marks, object))

print(issubclass(Student, Marks))

#Question 4
#Write a Python class named Student with two attributes student_name, marks. Modify the 
#attribute values of the said class and print the original and modified values of the said 
#attributes. 
class Student():
    def __init__(self, nombre, notas):
        self.student_name = nombre
        self.marks = notas

estudiante = Student("Esteban",10)
print(estudiante.student_name,estudiante.marks)

estudiante.student_name = "James"
estudiante.marks = 0
print(estudiante.student_name,estudiante.marks)

#Question 5
#Write a Python class named Student with two attributes student_id, student_name. Add a new 
#attribute student_class and display the entire attribute and their values of the said class. Now 
#remove the student_name attribute and display the entire attribute with values. 
class Student():
   student_name = ""
   student_id = ""

Student.student_class = ""

print(Student.__dict__)

del Student.student_name

prinnt(Student.__dict__)

#Question 6
#Write a Python class named Student with two attributes student_id, student_name. Add a new 
#attribute student_class. Create a function to display the entire attribute and their values in 
#Student class. 
class Student():
    student_name = ""
    student_id = ""
    student_class = ""

    def __str__(self):
        return "Nombre " + self.student_name + " Id " + self.student_id + " Clase " + self.student_class

estudiante = Student()
print(estudiante)

#Question 7
#Write a Python class named Student with two instances student1, student2 and assign given 
#values to the said instances attributes. Print all the attributes of student1, student2 instances 
#with their values in the given format
class Student():
    def __init__(self, nombre, notas):
        self.student_name = nombre
        self.marks = notas

student1 = Student("James",10)
student2 = Student("Jane",9)

print(student1.__dict__)
print(student1.__dir__())

print(student2.__dict__)
print(student2.__dir__())

#Question 8
#Write a Python class to convert an integer to a roman numeral. 
roseta = {
    "I":1,
    "IV":4,
    "V":5,
    "X":10,
    "XL":40,
    "L":50,
    "XC":90,
    "C":100,
    "CD":400,
    "D":500,
    "CM":900,
    "M":1000
}
#2024 a Numero romano
#Primero buscamos el valor mas alto que le podemos restar sin quedarnos en negativo
# 2024 - 1000 = 1024 Salida = M
#Es cero?, si es cero acabamos y sino seguimos restando
# 1024 - 1000 = 24 Salida = MM
#Es cero?, si es cero acabamos y sino seguimos restando
# 24 - 10 = 14 Salida = MMX
#Es cero?, si es cero acabamos y sino seguimos restando
# 14 - 10 = 4 Salida = MMXX
#Es cero?, si es cero acabamos y sino seguimos restando
# 4 - 4 = 0 Salida = MMXXIV
#Numero == 0? si acabamos la salida
# Salida = MMXXIV
class Conversor():
    roseta = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }
    def Ordenar(self):
          
        diccionario_ordenado = {}
        for claves in sorted(self.roseta.keys(),reverse=True):
            diccionario_ordenado[claves] = self.roseta[claves]           
        return(diccionario_ordenado)

    #TODO 5 minutos para convertir el codigo de Ordenar en una diccionario de comprension
    def Ordenar_2(self):
        return {clave:self.roseta[clave] for clave in sorted(self.roseta.keys(),reverse=True)}

    def enteroARomano(self, entero):
        resultado = ""
        while entero > 0:
            for valor_del_simbolo, simbolo in self.Ordenar().items():
                while entero >= valor_del_simbolo:
                    resultado = resultado + simbolo
                    entero = entero - valor_del_simbolo
        return resultado

conversor = Conversor()
print(conversor.enteroARomano(2024))

#Question 9
#Write a Python class to convert a roman numeral to an integer. 
#Tenemos MMCCX convertirlo a entero
# Cogemos letra a letra
# MMCCX => M  Salida = 1000
#Cadena vacia?, em equedan letras si quedan seguimos
# MCCX => M  salida = 1000 + 1000 = 2000
#Cadena vacia?, em equedan letras si quedan seguimos
#CCX => C salida = 2000 + 100 = 2100
#Cadena vacia?, em equedan letras si quedan seguimos
#CX => C salida = 2100 + 100 = 2200
#Cadena vacia?, em equedan letras si quedan seguimos
# X => X salida = 2200 + 10 = 2210
#La cadena es vacia acabamos
#Aqui ojo porque puede darse un caso especial
# XXIV
#La primera parte es igual
# XX => salida = 20
# IV => aqui hay que mirar si el anterior simbolo es menor que el siguienye
#una opcin es coger e nuemro mas grande V y restarle el anterior I = 5-1 = 4
class Conversor():
    roseta = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    def RomanoAEntero(self, romano):
        resultado = 0
        anterior = 0

        for letra in romano:
            valor = self.roseta[letra]
            if anterior <valor:
                resultado = resultado - (2*anterior) +  valor
            else:
                resultado = resultado + valor
            anterior = valor

        return resultado

# IV 
#Primera vuelta
# resultado = 1
# anterior = 1
#Segunda vuelta
# valor = 5, anterior = 1
# 1 < 5 , anterior < valor
# rsultado = 1 - 2 + 5 = 4

#Question 10
#Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These 
#brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", 
#"({[)]" and "{{{" are invalid

#Concepto de pila LIFO => Last In First Out (El ultimo en entrar el primero en salir)
# [()] => apilarlos
# voy apilando los de apertura [, (, {
#paso 1
#pila = [
#paso 2
#pila = [(
#Y cuando encuentro uno de cierre lo desapilo y comparo
#elultmo en entrar en la pila fue el del paso 2 (
# ahora tenemos el cierre ) es la pareja de (? si coinciden lo quitamos y seguimos
#paso 3
#pila = [
#tenemos otro cierre ], 
#este ] es la parecja de esta paertura que tengo en la pila [
#si coninden todo OK
#y si la pila esta vacia y no quedan mas caracteres es OK
#[[))]]
# pila = [[
#encuentro un cierre que es )
#comparamors el ) es la pareja de [? NO 
#Error cadena invalida no hace falta seguir probando
#En python podeis crear una pila facilmente con una lista donde inserteis conappend siempre al final
#y para despailar recupereis el ultimo elemento, y para ello acordaros de que poeis usar el indice
#[-1] que apunta al ultimo elemento

class Pila():

    def __init__(self):
        self.pila = []

    def apilar(self, valor):
        self.pila.append(valor)

    def desapilar(self):
        valor = self.pila[-1]
        del self.pila[-1]
        return valor


comprobar = "[()]"
cierres = {
    ")":"(",
    "}":"{",
    "]":"["
    }

pila = Pila():

for elemento in comprobar:
    if elemento in cierres.keys():
        ultimo_valor = pila.desapilar()
        if ultimo_valor != cierres.get(elemento):
            print("Cadena erronea")
            break
    else:
        pila.apilar(elemento)
