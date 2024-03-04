import random

#Para simplificar hemos añadido  las constantes de usuario
PLAYER_X = "X"
PLAYER_0 = "0"

#Esta funcion pinta el tablero
def display_board(board):
    for row in board:
        
        print("|".join(row))
        print("-*-*-")

#Esta funcion es para introducir nuestro movimiento
#TODO cambiar el tablero y los datos que se introducen por numeros de casillas en lugar de coordenadas
#TODO arreglar que cuando se introducen coordenadas incorrectas se pierda turno
               
def enter_move(board):
    while True:
        x = int(input("Introduce la coordenada x: "))
        y = int(input("Introduce la coordenada y: "))

        if 0 <= x <= 2 and 0 <= y <= 2 and board[x][y] == " ":
            board[x][y] = PLAYER_X
            break
        else:
            print("Coordenadas inválidas. Introduce valores válidos.")

#Esta funcion hace una lista de los espacios en blanco 
#TODO tenemos que añadir que si mete cualquier dato que no sea numerico lo vuelva pedir
            
def make_list_of_free_fields(board):
    return [(fila, columna) for fila in range(3) for columna in range(3) if board[fila][columna] == " "]


#Esta funcion determina la victoria comprobando si hay tres dibujos iguales 

def victory_for(board, sign):
    for i in range(3):
        #Horizontales y verticales
        if (
            board[i][0] == board[i][1] == board[i][2] == sign or
            board[0][i] == board[1][i] == board[2][i] == sign
        ):
            return True
        #Las diagonales

    if (
        board[0][0] == board[1][1] == board[2][2] == sign or
        board[0][2] == board[1][1] == board[2][0] == sign
    ):
        return True

    return False

def draw_move(board):
    casillas_libres = make_list_of_free_fields(board)
    
        # Verificar si la máquina puede ganar en el próximo movimiento
    
    for x, y in casillas_libres:
        # Simula el movimiento y verifica si la máquina gana
        
        board[x][y] = PLAYER_0
        if victory_for(board, PLAYER_0):
            return
        board[x][y] = " "  

        # Deshacer el movimiento si no gana
        # Reutilizamos la funcion de ganar para que la maquina intente bloquear los movimientos del jugador
        # Verificar si el jugador puede ganar en el próximo movimiento y bloquear

    for x, y in casillas_libres:
        # Simula el movimiento del jugador y verifica si va a ganar
        
        board[x][y] = PLAYER_X
        if victory_for(board, PLAYER_X):
            board[x][y] = PLAYER_0  
            
            # Bloquea al jugador
            
            return
        board[x][y] = " "  
        
        # Deshacer el movimiento si no va a ganar

    # Si la maquina no necesita bloquear, realiza un movimiento aleatorio
    if casillas_libres:
        x, y = random.choice(casillas_libres)
        board[x][y] = PLAYER_0


def jugar():
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    display_board(tablero)
    print("¡Vamos a jugar al 3 en raya!")

    while True:
        casillas_libres = make_list_of_free_fields(tablero)
        if not casillas_libres:
            print("Empate. No quedan mas jugadas")
            break

        enter_move(tablero)
        display_board(tablero)

        if victory_for(tablero, PLAYER_X):
            print("¡Ha ganado el jugadorx!")
            break
            
            #Este print lo usamos para separar y verificar que la maquina hace su movimiento
            #TODO hay que mejorar la visualizacion del tablero para eliminar este print
        
        print("******* Maquina jugando ******")

        casillas_libres = make_list_of_free_fields(tablero)
        if not casillas_libres:
            print("No quedan más jugadas - caput!")
            break

        draw_move(tablero)
        display_board(tablero)

        if victory_for(tablero, PLAYER_0):
            print("¡Ha ganado la máquina!")
            break

    

# Llamada para iniciar el juego
jugar()
