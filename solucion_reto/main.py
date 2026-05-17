# Importación de funciones desde los módulos
from promedio import calcular_promedio
from max_min import calcular_max_min
from varianza import calcular_varianza

# Lista global donde se almacenan los datos ingresados
datos = []

# Función para ingresar datos
def ingresar_datos():
    global datos  # Permite modificar la variable global
    entrada = input("Ingrese números separados por espacios: ")

    # Validar que no esté vacío
    if entrada.strip() == "":
        print("Error: no ingresó ningún dato.")
        return

    try:
        # Convertir la entrada a lista de números
        datos = [float(x) for x in entrada.split()]
        print("Datos guardados correctamente.")
    except ValueError:
        # Error si el usuario escribe algo que no es número
        print("Error: solo se permiten números.")

# Función para mostrar el promedio
def mostrar_promedio():
    if len(datos) == 0:
        print("Error: primero debe ingresar datos.")
    else:
        print("Promedio:", calcular_promedio(datos))

# Función para mostrar el valor máximo y mínimo
def mostrar_max_min():
    if len(datos) == 0:
        print("Error: primero debe ingresar datos.")
    else:
        maximo, minimo = calcular_max_min(datos)
        print("Máximo:", maximo)
        print("Mínimo:", minimo)

# Función para mostrar la varianza
def mostrar_varianza():
    if len(datos) < 2:
        print("Error: necesita al menos 2 datos.")
    else:
        print("Varianza:", calcular_varianza(datos))


# Menú interactivo
while True:
    print("\n--- MENÚ ---")
    print("1. Ingresar datos")
    print("2. Calcular promedio")
    print("3. Calcular máximo y mínimo")
    print("4. Calcular varianza")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # Evaluación de la opción seleccionada
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
        break  # Termina el programa
    else:
        print("Error: opción inválida.")
