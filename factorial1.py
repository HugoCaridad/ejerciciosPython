#Realizar un programa que calcule el Factorial de un número

def factorial(n):
    index = n
    res = 1
    
    while(index > 0):
        res = res * index
        index -= 1
        
    print("El factorial del numero ", n, "es ", res)
    
    return res

print(factorial(4))
          