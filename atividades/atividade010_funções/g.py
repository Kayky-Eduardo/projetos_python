import os

from funcoes_usadas import matematica

os.system('cls')




a = float(input('Digite um número maior que 0 e menor q 11: '))
b = float(input('Digite outro número maior que 0 e menor q 11: '))

print('\nMenu: ')
print('1. Soma\n2. Subtração\n3. Produto\n4. Divisão\n5. Divisão inteira\n\
6. Resto da divisão')

opcao = input('\nEscolha uma das opções(1-6): ')

if opcao == '1':
    print(f'A soma de {a} por {b} é: {matematica.Soma(a, b):.2f}')

elif opcao == '2':
    print(f'A subtração de {a} por {b} é: {matematica.Subtracao(a, b):.2f}')

elif opcao == '3':
    print(f'O produto de {a} por {b} é: {matematica.Produto(a, b):.2f}')

elif opcao == '4':
    print(f'A divisão de {a} por {b} é: {matematica.Divisao(a, b):.2f}')

elif opcao == '5':
    print(f'A divisão inteira de {a} por {b} é: {matematica.Divisao_inteira(a, b):.2f}')

elif opcao == '6':
    print(f'O resto da divisão de {a} por {b} é: {matematica.Resto_da_divisao(a, b):.2f}')