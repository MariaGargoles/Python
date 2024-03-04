from mi_modulo import saludar as saludar_modulo

#Ejemplo de colision pilla el ultimo
def saludar():
    print("hola 2")

#aqui solo hemos importado saludar, nada mas
# es para el uso con el from import invocamos el elemento como si no estuviera dentro del modulo
saludar_modulo()