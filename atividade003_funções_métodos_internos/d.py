import os
import math


os.system('cls')

angulo = float(input('Digite seu ângulo: '))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print(f'O angulo {angulo} possui o seno {seno:.2f},'
      f' o cosseno de {cos:.2f} e a tangente de {tg:.2f}')