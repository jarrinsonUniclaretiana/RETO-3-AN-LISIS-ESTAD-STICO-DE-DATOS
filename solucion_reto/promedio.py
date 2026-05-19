def calcular_promedio(lista):
    """
    Calcula el promedio de una lista de números.
    """
    if len(lista) == 0:
        return 0  # evitar división por cero

    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio
