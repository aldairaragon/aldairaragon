import random

def tirar_dado():
    return random.randint(1, 6)

def jugar():
    print("¡Bienvenido al juego de tirar el dado!")
    input("Presiona Enter para tirar el dado...")

    # Tirar el dado para Álvaro
    print("\nTirando el dado para Álvaro...")
    resultado_alvaro = tirar_dado()
    print("Álvaro obtuvo:", resultado_alvaro)

    # Tirar el dado para Bárbara
    print("\nTirando el dado para Bárbara...")
    resultado_barbara = tirar_dado()
    print("Bárbara obtuvo:", resultado_barbara)

    # Determinar el resultado
    if resultado_alvaro > resultado_barbara:
        print("\n¡Álvaro gana!")
    elif resultado_alvaro < resultado_barbara:
        print("\n¡Bárbara gana!")
    else:
        print("\n¡Es un empate!")

# Iniciar el juego
jugar()