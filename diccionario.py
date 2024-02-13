def agregar_persona(diccionario):
    nombre = input("aldair: ")
    apellido = input("aragon: ")
    ciudad_nacimiento = input("medellin: ")
    altura = input("1.84: ")
    email = input("aldairaragon420@gmail.com: ")
    telefono = input("312836469: ")

    diccionario[nombre] = {
        'Apellido': apellido,
        'Ciudad de nacimiento': ciudad_nacimiento,
        'Altura': altura,
        'Email': email,
        'Teléfono': telefono
    }

def mostrar_persona(diccionario):
    nombre = input("Ingrese el nombre de la persona a buscar: ")
    if nombre in diccionario:
        print("\nInformación de", nombre + ":")
        for key, value in diccionario[nombre].items():
            print(key + ":", value)
    else:
        print("La persona no se encuentra en el diccionario.")

def main():
    diccionario_personas = {}

    while True:
        print("\n1. Agregar persona")
        print("2. Mostrar información de una persona")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_persona(diccionario_personas)
        elif opcion == '2':
            mostrar_persona(diccionario_personas)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()