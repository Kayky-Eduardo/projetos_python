import os


os.system('cls')

inic = int(input('Digite o início: '))
final = int(input('Digite o final: '))

for i in range(inic, final):
    divisor = 0
    for j in range(1, i+1):
        if i % j == 0:
            divisor += 1
    if divisor <= 2 and i >= 2:
        print(f'{i}', end=' | ')