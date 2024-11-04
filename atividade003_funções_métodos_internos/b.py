import os
import math


os.system('cls')

valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))

divisão = valor1 / valor2
cima = math.ceil(divisão)
baixo = math.floor(divisão)

if divisão // 1 == divisão:
    print(f'O resultado é {divisão}')
else:
    print(f'o resultado é {cima} ou {baixo} (arrendondado para cima e para baixo respectivamente)')