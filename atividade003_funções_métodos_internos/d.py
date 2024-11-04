import os
import math


os.system('cls')

angulo = float(input('Digite seu ângulo: '))

radiano = math.radians(angulo)
seno = math.sin(radiano)
cos = math.cos(radiano)
tg = math.tan(radiano)

print(f'O angulo {angulo} possui o seno {seno:.2f},'
      f' o cosseno de {cos:.2f} e a tangente de {tg:.2f}')