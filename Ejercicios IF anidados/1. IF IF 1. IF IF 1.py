#Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.

def compararnumeros(lado1, lado2, lado3):
    if lado1==lado2==lado3:
        print(lado1, lado2, lado3, "forma un triángulo equilátero")
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print(lado1, lado2, lado3, "forma un triángulo isósceles")
    else:
        print(lado1, lado2, lado3, "forma un triángulo escaleno") 
lado1 = float(input("Ingrese primer número: "))
lado2 = float(input("Ingrese segundo número: "))
lado3 = float(input("Ingrese segundo número: "))
resultado = compararnumeros(lado1, lado2, lado3)
print(resultado)
