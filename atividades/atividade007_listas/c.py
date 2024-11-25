#Utilizando o exercício anterior, coloque todas as listas em ordem crescente de valor
import os
import random

os.system('cls')

lista = []

for i in range(50):
    lista.append(random.randint(1, 100))

fatiada = []
for i in range(0, 50, 10):
    partes = lista[i:i + 10]
    partes.sort()
    fatiada.append(partes)

print(fatiada)