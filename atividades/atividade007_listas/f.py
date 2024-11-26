#Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.
import os
import random

os.system('cls')

lista = []
lista_a = []
lista_d = []

for i in range(10):
    lista.append(random.randint(1, 100))
    
lista.sort()
lista_a = lista
print(f'Lista ascendente: {lista_a}')

lista.sort(reverse=True)
lista_desc = lista
print(f'Lista descendente: {lista_desc}')