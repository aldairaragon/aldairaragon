conductores = []
kms = {}




while True:
    nombre = input("Ingrese el nombre del conductor; escriba terminar si ya no tines mas conductores por ingresar")
    if nombre.lower() == 'terminar':
        break
    conductores.append(nombre)


for conductor in conductores:
    print(f"Ingrese los kilómetros de {conductor} que condujo cada día de la semana:")
    kms[conductor] = []
    for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]:
        kms[conductor].append(float(input(f"{dia}: ")))

total_kms = {nombre: sum(kilometros) for nombre, kilometros in kms.items()}

print("los kilometros recorridos por cada conductor son:")
for nombre, total_km in total_kms.items():
    print(f"{nombre}: {total_km} km")
