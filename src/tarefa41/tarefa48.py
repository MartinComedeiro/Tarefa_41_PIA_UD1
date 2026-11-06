def calcularWin(lista):
    
    for row in lista:
        if(row.count("X") == 3 or row.count("O") == 3):
            return True

    for num in range(0, len(lista[0])):
        if((lista[0][num] == lista[1][num] == lista[2][num]) and (lista[0][num] == "X" or lista[0][num] == "O")):
            return True

    if ((lista[0][0] == lista[1][1] == lista[2][2]) or (lista[0][2] == lista[1][1] == lista[2][0])) and (lista[1][1] == "X" or lista[1][1] == "O"):
        return True
     
    
    return False

def jugar(lista):

    while True:
        fila1 = int(input("Jugador 1 dime una fila (1-3)"))
        columna1 = int(input("Jugador 1 dime una columna (1-3)"))
        fila2 = int(input("Jugador 2 dime una fila (1-3)"))
        columna2 = int(input("Jugador 2 dime una columna (1-3)"))
        lista[fila1-1][columna1-1] = "X"
        lista[fila2-1][columna2-1] = "O"
        print(lista)

        if calcularWin(lista):
            print("Tenemos un ganador!")
            break

if __name__ == "__main__":
    lista = [
        [".",".","."],
        [".",".","."],
        [".",".","."]
    ]
    print(jugar(lista))