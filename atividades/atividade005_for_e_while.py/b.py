#Evolua o programa anterior para um código que pergunte ao usuário
# qual o intervalo que ele deseja ver  impresso.
import os


os.system('cls')

comeco = int(input('Começa em: '))
parar = int(input('Para em:'))
intervalo = int(input('Qual o intervalo que você deseja imprimir: '))

for i in range(comeco, parar + 1, intervalo):
    print(f'{i}', end=' | ')
    if i % 10 == 0:
        print('\n')
print('Acabou!')