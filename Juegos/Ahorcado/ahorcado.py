
from tablero import Tablero
from jugador import Jugador

class Ahorcado:
    @staticmethod
    def jugar():
        
        #Creamos el diccionario con mas palabras , para crear variedad

        palabras = ["ama", "casa", "pata", "leon", "roto", "sol", "luna", "coche", "python", "montaña", "playa", "libro", "cuchara", "avión", "piano", "manzana", "azul", "feliz", "triste", "agua", "familia"]
        palabra_a_adivinar = Jugador.seleccionar_palabra(palabras)
        huecos = ["_" for _ in palabra_a_adivinar] #asi pintamos los huecos de las palabras
        errores = 0

        Tablero.dibujar_muneco(errores)

        #Este bucle controla la logica del juego 
        while "_" in huecos and errores < 6:
            Jugador.pintar_palabra(huecos)
            huecos, errores = Jugador.introducir_letra(palabra_a_adivinar, huecos, errores)
            Tablero.dibujar_muneco(errores)
        #Si se superan los 6 errores se acaba
        if errores == 6:
            print("Has muerto X.X")
        else:
            print("¡Felicidades! ↖(^▽^)↗")


if __name__ == "__main__":
    Ahorcado.jugar()


