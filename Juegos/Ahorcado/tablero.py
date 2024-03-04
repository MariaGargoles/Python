#Utilizaremos este objeto para pintar la clase tablero

class Tablero:
    @staticmethod
    def dibujar_muneco(errores):
        """
        Método para dibujar el muñeco
        Parámetros de entrada:
            - Errores: número de errores
        Salida:
            - Ninguna
        """
        posiciones_muneco = [
            '''
               +---+
               |   |
                   |
                   |
                   |
                   |
            =========
            ''',
            '''
               +---+
               |   |
               O   |
                   |
                   |
                   |
            =========
            ''',
            '''
               +---+
               |   |
               O   |
               |   |
                   |
                   |
            =========
            ''',
            '''
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
            =========
            ''',
            '''
               +---+
               |   |
               O   |
              /|\  |
                   |
                   |
            =========
            ''',
            '''
               +---+
               |   |
               O   |
              /|\  |
              /    |
                   |
            =========
            ''',
            '''
               +---+
               |   |
               O   |
              /|\  |
              / \  |
                   |
            =========
            ''',
        ]
        print(posiciones_muneco[errores])
