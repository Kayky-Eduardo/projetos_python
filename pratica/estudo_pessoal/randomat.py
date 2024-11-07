import os
import math
import random

os.system('cls')

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)
num4 = random.randint(1, 100)
num5 = random.randint(1, 100)
num6 = random.randint(1, 100)
num7 = random.randint(1, 100)
num8 = random.randint(1, 100)
num9 = random.randint(1, 100)
num10 = random.randint(1, 100)

#seno do num1
seno = math.sin(math.radians(num1))
#cosseno do num2
cos = math.cos(math.radians(num2))
#tangente do num3
tan = math.tan(math.radians(num3))
#potência no num4 pelo num5
potencia = math.pow(num4, num5)
#hipotenusa
hipotenusa = math.hypot(num6, num7)
#media
media = (num8 + num9 + num10) / 3

print(f'seno de {num1}:{seno:.2f}')
print(f'cosseno de {num2}: {cos:.2f}')
print(f'tangente de {num3}: {tan:2f}')
print(f'potencia de {num4} por {num5}: {potencia:.2f}')
print(f'hipotenusa(co = {num5} e ca = {num6}) = {hipotenusa:.2f}')
print(f'media de {num8}, {num9} e {num9}: {media:.2f}')