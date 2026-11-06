def esPar(numero):
    
    if((numero % 2) == 0):
        par = True
    else:
        par = False

    return par

def listaPar(lista):
    listaPares = [esPar(num) for num in lista]
    return listaPares

if __name__ == "__main__":
    lista = [5, 4, 6, 8, 3]
    print(listaPar(lista))