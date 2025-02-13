#Faça um programa que sorteia os números da Mega Sena e da Lotofácil
import os
import random


os.system('cls')

print('-----MEGA SENA-----')
print('Números escolhidos: ')

# sample não deixa repetir
megasena = random.sample(range(1, 61), 6)

print(megasena, end= ' ')
print('\n')
print('-----LOTO FÁCIL-----')
print('Números escolhidos: ')

num_loto = random.sample(range(1, 26), 15)
print(num_loto, end= ' ')    