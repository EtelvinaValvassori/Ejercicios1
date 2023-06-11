#Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo "puede votar", sino "no vota".

def comparar(edad, valor):
    if edad>valor:
        print("puede votar")
    else:
        print ("no vota") 
edad = int(input("Ingrese su edad: "))  
resultado = comparar(edad, 16) 
print(resultado)