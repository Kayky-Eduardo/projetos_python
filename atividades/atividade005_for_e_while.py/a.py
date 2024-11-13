#Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.
import os


os.system('cls')

for i in range(1, 100 + 1):
    print(f'{i}', end=' | ')
    if i % 10 == 0:
        print('\n')