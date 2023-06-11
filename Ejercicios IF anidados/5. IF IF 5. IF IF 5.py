#Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.

def mes(numero):
    if numero == 1:
        print("Es  Enero")
    elif numero == 2:
        print("Es Febrero")
    elif numero == 3:
        print("Es Marzo")
    elif numero == 4:
        print("Es Abril")
    elif numero == 5:
        print("Es Mayo")
    elif numero == 6:
        print("Es Junio")
    elif numero == 7:
        print("Es Julio")
    elif numero == 8:
        print("Es Agosto")
    elif numero == 9:
        print("Es Septiembre")
    elif numero == 10:
        print("Es Octubre")
    elif numero == 11:
        print("Es Noviembre")
    elif numero == 12:
        print("Es Diciembre")
    else: 
        print("Error en la carga del dato, por favor ingrese nuevamente el número") 
numero = int(input("Ingrese un número del 1 al 12: "))
resultado = mes(numero)
print(resultado)