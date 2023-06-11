#Realice un programa que lea 4 números y diga cuántos son pares y cuántos impares y devuelva la sumatoria de los pares.

x = 4
num = 0
numpar = 0
numimpar = 0
totalpar = 0
for i in range(x):
    num=int(input("Ingrese un número: "))
    if num % 2 == 0:
        numpar = numpar + 1 
        totalpar = totalpar + num
    else:
        numimpar = numimpar + 1
print("cantidad de números pares: ", numpar)
print("cantidad de número impares: ", numimpar)
print("Suma de números pares: ", totalpar)