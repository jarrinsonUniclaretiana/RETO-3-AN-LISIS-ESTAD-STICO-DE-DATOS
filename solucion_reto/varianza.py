def calcular_varianza(datos):
    promedio = sum(datos) / len(datos)

    suma = 0
    for numero in datos:
        suma += (numero - promedio) ** 2

    varianza = suma / len(datos)

    return varianza