#introduciendo la hora del dia en horas, min y segundos, calcular cuantos segundos han transcurrido desde el contenido del dia
#Ej 1

#VARIABLES
hora = 0
minutos = 0
segundos = 0


print("Dime la hora ")
hora = input()
minutos = int(input("Dime los mminutos: "))
segundos = int(input("Dime los segundos: "))


hora = hora * 3600
minutos = minutos * 60
segundos = segundos + minutos + hora

print("Han transcurrido desde el inicio del día ", segundos, "segundos")