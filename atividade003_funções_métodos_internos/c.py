import os
import math

os.system('cls')

base = float(input('Insira a base: '))
expoente = float(input('Insira o expoente: '))

potencia = math.pow(base, expoente)

print(f'O valor da potência é de {potencia}')