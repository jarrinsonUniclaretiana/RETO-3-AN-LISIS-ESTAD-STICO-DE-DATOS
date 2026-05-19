# Importaciones con manejo de errores
try:
    from promedio import calcular_promedio
except ImportError:
    calcular_promedio = None

try:
    from max_min import calcular_max_min
except ImportError:
    calcular_max_min = None

try:
    from varianza import calcular_varianza
except ImportError:
    calcular_varianza = None


# Lista global de datos
datos = []


# Función para ingresar datos
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


# Función para promedio
def mostrar_promedio():
    if calcular_promedio is None:
        print("Módulo de promedio no disponible.")
    elif len(datos) == 0:
        print("Error: primero debe ingresar datos.")
    else:
        print("Promedio:", calcular_promedio(datos))


# Función para máximo y mínimo
def mostrar_max_min():
    if calcular_max_min is None:
        print("Módulo de max/min no disponible.")
    elif len(datos) == 0:
        print("Error: primero debe ingresar datos.")
    else:
        maximo, minimo = calcular_max_min(datos)
        print("Máximo:", maximo)
        print("Mínimo:", minimo)


# Función para varianza
def mostrar_varianza():
    if calcular_varianza is None:
        print("Módulo de varianza no disponible.")
    elif len(datos) < 2:
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
