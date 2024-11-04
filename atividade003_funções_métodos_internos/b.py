import os
import math


os.system('cls')

valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))

if valor2 == 0:
    print('erro!')
else:
    divisão = valor1 / valor2
    if divisão % 1 == 0:
        print(f'o resultado é: {divisão}')
    else:
        cima = math.ceil(divisão)
        baixo = math.floor(divisão)
        print(f'O resultado é {cima} ou {baixo}')