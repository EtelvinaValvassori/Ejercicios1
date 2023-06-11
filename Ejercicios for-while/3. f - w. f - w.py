#ingresar las edades y el sexo de 15 personas y determinar cuantas son mujeres cuantos varones cuantos mayores de edad y cuantos menores de edad

mujer = 0
varon = 0
mayor = 0
menor = 0
for i in range(15):
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (M/F): ")
    if sexo.upper() == "F": 
        mujer += 1 
    else:
        varon += 1
    if edad >= 18:
        mayor += 1
    else:
        menor += 1
print("Total de mujeres: ", mujer)
print("Total de varones: ", varon)
print("Total de mayores de edad: ", mayor)
print("Total de menores de edad: ", menor)

#No cuenta correctamente las mujeres y varones. No pude solucionarlo