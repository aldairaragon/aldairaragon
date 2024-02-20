def calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva=21):
    """
    Calcula el total de una factura tras aplicarle el IVA.

    Parámetros:
        cantidad_sin_iva (float): La cantidad sin IVA.
        porcentaje_iva (float, opcional): El porcentaje de IVA a aplicar. Por defecto es 21%.

    Retorna:
        float: El total de la factura después de aplicar el IVA.
    """
    total = cantidad_sin_iva + cantidad_sin_iva * (porcentaje_iva / 100)
    return total

# Ejemplo de uso
cantidad = float(input("Ingrese la cantidad sin IVA: "))
total_con_iva = calcular_total_con_iva(cantidad)
print("Total con IVA (21%):", total_con_iva)