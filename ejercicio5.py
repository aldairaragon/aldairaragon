def main():
    # Contraseña almacenada
    contraseña_correcta = "contraseña123"

    # Solicitar la contraseña al usuario
    intentos = 3
    while intentos > 0:
        contraseña_ingresada = input("Ingrese la contraseña: ")

        # Verificar si la contraseña es correcta
        if contraseña_ingresada == contraseña_correcta:
            print("¡Contraseña correcta! Bienvenido.")
            break
        else:
            intentos -= 1
            print("Contraseña incorrecta. Te quedan {} intentos.".format(intentos))

    if intentos == 0:
        print("Has agotado todos tus intentos. Acceso denegado.")

if __name__ == "__main__":
    main()