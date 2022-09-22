#Escriba, usando comparaciones, un algoritmo que muestre el estado del agua (hielo, liquido, vapor) en función de su temperatura

#VARIABLES
temp = 0.0

temp = float(input("Dime la temperatura: "))

#ESTADOS
if (temp < 0):
     print(temp, "Su estado esta en hielo")
else:
    if (temp >= 100):
        print(temp, "Su estado esta en vapor")
    else:
        print(temp, "su estado esta en liquido")