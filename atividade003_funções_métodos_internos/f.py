import random
import os


os.system('cls')

numero = random.randint(1, 10)

resposta = int(input('Digite um número de 1 a 10: '))

if resposta < 1 or resposta > 10:
    print('Ultrapassou o limite, tentou quebrar com a brincadeira!')
elif resposta != numero:
    print('Boa tentativa, tente denovo!')
else:
    print(f'parabéns você conseguiu acertar o número')