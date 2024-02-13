def main():
    # Solicitar al usuario que ingrese la lista de números separados por espacios
    numeros = input("Ingresa una lista de números separados por espacios: ")

    # Convertir la entrada del usuario en una lista de números enteros
    numeros_enteros = [int(x) for x in numeros.split()]

    # Calcular la suma de los números
    suma = sum(numeros_enteros)

    # Imprimir la suma
    print("La suma de los números ingresados es:", suma)

if __name__ == "__main__":
    main()