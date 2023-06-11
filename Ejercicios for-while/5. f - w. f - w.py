#Leer 15 números negativos y convertirlos a positivos e imprimir dichos números

x = 4
num = 0
totalpos = []
totalneg = []
for i in range(x):
    num=int(input("Ingrese un número negativo: "))
    totalneg.append(num)
    if num >= 0:
        print("El número ingresado es incorrecto, por favor ingrese un número negativo: ") 
        x = i - 1      
    else:
        numpos = (-1) * num        
        totalpos.append(numpos) 
print("Los números ingresados son: ", totalneg)
print("Los números transformados son: ", totalpos)

#si ingresa un número que no sea negativo pide que ingrese otro, pero lo cuenta por lo que el total de negativos va a ser menor a 15. (no pude arreglarlo)