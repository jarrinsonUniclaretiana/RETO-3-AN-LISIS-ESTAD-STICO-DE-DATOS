from promedio import calcular_promedio
from max_min import calcular_max_min
from varianza import calcular_varianza

datos = []

def ingresar_datos():
    global datos
    entrada = input("Ingrese números separados por espacios: ")

    if entrada.strip() == "":
        print("Error: no ingresó ningún dato.")
        return

    try:
        datos = [float(x) for x in entrada.split()]
        print("Datos guardados correctamente.")
    except ValueError:
        print("Error: solo se permiten números.")

def mostrar_promedio():
    if len(datos) == 0:
        print("Error: primero debe ingresar datos.")
    else:
        print("Promedio:", calcular_promedio(datos))

def mostrar_max_min():
    if len(datos) == 0:
        print("Error: primero debe ingresar datos.")
    else:
        maximo, minimo = calcular_max_min(datos)
        print("Máximo:", maximo)
        print("Mínimo:", minimo)

def mostrar_varianza():
    if len(datos) < 2:
        print("Error: necesita al menos 2 datos.")
    else:
        print("Varianza:", calcular_varianza(datos))


# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Ingresar datos")
    print("2. Calcular promedio")
    print("3. Calcular máximo y mínimo")
    print("4. Calcular varianza")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ingresar_datos()
    elif opcion == "2":
        mostrar_promedio()
    elif opcion == "3":
        mostrar_max_min()
    elif opcion == "4":
        mostrar_varianza()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Error: opción inválida.")