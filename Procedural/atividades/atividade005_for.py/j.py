#Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, 
# ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo, 
# assim como a soma dos mesmos.
import os


os.system('cls')

impar = 0
soma = 0

for i in range(1, 101, 2):
        impar += 1
        soma += i
print(f'quantidade de impar: {impar}')
print(f'soma dos números impares: {soma}')