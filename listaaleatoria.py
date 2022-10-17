import random

def lista_numeros():
    contador=0
    lst=[]
    while(contador<20):
        num_random=random.randint(0,100)
        contador+=1
        lst.append(num_random)
    return lst


"""
print("La longitud es",len(lista_numeros()))
print("El tipo de la lista es",type(lista_numeros()))
"""

def filtra_lista_pares(lst):
    lst_pares=[]
    for i in lst:
       if(i%2==0):
            lst_pares.append(i)
    return lst_pares

       
           
'''
Definir una función que dado una lista y un número
devuelva
   - True si se encuentra el número en la lista
   - False e.c.c.
'''

lista = lista_numeros()
print(lista)
numero= int(input("Dime un número: "))
def busqueda_num(lst, numero):
    if(numero in lst):
       return True
    else:
       return False

print(busqueda_num(lista,numero))