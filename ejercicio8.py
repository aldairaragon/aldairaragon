def calcular_precio_final(fruta, cantidad, precios_frutas):
    """
    Calcula el precio final de una fruta dados su nombre y cantidad vendida.

    Parámetros:
        fruta (str): El nombre de la fruta.
        cantidad (int): La cantidad vendida.
        precios_frutas (dict): Diccionario que contiene los precios de las frutas.

    Retorna:
        float: El precio final de la fruta.
    """
    if fruta in precios_frutas:
        precio_unitario = precios_frutas[fruta]
        precio_final = precio_unitario * cantidad
        return precio_final
    else:
        print("Error: La fruta '{}' no está en el diccionario.".format(fruta))
        return None

def main():
    precios_frutas = {
        "manzana": 2.5,
        "banana": 1.8,
        "naranja": 3.0,
        "pera": 2.0
    }

    while True:
        fruta = input("Ingrese el nombre de la fruta: ").lower()
        cantidad = int(input("Ingrese la cantidad vendida: "))

        precio_final = calcular_precio_final(fruta, cantidad, precios_frutas)
        if precio_final is not None:
            print("El precio final de {} es: {}".format(fruta, precio_final))

        continuar = input("¿Desea hacer otra consulta? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()