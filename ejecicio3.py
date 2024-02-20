def determinar_grupo(nombre, sexo):
    if sexo.lower() == 'f':
        if nombre[0].lower() < 'm':
            return "Grupo A"
        else:
            return "Grupo B"
    elif sexo.lower() == 'm':
        if nombre[0].lower() >= 'n':
            return "Grupo A"
        else:
            return "Grupo B"
    else:
        return "Sexo no válido"

def main():
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (M para masculino, F para femenino): ")

    grupo = determinar_grupo(nombre, sexo)
    print("Usted pertenece al", grupo)

if __name__ == "__main__":
    main()