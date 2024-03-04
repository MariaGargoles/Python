import random

class Jugador:
    @staticmethod
    def pintar_palabra(huecos):
    # Muestra en la pantalla la palabra con espacios en blanco
        
        print(" ".join(huecos))

    @staticmethod
    def introducir_letra(palabra_a_adivinar, huecos, errores):
    
    # Permite al jugador introducir una letra y actualiza la lista de huecos y el contador de errores
        letra_introducida = input("Introduce tu letra: ")
        
        posicion = palabra_a_adivinar.find(letra_introducida)
        
        if posicion == -1:
            print("Lo siento no está la letra ¯\_◉‿◉_/¯")
            errores += 1
        else:
            
            for i, letra in enumerate(palabra_a_adivinar):
                
                if letra == letra_introducida:
                    huecos[i] = letra
        return huecos, errores

    @staticmethod
    def seleccionar_palabra(lista_palabras):
    # Devuelve una palabra aleatoria de la lista de palabras
       
        return random.choice(lista_palabras)