#numero perfeitos

import os


os.system('cls')


for i in range(1, 100):
    divisores = 0
    for j in range(1, i):
        if i % j == 0:
            divisores += j
    if divisores == i:
        print(divisores)