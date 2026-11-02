def suma(numero):
    if numero<0:
        numero = -numero
    
    suma = 0
    for num in range(1, numero + 1):
        suma += num;
    return suma

if __name__ == "__main__":
    print("Dime un numero")
    numero = int(input())
    print(" ")

    numero = suma(numero)
    print(f"La suma es: {numero}")
