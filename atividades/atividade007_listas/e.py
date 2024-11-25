#Faça um programa que receba 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares.
import os


os.system('cls')
 
lista = []
lista_pares = []
lista_impar = []

for i in range(7):
    inteiros = int(input('Digite os números: '))
    lista.append(inteiros)

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impar.append(i)
        
print(f'Números pare: {lista_pares}')
print(f'Números ímpares: {lista_impar}')