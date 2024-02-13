def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")

    agenda[nombre] = telefono
    print("Contacto agregado exitosamente.")

def mostrar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea buscar: ")
    if nombre in agenda:
        print("Nombre:", nombre)
        print("Teléfono:", agenda[nombre])
    else:
        print("El contacto no se encuentra en la agenda.")

def mostrar_agenda(agenda):
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("Lista de contactos en la agenda:")
        for nombre, telefono in agenda.items():
            print("Nombre:", nombre)
            print("Teléfono:", telefono)
            print()

def main():
    agenda = {}

    while True:
        print("\n1. Agregar contacto")
        print("2. Mostrar contacto")
        print("3. Mostrar agenda")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            mostrar_contacto(agenda)
        elif opcion == '3':
            mostrar_agenda(agenda)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()