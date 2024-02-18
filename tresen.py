import random

PLAYER_X = "X"
PLAYER_0 = "0"

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-*-*-*")

def enter_move(board):
    while True:
        x = int(input("Introduce la coordenada x: "))
        y = int(input("Introduce la coordenada y: "))

        if 0 <= x <= 2 and 0 <= y <= 2 and board[x][y] == " ":
            board[x][y] = PLAYER_X
            break
        else:
            print("Coordenadas inválidas. Introduce valores válidos.")

def make_list_of_free_fields(board):
    return [(fila, columna) for fila in range(3) for columna in range(3) if board[fila][columna] == " "]

def victory_for(board, sign):
    for i in range(3):
        if (
            board[i][0] == board[i][1] == board[i][2] == sign or
            board[0][i] == board[1][i] == board[2][i] == sign
        ):
            return True

    if (
        board[0][0] == board[1][1] == board[2][2] == sign or
        board[0][2] == board[1][1] == board[2][0] == sign
    ):
        return True

    return False

def draw_move(board):
    casillas_libres = make_list_of_free_fields(board)
    
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
            print("No quedan más jugadas - caput!")
            break

        enter_move(tablero)
        display_board(tablero)

        if victory_for(tablero, PLAYER_X):
            print("¡Ha ganado el humano!")
            break

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

    print("Alguien ha ganado")

# Llamada para iniciar el juego
jugar()
