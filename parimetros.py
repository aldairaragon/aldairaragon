def main():
    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Verificar si el primer número es mayor o igual al segundo
    if num1 >= num2:
        print(f"{num1} es mayor o igual que {num2}")
    else:
        print(f"{num1} no es mayor o igual que {num2}")

if __name__ == "__main__":
    main()
