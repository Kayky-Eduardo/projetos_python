import os
import random

os.system('cls')

print('------ JOGO DE CARTA 21 -------')
p1 = input('Qual o nome do jogador: ')

ás = 1
nobres = 10
cartas = [random.randint(2, 10), ás, nobres]

total = 0
continuar = True

while continuar and total < 21:
    carta = random.choice(cartas)
    total += carta
    print(f'Você puxou a carta {carta}.\nTotal: {total}')
    
    if total >= 21:
        break

    resposta = input('Quer puxar outra carta? (sim/não): ').lower()
    if resposta not in ['sim', 's']:
        continuar = False

if total > 21:
    print(f'Você ultrapassou 21! Você perdeu com {total}.')
else:
    print(f'Você terminou com {total}.')
