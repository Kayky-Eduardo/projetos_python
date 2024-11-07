import os
import math
import random


os.system('cls')

x1 = random.randint(0,50)
y1 = random.randint(0,50)
x2 = random.randint(0,50)
y2 = random.randint(0,50)

distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f'coordenada X1: {x1}')
print(f'Coprdenada X2: {x2}')
print(f'Coordenada Y1: {y1}')
print(f'Coordenada Y2: {y2}')
print(f'a distância entre os pontos são: {distancia:.2f}')