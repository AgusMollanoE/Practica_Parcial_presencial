
import os

# VARIABLE GLOBAL
DIM = 50

# Auxiliares para limpiar pantalla y pausar
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    os.system("pause" if os.name == "nt" else "input('Presione Enter para continuar...')")

# FUNCIONES

# 1. Cargar pesos de contenedores
def cargar_pesos(cantidad):
    pesos = []
    print(f"--- Carga de {cantidad} contenedores ---")
    for i in range(cantidad):
        while True:
            try:
                peso = int(input(f"Ingrese el peso del contenedor {i+1} (kg): "))
                if peso < 0:
                    print("ERROR: El peso no puede ser negativo.")
                else:
                    pesos.append(peso)
                    break
            except ValueError:
                print("ERROR: Ingrese un número entero válido.")
            except Exception as error:
                            print(f"Error inesperado: {error}")
    return pesos

# 2. Mostrar contenido de una lista
def mostrar_pesos(pesos, titulo="Lista de Pesos"):
    if not pesos:
        print(f"{titulo}: (Lista vacía)")
        return
    print(f"--- {titulo} ---")
    for i, peso in enumerate(pesos):
        print(f"Contenedor {i+1}: {peso} kg")
        
# 3. Calcular promedio de los pesos
def calcular_promedio(pesos):
    if not pesos:
        return 0.0
    return sum(pesos) / len(pesos)

# 4. Filtrar a Pila (Carga Pesada) y Arreglo (Carga Estándar)
def filtrar_pesos(pesos, promedio):
    pila_mayores = []   # Funciona como Pila
    arreglo_menores = []

    for peso in pesos:
        if peso > promedio:
            pila_mayores.append(peso) # Apilamos
        else:
            arreglo_menores.append(peso)

    return pila_mayores, arreglo_menores

# 5. Buscar el menor en la Pila de mayores
def buscar_menor_pila(pila_mayores):
    if not pila_mayores:
        return None
    return min(pila_mayores)

# 6. Buscar el mayor en el arreglo de menores
def buscar_mayor_arreglo(arreglo_menores):
    if not arreglo_menores:
        return None
    return max(arreglo_menores)

# 7. Contar elementos de la Pila de mayores
def contar_elementos_pila(pila_mayores):
    return len(pila_mayores)

# 8. Cargar nombres de Buques o Empresas de transporte
def cargar_nombres(cantidad, tipo):
    nombres = []
    print(f"\n--- Carga de {tipo} ({cantidad} requeridos) ---")
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre de {tipo} {i+1}: ").strip()
        while not nombre:
            nombre = input("El nombre no puede estar vacío. Reintente: ").strip()
        nombres.append(nombre)
    return nombres

# 9. Mostrar nombres cargados
def mostrar_nombres(nombres, tipo="Transportes"):
    if not nombres:
        print(f"No hay {tipo} registrados.")
        return
    print(f"\n--- Lista de {tipo} ---")
    for i, nombre in enumerate(nombres):
        print(f"{i+1}. {nombre}")
        
# 10. Main()

lista_pesos = []
pila_mayores = []
arreglo_menores = []
lista_nombres = []
tipo_transporte = ""

# MENU
while True:
    limpiar_pantalla()
    print("========================================")
    print("    TERMINAL PORTUARIA MAR DEL PLATA    ")
    print("========================================")
    print(" 1. Cargar Pesos de Contenedores")
    print(" 2. Mostrar Contenedores")
    print(" 3. Calcular Promedio y Filtrar")
    print(" 4. Ver Pesos Críticos (Min / Max)")
    print(" 5. Balance Operativo y Cargar Nombres")
    print(" 6. Mostrar Nombres Registrados")
    print(" 0. Salir")
    print("========================================")

    opcion = input("Seleccione una opción: ")
    limpiar_pantalla()

    if opcion == "1":
        lista_pesos = cargar_pesos(DIM)
        pausar()

    elif opcion == "2":
        mostrar_pesos(lista_pesos, "Contenedores Cargados")
        pausar()

    elif opcion == "3":
        if not lista_pesos:
            print("ERROR: Primero debe cargar los pesos en la opción 1.")
        else:
            promedio = calcular_promedio(lista_pesos)
            print(f"Peso promedio diario: {promedio:.2f} kg\n")

            pila_mayores, arreglo_menores = filtrar_pesos(lista_pesos, promedio)

            print(f"Carga Pesada (> {promedio:.2f} kg): {pila_mayores}")
            print(f"Carga Estándar (<= {promedio:.2f} kg): {arreglo_menores}")
            pausar()

    elif opcion == "4":
        if not pila_mayores and not arreglo_menores:
            print("ERROR: Primero ejecute el filtro en la opción 3.")
        else:
            menor_pesado = buscar_menor_pila(pila_mayores)
            mayor_estandar = buscar_mayor_arreglo(arreglo_menores)

            print("--- VALORES CRÍTICOS ---")
            if menor_pesado is not None:
                print(f"• Contenedor más liviano de Carga Pesada (Grúa pequeña): {menor_pesado} kg")
            else:
                print("• No hay contenedores en Carga Pesada.")

            if mayor_estandar is not None:
                print(f"• Contenedor más pesado de Carga Estándar (Reforzar camión): {mayor_estandar} kg")
            else:
                print("• No hay contenedores en Carga Estándar.")
        pausar()

    elif opcion == "5":
        cant_pesados = contar_elementos_pila(pila_mayores)
        cant_estandar = len(arreglo_menores)

        if cant_pesados == 0 and cant_estandar == 0:
            print("ERROR: Primero ejecute el filtro en la opción 3.")
        else:
            print(f"Contenedores Pesados: {cant_pesados} | Contenedores Estándar: {cant_estandar}\n")

            if cant_pesados > cant_estandar:
                print("--> Predomina la CARGA PESADA.")
                critico = buscar_menor_pila(pila_mayores)
                print(f"Peso crítico asignado: {critico} kg")
                tipo_transporte = "Buques"
                lista_nombres = cargar_nombres(cant_pesados, "Buque")

            elif cant_estandar > cant_pesados:
                print("--> Predomina la CARGA ESTÁNDAR.")
                critico = buscar_mayor_arreglo(arreglo_menores)
                print(f"Peso crítico asignado: {critico} kg")
                tipo_transporte = "Empresas Terrestres"
                lista_nombres = cargar_nombres(cant_estandar, "Empresa de Transporte")

            else:
                print("--> Hay IGUALDAD entre Carga Pesada y Estándar.")
                critico = buscar_menor_pila(pila_mayores) or buscar_mayor_arreglo(arreglo_menores)
                print(f"Peso crítico: {critico} kg")
                tipo_transporte = "Buques"
                lista_nombres = cargar_nombres(cant_pesados, "Buque")
        pausar()

    elif opcion == "6":
        mostrar_nombres(lista_nombres, tipo_transporte)
        pausar()

    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
        pausar()