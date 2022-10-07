num = input("Dime un numero")
tam = len(num)

num_sin_digito = ""

for i in range(1, tam):
    num_sin_digito += num[i]
    
print(num_sin_digito)