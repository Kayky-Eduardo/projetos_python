#Faça um programa que sorteia os números da Mega Sena e da Lotofácil
import os
import random


os.system('cls')

print('-----MEGA SENA-----')
print('Números escolhidos: ')
for i in range(6):
    numeros = [random.randint(1, 100)]
    print(numeros, end= ' ')

print('\n')
print('-----LOTO FÁCIL-----')
print('Números escolhidos: ')
for j in range(15):
    num_loto = [random.randint(1, 100)]
    print(num_loto, end= ' ')    