#Leer 10 números y mostrar solamente los números positivos y sus sumatoria

x = 10
num = 0
numpos = 0
numneg = 0
totalpos = []
for i in range(x):
    num=int(input("Ingrese un número: "))
    if num > 0:
        numpos = numpos + num
        totalpos.append(num) #para que muestre los positivos
    else:
        numneg
print("Los números positivos son: ", totalpos)
print("Suma de números positivos es: ", numpos)