import random
import os
import math

os.system('cls')

dados1 = random.randint(1, 6)
dados2 = random.randint(1, 6)

soma = dados1 + dados2
raiz = math.sqrt(soma)

print(f'resultado do primeiro dado: {dados1}')
print(f'resultado do segundo dado: {dados2}')
print(f'raiz quadrada da soma dos numeros dos dados: {raiz:.2f}')