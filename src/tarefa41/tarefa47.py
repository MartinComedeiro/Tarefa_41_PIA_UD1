def calcularPrecio(inmueble):
    precio = (inmueble["metros"] * 1000 + inmueble["habitacións"] * 5000 + (15000 if inmueble["garaxe"] == True else 0)) * (1 - (2026 - inmueble["ano"])/100) * (1 if inmueble["zona"] == "A" else 1.5) 
    return precio


def comprar(lista, precioMax):
    listaComprar = [dict(inmueble, prezo = calcularPrecio(inmueble)) for inmueble in lista if calcularPrecio(inmueble)<= precioMax]
    return listaComprar

if __name__ == "__main__":
    lista = [
        {'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe':  True, 'zona': 'A'},
        {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe':  True, 'zona': 'B'},
        {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe':  False, 'zona': 'A'},
        {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe':  True, 'zona': 'B'},
        {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe':  False, 'zona': 'A'}
    ]
    print(comprar(lista, 100000))