#Utilizando o exercício anterior, coloque todas as listas em ordem crescente de valor
import os
import random

os.system('cls')

for i in range(6):
    lista = []
    for j in range(0, 51):
        lista.append(random.randint(1, 100))
        qntd = len(lista)
        if qntd > 9:
            break
    lista.sort()
    print(lista)
