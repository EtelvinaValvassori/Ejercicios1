#Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.

def compararnumeros(num1, num2, num3):
    if num1>num2 and num1>num3: 
        print (num1, "Es el número mayor")
        if num1 % 2 == 0:
            print("Es un número par")
        else:
            print("Es un número impar")
    elif num2>num1 and num2>num3:
        print (num2, "Es el número mayor")
        if num2 % 2 == 0:
            print("Es un número par")
        else:
            print("Es un número impar")
    else:
        print (num3, "Es el número mayor")
        if num3 % 2 == 0:
            print("Es un número par")
        else:
            print("Es un número impar")         
num1 = float(input("Ingrese primer número: "))
num2 = float(input("Ingrese segundo número: "))
num3 = float(input("Ingrese tercer número: "))
resultado = compararnumeros(num1, num2, num3)
print(resultado)
     