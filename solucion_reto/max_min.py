def calcular_max_min(lista):
    if len(lista) == 0:
        raise ValueError("La lista está vacía")
    return max(lista), min(lista)