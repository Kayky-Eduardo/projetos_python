# Faça um programa que preencha uma lista com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.
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
    print(lista)