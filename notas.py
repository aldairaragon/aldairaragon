def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    else:
        return sum(notas) / len(notas)

def main():
    num_alumnos = int(input("Ingrese el número de alumnos: "))
    alumnos = {}

    for _ in range(num_alumnos):
        nombre = input("Ingrese el nombre del alumno: ")

        if nombre in alumnos:
            print("El alumno ya existe en la lista.")
            continue

        notas = []
        nota = float(input(f"Ingrese la nota del alumno {nombre} (ingrese un número negativo para terminar): "))
        while nota >= 0:
            notas.append(nota)
            nota = float(input("Ingrese la siguiente nota (ingrese un número negativo para terminar): "))

        alumnos[nombre] = notas

    print("\nLista de alumnos y sus promedios:")
    for nombre, notas in alumnos.items():
        promedio = calcular_promedio(notas)
        print(f"{nombre}: Promedio = {promedio:.2f}")

if __name__ == "__main__":
    main()