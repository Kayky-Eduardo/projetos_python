#importando a biblioteca
import os

#limpando o terminal
os.system('cls')

#entrada
numero = int(input('Digite um número: '))

#processamento

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')