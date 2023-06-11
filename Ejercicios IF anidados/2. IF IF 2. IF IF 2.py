#Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:Contado (1) se aplica un descuento del 10% al importe. Tarjeta (2) se aplica un interés del 10%. Débito (3) se aplica un descuento del 5%. Mostrando el importe, el descuento o interés y el importe total 

monto = float(input("Ingrese el monto: "))
pago = int(input("Ingrese forma de pago: 1, 2, 3: "))
monto2 = monto * 0.1
monto3 = monto * 0.05
calculartotal1 = monto - monto2
calculartotal2 = monto + monto2
calculartotal3 = monto - monto3
if pago == 1:
    monto2 = monto * 0.1
    calculartotal1 = monto - monto2
    print("El monto ingresado es: ", monto, "El interés es: ", monto2, "El monto total a pagar es: ", calculartotal1)
elif pago == 2:
    monto2 = monto * 0.1
    calculartotal2 = monto + monto2
    print("El monto ingresado es: ", monto, "El interés es: ", monto2, "El monto total a pagar es: ", calculartotal2)
elif pago == 3:
    monto3 = monto * 0.05
    calculartotal3 = monto - monto3
    print("El monto ingresado es: ", monto, "El interés es: ", monto3, "El monto total a pagar es: ", calculartotal3)
else:
    print("Opción de pago inválida, por favor ingrese la opción correspondiente")


