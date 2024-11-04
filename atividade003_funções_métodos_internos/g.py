import os
import math

os.system('cls')

print('---------Equação de segundo grau----------')
a = float(input('Digite o valor a: '))
b = float(input('Digite o valor b: '))
c = float(input('Digite o valor c: '))

delta = (b * b) - ( 4 * a * c)

raiz_delta = math.sqrt(delta)

raiz1 = (- b + raiz_delta) / (2 * a)
raiz2 = (- b - raiz_delta) / (2 * a)

print(f'As raízes são {raiz1} e {raiz2}')