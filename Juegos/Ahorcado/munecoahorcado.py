#El objetivo es crear un juego del ahorcado en python
# se trata de adivinar una palabra antes de que el muñeco sea colgado
# Requisitos:
# lo haremos todo con objetos, debeis crear la estructura de objetos necesaria para el juego
# poder pasar una tupla de palabras a adivinar, de las cuales en cada partida se seleccionara una al azar
# esta tupa estara almacenada en un modulo aparte para que sea mas facil de configurar, el modulo se llamara palabras
# tendrmoes un interfaz donde el muñeco se ira colgando, tenemos como limite 8 oportunidades erroneas antes de que el muñeco se cuelgue
# asimismo en el interfaz pintaresmo tantas lineas _ _ _ _ como letras tenga la palabra a adivinar
# y a medida que el usuario adivina vamos descubriendolas _ A _ A
# permitiremos que el usuario repita letras, si la letra ya estaba introducida y desvelo letrs lo consideraemos un erro
muneco = = [
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
      / \ |
           |
    =========
    ''',
]