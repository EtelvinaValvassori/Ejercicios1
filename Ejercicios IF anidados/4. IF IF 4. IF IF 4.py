#Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.

def diadelasemana(numero):
    if numero == 1:
        print("es día Lunes")
    elif numero == 2:
        print("Es día Martes")
    elif numero == 3:
        print("Es día Miércoles")
    elif numero == 4:
        print("Es día Jueves")
    elif numero == 5:
        print("Es día Viernes")
    elif numero == 6:
        print("Es día Sabado")
    elif numero == 7:
        print("Es día Domingo")
    else: 
        print("Error en la carga del dato, por favor ingrese nuevamente el número") 
numero = int(input("Ingrese un número del 1 al 7: "))
resultado = diadelasemana(numero)
print(resultado)
