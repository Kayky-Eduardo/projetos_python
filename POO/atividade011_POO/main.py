import os

from modulo.matematica import OperacaoMatematica

os.system('cls')

a = float(input('Digite um número maior que 0 e menor q 11: '))
b = float(input('Digite outro número maior que 0 e menor q 11: '))

print('\nMenu: ')
print('1. Soma\n2. Subtração\n3. Produto\n4. Divisão\n5. Divisão inteira\n\
6. Resto da divisão')

opcao = input('\nEscolha uma das opções(1-6): ')
conta = OperacaoMatematica(a, b)

if opcao == '1':
    soma = conta.somar()
    print(f'A soma de {a} por {b} é: {soma:.2f}')

elif opcao == '2':
    subtracao = conta.subtrair()
    print(f'A subtração de {a} por {b} é: {subtracao:.2f}')

elif opcao == '3':
    multiplicacao = conta.multiplicar()
    print(f'O produto de {a} por {b} é: {multiplicacao:.2f}')

elif opcao == '4':
    divisao = conta.dividir()
    print(f'A divisão de {a} por {b} é: {divisao:.2f}')

elif opcao == '5':
    divisao_inteira = conta.divisao_inteira()
    print(f'A divisão inteira de {a} por {b} é: {divisao_inteira:.2f}')

elif opcao == '6':
    resto_divisao = conta.resto_da_divisao()
    print(f'O resto da divisão de {a} por {b} é: {resto_divisao:.2f}')