from math import pi

def areaCir(radio):
        return pi*(radio**2)

def volCil(radio, altura):
    return areaCir(radio)*altura

if __name__ == "__main__":
    print("Dime el radio de un circulo (m)")
    radio = int(input())
    print(" ")

    print("Dime la altura de un cilindro (m)")
    altura = int(input())
    print(" ")

    print(f"El area del circulo es: {areaCir(radio)}m")
    print(f"El volumen del cilindro es: {volCil(radio, altura)}m")
