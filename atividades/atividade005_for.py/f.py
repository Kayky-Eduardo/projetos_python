#Faça um programa que imprima os números primos entre 0 e 100.
import os


os.system('cls')


for i in range(2, 101):
    divisor = 0
    for j in range(1, i+1):
        if i % j == 0:
            divisor += 1
    if divisor <= 2:
        print(f'{i}', end=' | ')