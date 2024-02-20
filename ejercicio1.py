def ejercicio1():
    print("Este es el ejercicio 1")

def ejercicio2():
    print("Este es el ejercicio 2")

def ejercicio3():
    print("Este es el ejercicio 3")

def mostrar_menu():
    print("Menú Principal:")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido del menú.")

if __name__ == "__main__":
    main()