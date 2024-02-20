def calcular_precio_entrada(edad):
    if edad < 4:
        return 0
    elif 4 <= edad <= 18:
        return 30000
    else:
        return 50000

def main():
    try:
        edad = int(input("Ingrese la edad del cliente: "))
        if edad < 0:
            print("La edad no puede ser un número negativo.")
            return
        precio_entrada = calcular_precio_entrada(edad)
        if precio_entrada == 0:
            print("El cliente puede entrar gratis.")
        else:
            print("El precio de la entrada es:", precio_entrada)
    except ValueError:
        print("Por favor, ingrese una edad válida.")

if __name__ == "__main__":
    main()