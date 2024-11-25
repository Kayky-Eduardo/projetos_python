#Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.
import os


os.system('cls')

nomes = []

for i in range(6):
    entrada = input('Digite seu nome: ')
    nomes.append(entrada)

for i in range(len(nomes)):
    print(f'Índice {i}: {nomes[i]}', end= ' | ')