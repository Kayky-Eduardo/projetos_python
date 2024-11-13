#Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.
import os


os.system('cls')

for i in range(0, 100 + 1):
    if i % 2 == 0:
        i += i
        print(i)
print('Fim!')