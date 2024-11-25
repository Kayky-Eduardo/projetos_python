# Faça um programa que preencha uma lista com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.
import os
import random

os.system('cls')

lista = []

for i in range(50):
    aleatorio = random.randint(1, 100)
    lista.append(aleatorio)

fatiada = []
for i in range(0, 50, 10):
    partes = lista[i:i + 10]
    fatiada.append(partes)
print(fatiada)