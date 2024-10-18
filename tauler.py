"""
TABLERO
        -Modificar una parte para que en el centro no se impriman "|" y solo espacio.
"""
def line(): #Funció linea (+--------+--...)
    for _ in range(7):
        print("+---------", end="")
    print("+")

    
def create_board(rows, cols):#Funció que crear el tauler
    board = [] #Llista taula
    for row in range(rows):
        board.append([" " for _ in range(cols)])#Afegeix espais per columna
    return board#Retorna la llista


def print_board(board): #Imprimeix el tauler
    #for rom in board[0]: #Posar que en la primera y última fila faci un afegit de |
        #print("|", end="")
    for row in board:#Per cada fila en el tauler
        print("|", end="")#Imprimeix "|" i les va afegint en linea 
        for cell in row:#Per cada cel·la en la fila
            print(cell, end="|")#Afegeix la cel·la i acaba amb "|"
        print()#Imprimeix un espai de línea
        line()
        


def add_piece(board, row, col, piece):#Funció afegir nom
    board[row][col] = piece #Defineix la variable piece com un caracter en la taula

def add_text(text):
    pass    

def texto():
    text = "Hola"
    add_piece(board, 1, 1, f"{text:<9}")
    add_piece(board, 1, 2, f"{text:<9}")
    add_piece(board, 1, 3, f"{text:<9}")
    add_piece(board, 1, 4, f"{text:<9}")
    add_piece(board, 1, 5, f"{text:<9}")
    add_piece(board, 2, 1, f"{text:<9}")
    add_piece(board, 2, 2, f"{text:<9}")
    add_piece(board, 2, 3, f"{text:<9}")
    add_piece(board, 2, 4, f"{text:<9}")
    add_piece(board, 2, 5, f"{text:<9}")
    add_piece(board, 3, 1, f"{text:<9}")
    add_piece(board, 3, 2, f"{text:<9}")
    add_piece(board, 3, 3, f"{text:<9}")
    add_piece(board, 3, 4, f"{text:<9}")
    add_piece(board, 3, 5, f"{text:<9}")
    add_piece(board, 4, 1, f"{text:<9}")
    add_piece(board, 4, 2, f"{text:<9}")
    add_piece(board, 4, 3, f"{text:<9}")
    add_piece(board, 4, 4, f"{text:<9}")
    add_piece(board, 4, 5, f"{text:<9}")
    add_piece(board, 5, 1, f"{text:<9}")
    add_piece(board, 5, 2, f"{text:<9}")
    add_piece(board, 5, 3, f"{text:<9}")
    add_piece(board, 5, 4, f"{text:<9}")
    add_piece(board, 5, 5, f"{text:<9}")



def main():#Funció principal (main)
    global board
    rows = 7#Filas
    cols = 7#Columnas
    board = create_board(rows, cols)#Crida la funció crear tauler

    
    
    caselles = ["Parking","Urqinoa", "Fontan", "Sort", "Rambles", "Pl. Cat", "Anr pró", "Aragó", "S.Joan","Caixa","Aribau","Muntan","Angel","Augusta","Caixa","Balmes","Gracia","Presó","Consell","Marina","Sort","Rosell","Lauria","Sortida"]
    
    #Afegeix els noms de les caselles
    line()
    add_piece(board, 0, 0, f"{caselles[0]:<9}")
    add_piece(board, 0, 1, f"{caselles[1]:<9}")
    add_piece(board, 0, 2, f"{caselles[2]:<9}")
    add_piece(board, 0, 3, f"{caselles[3]:<9}")
    add_piece(board, 0, 4, f"{caselles[4]:<9}")
    add_piece(board, 0, 5, f"{caselles[5]:<9}")
    add_piece(board, 0, 6, f"{caselles[6]:<9}")
    add_piece(board, 1, 0, f"{caselles[7]:<9}")
    add_piece(board, 2, 0, f"{caselles[8]:<9}")
    add_piece(board, 3, 0, f"{caselles[9]:<9}")
    add_piece(board, 4, 0, f"{caselles[10]:<9}")
    add_piece(board, 5, 0, f"{caselles[11]:<9}")
    add_piece(board, 1, 6, f"{caselles[12]:<9}")
    add_piece(board, 2, 6, f"{caselles[13]:<9}")
    add_piece(board, 3, 6, f"{caselles[14]:<9}")
    add_piece(board, 4, 6, f"{caselles[15]:<9}")
    add_piece(board, 5, 6, f"{caselles[16]:<9}")
    add_piece(board, 6, 0, f"{caselles[17]:<9}")
    add_piece(board, 6, 1, f"{caselles[18]:<9}")
    add_piece(board, 6, 2, f"{caselles[19]:<9}")
    add_piece(board, 6, 3, f"{caselles[20]:<9}")
    add_piece(board, 6, 4, f"{caselles[21]:<9}")
    add_piece(board, 6, 5, f"{caselles[22]:<9}")
    add_piece(board, 6, 6, f"{caselles[23]:<9}")
    texto()
    print_board(board)

main()