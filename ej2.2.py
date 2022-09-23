#Escriba un algoritmo que determine la categoría deportiva de un usuario en funcion de su edad
#6 a 7 años : "BENJAMIN"
#8 a 9 : "ALEVIN"
#10 a 11 años : "INFANTIL"
#12 años y más : "CADETE"

edad = 0
print("Dime la edad del niño : ")
edad = int(input())

if(edad < 0):
    print("El niño no tiene categoria deportiva")
elif(edad == 0 or edad == 7):
    print("La categoría del niño es BENJAMÍN")
elif(edad == 8 or edad == 9):
    print("La categoría del niño es ALEVIN")
elif(edad == 10 or edad == 11):
    print("La categoría del niño es INFANTIL")
elif(edad >= 12 ):
    print("La categoría del niño es CADETE")