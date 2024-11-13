#Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.
import os


os.system('cls')

comeco = int(input('Digite o começo: '))
final = int(input('Digite onde ele termina: '))

for i in range(comeco, final):
    if i == 4:
        continue
    if i <= 5:
        print(i)
    elif i % 2 != 0 and i % 3 != 0 and i % 5 !=0:
        print(i)
print(f'Acabou')