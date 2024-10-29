import os 


os.system('cls')

numero = int(input('Digite um numero inteiro: '))

if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')