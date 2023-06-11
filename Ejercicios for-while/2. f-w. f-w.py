#Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.

x = 10
num = 0
nummenor = 0
nummayor = 0
numero = []                              #lista vacía 
for i in range(x):
    num=int(input("Ingrese un número: "))
    numero.append(num)                        #almacena numeros 
    if num < 100:
        nummenor = nummenor + 1 
    else:
        nummayor = nummayor + 1
print("cantidad de números menores a 100 son: ", nummenor)
print("cantidad de número mayores a 100 son: ", nummayor)
print("El número mayor es: ", max (numero))
print("El número menor es: ", min (numero))
