#Faça um programa que leia as vogais, depois mostre-as em ordem inversa.
import os


os.system('cls')

vogais = []

for i in range(5):
    entrada = input('Digite as vogais: ').lower()
    if entrada in 'aeiou':
        vogais.append(entrada)
    else:
        print('Não é uma vogal')
        i -= 1
print(f'Ordem inversa: {vogais[::-1]}')