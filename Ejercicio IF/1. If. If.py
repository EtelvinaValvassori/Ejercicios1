#Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje

def compararletras(letra1, letra2):
    if letra1==letra2:
        print("son iguales")
    else:
        print("son diferentes")
letra1 = input("Ingrese la primer letra: ")
letra2 = input("Ingrese la segunda letra: ")
resultado = compararletras(letra1, letra2)
print(resultado)
