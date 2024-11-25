#Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.
import os
import random

os.system('cls')

lista = []
for i in range(10):
    lista.append(random.randint(1, 100))

lista.sort()
print(f'Lista ascendente: {lista}')

lista.reverse()
print(f'Lista descendente: {lista}')
