#Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.
import os


os.system('cls')

inicio = 1
fim = 10

for i in range(1, 11)[::-1]:
    print(f'{i}', end=' | ')
    