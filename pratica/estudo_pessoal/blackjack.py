import os
import random


os.system('cls')

print('------ JOGO DE CARTA 21 -------')
p1 = input('Qual o nome do jogador: ')


ás = 1
nobres = 10
cartas = [random.randint(2, 10), ás, nobres]


primeira = random.choice(cartas)
total = primeira 
print(f'Você puxou a carta {primeira}. Total: {total}')


segunda_car = input('Quer puxar uma segunda carta? (sim/não): ').lower()

if segunda_car == 'sim' or segunda_car == 's':
    segunda = random.choice(cartas)
    total += segunda  
    print(f'Você puxou a carta {segunda}. Total agora: {total}')
else:
    print(f'OK! Você parou com {total}')

if total < 21:
    terceira_car = input('Quer puxar uma terceira carta? (sim/não): ').lower()

    if terceira_car == 'sim' or terceira_car == 's':
        terceira = random.choice(cartas)
        total += terceira  
        print(f'Você puxou a carta {terceira}. Total agora: {total}')
    else:
        print(f'OK! Você parou com {total}')

if total < 21:
    quarta_car = input('Quer puxar uma quarta carta? (sim/não): ').lower()

    if quarta_car == 'sim' or quarta_car == 's':
        quarta = random.choice(cartas)
        total += quarta 
        print(f'Você puxou a carta {quarta}. Total agora: {total}')
    else:
        print(f'OK! Você parou com {total}')

if total < 21:
    quinta_car = input('Quer puxar uma quinta carta? (sim/não): ').lower()

    if quinta_car == 'sim' or quinta_car == 's':
        quinta = random.choice(cartas)
        total += quinta  
        print(f'Você puxou a carta {quinta}. Total agora: {total}')
    else:
        print(f'OK! Você parou com {total}')

if total > 21:
    print(f'Você ultrapassou 21! Você perdeu com {total}.')
else:
    print(f'Você terminou com {total}.')