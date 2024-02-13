def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def contar_anios_y_bisiestos(inicio, fin):
    cantidad_anios = fin - inicio + 1
    cantidad_bisiestos = sum(1 for year in range(inicio, fin + 1) if es_bisiesto(year))
    return cantidad_anios, cantidad_bisiestos

def main():
    anio_inicio = int(input("Ingrese el año de inicio: "))
    anio_fin = int(input("Ingrese el año de fin: "))
    
    cantidad_anios, cantidad_bisiestos = contar_anios_y_bisiestos(anio_inicio, anio_fin)
    
    print(f"Entre los años {anio_inicio} y {anio_fin} hay {cantidad_anios} años.")
    print(f"De ellos, {cantidad_bisiestos} son años bisiestos.")

if __name__ == "__main__":
     main()