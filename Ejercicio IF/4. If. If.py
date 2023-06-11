#Realice un programa que lea dos números y diga cuál es mayor

def compararnumeros(num1, num2):
    if num1>num2:
        print(num1,"es mayor")
    elif num1<num2:
        print(num2,"es mayor")
    else:
        print("Los números son iguales")
num1 = float(input("Ingrese primer número: "))
num2 = float(input("Ingrese segundo número: "))
resultado = compararnumeros(num1, num2)
print(resultado)


