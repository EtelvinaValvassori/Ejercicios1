#Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.

def convertir_dolares_a_pesos(dolares):
    tasa_cambio = 350.0  # Tasa de cambio: 1 dólar = 350.0 pesos
    pesos = dolares * tasa_cambio
    return pesos

def convertir_pesos_a_dolares(pesos):
    tasa_cambio = 350.0  # Tasa de cambio: 1 dólar = 350.0 pesos
    dolares = pesos / tasa_cambio
    return dolares

opcion = input("¿Qué conversión deseas realizar? (1: Dólares a pesos, 2: Pesos a dólares): ")

if opcion == "1":
    dolares = float(input("Ingrese la cantidad en dólares: "))
    pesos = convertir_dolares_a_pesos(dolares)
    print(f"{dolares} dólares equivale a {pesos} pesos.")
elif opcion == "2":
    pesos = float(input("Ingrese la cantidad en pesos: "))
    dolares = convertir_pesos_a_dolares(pesos)
    print(f"{pesos} pesos equivale a {dolares} dólares.")
else:
    print("Opción no válida. Por favor, seleccione 1 o 2.")
