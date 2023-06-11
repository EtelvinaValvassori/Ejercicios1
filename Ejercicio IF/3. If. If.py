#Realizar un programa que permita ingresar "f" o "m" y determinar si vota en mesa femenina o masculina

def ingresargenero(genero1, genero2):
    if genero1.lower() == "f":
        print("Vota en mesa femenina")
    elif genero2.lower() == "m":
        print("Vota en mesa masculina")
    else:
        print("Error. Género no conocido, vuelva a ingresar el género")
genero = input("Ingrese su género: ")



