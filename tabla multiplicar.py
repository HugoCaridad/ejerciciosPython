#realizar una tabla de multiplicar

#VARIABLES
resultado = -1
indice = 0
numero = -1

#Muestro mensaje
print("Dime la tabla de multiplicar: ")
numero = int(input())
print("La tabla del ", numero)

while(indice <= 10):
    resultado = numero * indice
    print(numero, " x ", indice , " = ", resultado)
    indice = indice + 1



