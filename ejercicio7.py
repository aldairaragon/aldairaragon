def añadir_numero(lista):
    numero = int(input("Ingrese un número para añadir a la lista: "))
    lista.append(numero)
    print("Número añadido a la lista.")

def añadir_numero_posicion(lista):
    numero = int(input("Ingrese un número para añadir a la lista: "))
    posicion = int(input("Ingrese la posición en la que desea insertar el número (empezando desde 1): "))
    if 1 <= posicion <= len(lista) + 1:
        lista.insert(posicion - 1, numero)
        print("Número añadido en la posición", posicion, "de la lista.")
    else:
        print("La posición especificada no es válida.")

def longitud_lista(lista):
    print("La longitud de la lista es:", len(lista))

def eliminar_ultimo_numero(lista):
    if lista:
        ultimo_numero = lista.pop()
        print("Se eliminó el último número de la lista:", ultimo_numero)
    else:
        print("La lista está vacía.")

def eliminar_numero_posicion(lista):
    posicion = int(input("Ingrese la posición del número que desea eliminar (empezando desde 1): "))
    if 1 <= posicion <= len(lista):
        numero_eliminado = lista.pop(posicion - 1)
        print("Se eliminó el número", numero_eliminado, "de la lista.")
    else:
        print("La posición especificada no es válida.")

def contar_numeros(lista):
    numero = int(input("Ingrese el número que desea contar en la lista: "))
    apariciones = lista.count(numero)
    print("El número", numero, "aparece", apariciones, "veces en la lista.")

def posiciones_numero(lista):
    numero = int(input("Ingrese el número del que desea conocer las posiciones en la lista: "))
    posiciones = [i + 1 for i, n in enumerate(lista) if n == numero]
    if posiciones:
        print("El número", numero, "aparece en las siguientes posiciones:", posiciones)
    else:
        print("El número", numero, "no está en la lista.")

def mostrar_numeros(lista):
    print("Los números en la lista son:", lista)

def menu():
    lista = []
    while True:
        print("\n--- Menú ---")
        print("1. Añadir número a la lista")
        print("2. Añadir número de la lista en una posición")
        print("3. Longitud de la lista")
        print("4. Eliminar el último número")
        print("5. Eliminar un número")
        print("6. Contar números")
        print("7. Posiciones de un número")
        print("8. Mostrar números")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            añadir_numero(lista)
        elif opcion == "2":
            añadir_numero_posicion(lista)
        elif opcion == "3":
            longitud_lista(lista)
        elif opcion == "4":
            eliminar_ultimo_numero(lista)
        elif opcion == "5":
            eliminar_numero_posicion(lista)
        elif opcion == "6":
            contar_numeros(lista)
        elif opcion == "7":
            posiciones_numero(lista)
        elif opcion == "8":
            mostrar_numeros(lista)
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()