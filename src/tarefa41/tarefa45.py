def esPrimo(numero):

    primo = True
    mitad = numero//2

    for num in range(2, mitad+1):
        if((numero % num) == 0):
            primo = False
            break

    return primo

def listaPrimo(lista):
    listaPrimos = [esPrimo(num) for num in lista]
    return listaPrimos

if __name__ == "__main__":
    lista = [5, 4, 6, 8, 3]
    print(listaPrimo(lista))