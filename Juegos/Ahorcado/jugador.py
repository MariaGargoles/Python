import random

class Jugador:
    @staticmethod
    def pintar_palabra(huecos):
        """
        Método para pintar la palabra y los huecos restantes
        Parámetros de entrada:
            - Huecos: lista con los huecos de la palabra
        """
        print(" ".join(huecos))

    @staticmethod
    def introducir_letra(palabra_a_adivinar, huecos, errores):
        """
        Método para introducir una letra y verificar si está en la palabra
        Parámetros de entrada:
            - Palabra_a_adivinar: palabra que se debe adivinar
            - Huecos: lista con los huecos de la palabra
            - Errores: número de errores
        Salida:
            - Huecos: lista modificada con los huecos
            - Errores: número actualizado de errores
        """
        letra_introducida = input("Introduce tu letra")
        posicion = palabra_a_adivinar.find(letra_introducida)
        if posicion == -1:
            print("Lo siento no está la letra")
            errores += 1
        else:
            for i, letra in enumerate(palabra_a_adivinar):
                if letra == letra_introducida:
                    huecos[i] = letra
        return huecos, errores

    @staticmethod
    def seleccionar_palabra(lista_palabras):
        """
        Método que recibe una lista de palabras y devuelve una aleatoria
        Parámetros de entrada:
            - Lista_palabras: Lista de palabras
        Salida:
            - Palabra seleccionada al azar
        """
        return random.choice(lista_palabras)