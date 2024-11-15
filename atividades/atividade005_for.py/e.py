#Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.
import os


os.system('cls')
soma = 0
for i in range(0, 101, 2):
        soma += i
        print(i)
print(f'Quantidade da soma dos números pares: {soma}')