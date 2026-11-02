def resta(cantidad, resta = 2):
    return (cantidad - resta)

def ejecutarLista(lista, funct):
    listaNueva = []

    for producto in lista:
        listaNueva.append(funct(producto))
        
    return listaNueva


if __name__ == "__main__":
    lista = [5, 4, 6, 8, 3]

    resultado = ejecutarLista(lista, resta)
    print(resultado)