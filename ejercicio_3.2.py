#Bucles while ej 3.2
total_multiplos = 0
numero = -1
index = 1

numero = int(input("Dime un numero: "))

while(index <= numero):
    if(index % 3 == 0):
        total_multiplos += 1
    
    index += 1

print("Entre la unidad y el número ", numero, "Hay un total de ", total_multiplos , "multiplos")