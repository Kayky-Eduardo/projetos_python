#Faça um programa que imprima os valores no intervalo definidos pelo usuário.  Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.
import os


os.system('cls')

intervalo = int(input('Digite o intervalo do loop: '))

for i in range(1, 20, intervalo):
    if i == 3:
        print(f'não imprimi o {i}')
        continue
    elif i == 6:
        print(f'não imprimi o {i}')
        continue
    elif i == 12:
        print(f'não imprimi o {i}')
        continue
    print(i)
