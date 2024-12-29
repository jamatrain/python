mi_numero  =  1
edad  = input("Dime  tu edad: ")
sum_edad = int(edad) + 2
print("Tu edad dentro de 2 seria : " + str(sum_edad))

#Primera manera de concatenar variables en un string
print("tu edad es {} y tu edad sera {}".format(edad, sum_edad))


#Segunda manera de concatenar variables en un string, cadenas literales
color = "rojo"
matricula = 12345
print(f"El auto es {color} y su matricula es {matricula}")