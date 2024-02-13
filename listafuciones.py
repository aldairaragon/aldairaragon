def main():
    # Solicitar al usuario que ingrese la lista de enteros
    lista_enteros = input("Ingresa una lista de enteros separados por espacios: ")

    # Convertir la entrada del usuario en una lista de enteros
    lista_enteros = [int(x) for x in lista_enteros.split()]

    # Imprimir la lista de enteros
    print("La lista de enteros ingresada es:", lista_enteros)

if __name__ == "__main__":
    main()