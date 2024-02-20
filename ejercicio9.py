def crear_cesta_compra():
    cesta_compra = {}
    while True:
        articulo = input("Ingrese el nombre del artículo (o 'fin' para terminar): ")
        if articulo.lower() == 'fin':
            break
        precio = float(input("Ingrese el precio del artículo: "))
        cesta_compra[articulo] = precio
    return cesta_compra

def mostrar_cesta_compra(cesta_compra):
    print("\n--- Cesta de la Compra ---")
    total = 0
    for articulo, precio in cesta_compra.items():
        print("{:<15}: {:>10.2f}".format(articulo, precio))
        total += precio
    print("--------------------------")
    print("Total{:>21.2f}".format(total))

def main():
    print("Bienvenido a su cesta de la compra.")
    cesta_compra = crear_cesta_compra()
    mostrar_cesta_compra(cesta_compra)

if __name__ == "__main__":
    main()