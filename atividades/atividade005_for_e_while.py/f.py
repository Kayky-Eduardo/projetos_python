#Faça um programa que imprima os números primos entre 0 e 100.
import os


os.system('cls')


for i in range(1, 101):
    if i == 4:
        continue
    if i <= 5:
        print(i)
    elif i % 2 != 0 and i % 3 != 0 and i % 5 !=0:
        print(i)
print(f'Acabou')