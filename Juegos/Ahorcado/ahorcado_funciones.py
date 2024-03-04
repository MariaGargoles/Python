
#Primer paso entender el problema
#Dibujar el muñeco
#Tener una lista de palabras y seleccionar un para jugar
#Espacios para la palabra
#Intentos - introducir letra

# Esbozar un esqueleto de las funciones que necesitemos
import random

def dibujarMuneco(errores):
    """
        Funcion para dibujar el muñeco
            Parametros de entrada: 
                - Errores, numero de errores
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
      / \ |
           |
    =========
    ''',
] #PONER LISTA DE POSICONES MUÑECO
    print(posiciones_muneco[errores])

def seleccionarPalabra(lista_palabras):
    """
            Funcion que recibe una lista de palabras y devuelve una aleatoria
            Parametros de entradas:
                - Lista de palabras
            Salida:
                - Palabra seleccionada al azar
    """
    #el choice que tenemos dentro de random si le pasamos una lista de palabras nos devuele una palabra aleatr¡oria de dicha lista
    return random.choice(lista_palabras) 

def pintarPalabra(huecos):
    """
    Funcion para pintar la palabra y los huecos restantes
        - Parametros de entrada:
            - Palabra, que es la palabra a pintar con huecos
    """
    print(" ".join(huecos))

def introducirLetra(palabra_a_adivinar, huecos, errores):
    """
        Funcion para introducir una letra para ver si esta o no en la palabra
        Parametros de entrada:
            - Palabra: la palabra a adivinar
            - Huecos: los huecos pendientes de rellenar
        Salida:
            - Huecos: los huecos modificados en caso de que se haya acertado
    """
    letra_introducida = input("Introduce tu letra")
    posicion = palabra_a_adivinar.find(letra_introducida)
    if (posicion==-1):
        print("Lo siento no esta la letra")
        errores = errores  + 1
    else:
        posicion = 0
        for letra in palabra_a_adivinar:
            if (letra == letra_introducida):
                huecos[posicion] = letra
                
            posicion = posicion + 1
    return huecos, errores
    
   

def jugar():
    """
        Funcion para controla el juego
        Parametros de entrada:
            - Ninguno
        Parametros de salida:
            - Ninguno
    """
    palabras = ["ama","casa","pata","leon","roto"]
    palabra_a_adivinar = seleccionarPalabra(palabras)
    #genero tantos huecos como posiciones tiene la palabra
    huecos = ["_" for letra in palabra_a_adivinar]
    #La forma mas sencilla es plantearnos como parar la partica
    #no superar el numero maximo e errores o acertar la palabra
    #controlamos el numero de huecos que nos quedan vacios huecos.count("_")!=0
    # y para saber si superamos el numero de errores, creamos una variable errores para llevar la cuenta
    errores = 0
    pintarPalabra(huecos)
    dibujarMuneco(errores)

    while(huecos.count("_")!=0 and errores <6):      
        huecos, errores = introducirLetra(palabra_a_adivinar, huecos, errores)
        pintarPalabra(huecos)
        dibujarMuneco(errores)
    else:
        if(errores == 6):
            print("HAs perdido")
        else:
            print("Felicidades has ganado!!!")
 
jugar()
