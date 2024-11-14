#Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.
import os


os.system('cls')

comeco = int(input('Digite o começo: '))
final = int(input('Digite onde ele termina: '))

for i in range(comeco, final):
    divisor = 0
    for j in range(1, i+1):
        if i % j == 0:
            divisor += 1
    if divisor <= 2 and i >= 2:    
        print(f'{i}', end= ' | ')