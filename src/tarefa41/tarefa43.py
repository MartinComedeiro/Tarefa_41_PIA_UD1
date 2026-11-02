def IVE(cantidad, ive = 21):
    return cantidad *((100-ive)*0.01)

def IVE4(cantidad, ive = 4):
    return cantidad *((100-ive)*0.01)

def descuento(cantidad, ive = 10):
    return cantidad *((100-ive)*0.01)

def ejecutarLista(lista):
    suma = 0
    sumaTotal = 0
    sumaIVE = 0
    sumaDescuento = 0

    for producto in lista:
        cantidad = producto["prezo_sen_ive"]
        sumaTotal += producto["prezo_sen_ive"]

        if producto["desconto"] != None:
            cantidad = producto["desconto"](cantidad)
            sumaDescuento += producto["prezo_sen_ive"] - cantidad

        cantidadDescuento = cantidad
        cantidad = producto["calcular_ive"](cantidad)
        sumaIVE += cantidadDescuento - cantidad

        suma += cantidad

    return [sumaTotal, suma, sumaDescuento, sumaIVE]


if __name__ == "__main__":
    lista = [
        {
        "produto": "Pan",
        "prezo_sen_ive": 1.20,
        "desconto": None, # Non ten desconto
        "calcular_ive": IVE4
        },
        {
        "produto": "Aceite de oliva",
        "prezo_sen_ive": 8.50,
        "desconto": descuento, # Aplica un 10%
        "calcular_ive": IVE
        },
        {
        "produto": "Deterxente",
        "prezo_sen_ive": 6.00,
        "desconto": descuento,
        "calcular_ive": IVE
        },
        {
        "produto": "Leite",
        "prezo_sen_ive": 0.95,
        "desconto": None,
        "calcular_ive": IVE4
        }
    ]

    resultado = ejecutarLista(lista)
    print(resultado)
