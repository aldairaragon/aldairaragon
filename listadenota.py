# Lista de nombres y notas de los estudiantes
estudiantes = [("Juan", 6), ("María", 3.5), ("Pedro", 7), ("Ana", 4.5), ("Luis", 2), ("Laura", 8), ("Carlos", 5)]

# Función para calificar las notas
def calificar_notas(estudiantes):
    calificaciones = []
    alumnos_muy_buenos = []
    for nombre, nota in estudiantes:
        if nota < 6:
            calificaciones.append((nombre, "Regular"))
        elif nota < 8:
            calificaciones.append((nombre, "Bueno"))
        else:
            calificaciones.append((nombre, "Muy bueno"))
            alumnos_muy_buenos.append(nombre)
    return calificaciones, alumnos_muy_buenos

# Calificar las notas de los estudiantes
calificaciones_estudiantes, alumnos_muy_buenos = calificar_notas(estudiantes)

# Imprimir las calificaciones
print("Calificaciones de los estudiantes:")
for nombre, calificacion in calificaciones_estudiantes:
    print(f"{nombre}: {calificacion}")

# Imprimir los nombres de los alumnos "Muy bueno"
print("\nNombres de los alumnos 'Muy bueno':")
for nombre in alumnos_muy_buenos:
    print(nombre)