
from tablero import Tablero
from jugador import Jugador

class Ahorcado:
    @staticmethod
    def jugar():
        """
        Método para controlar el juego
        Parámetros de entrada:
            - Ninguno
        Salida:
            - Ninguno
        """
        palabras = ["ama", "casa", "pata", "leon", "roto"]
        palabra_a_adivinar = Jugador.seleccionar_palabra(palabras)
        huecos = ["_" for _ in palabra_a_adivinar]
        errores = 0

        Tablero.dibujar_muneco(errores)

        while "_" in huecos and errores < 6:
            Jugador.pintar_palabra(huecos)
            huecos, errores = Jugador.introducir_letra(palabra_a_adivinar, huecos, errores)
            Tablero.dibujar_muneco(errores)

        if errores == 6:
            print("Has perdido")
        else:
            print("¡Felicidades, has ganado!")


if __name__ == "__main__":
    Ahorcado.jugar()


