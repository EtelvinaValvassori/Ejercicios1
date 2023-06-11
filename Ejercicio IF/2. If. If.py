#Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.

def compararpalabras(palabra1, palabra2):
    if palabra1 == palabra2:
        print ("Son iguales")
    else:
        print ("Son diferentes")
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
resultado = compararpalabras(palabra1, palabra2)
print(resultado)
