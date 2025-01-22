import os


os.system('cls')

def Soma(a, b):
    soma = a + b
    return soma

def Subtracao(a, b):
    subtracao = a - b
    return subtracao

def Produto(a, b):
    produto = a * b
    return produto

def Divisao(a, b):
    divisao = a / b
    return divisao

def Divisao_inteira(a, b):
    divisao_inteira = a // b
    return divisao_inteira

def Resto_da_divisao(a, b):
    resto_da_divisao = a % b
    return resto_da_divisao



a = float(input('Digite um número maior que 0 e menor q 11: '))
b = float(input('Digite outro número maior que 0 e menor q 11: '))

print('\nMenu: ')
print('1. Soma\n2. Subtração\n3. Produto\n4. Divisão\n5. Divisão inteira\n\
6. Resto da divisão')

opcao = input('\nEscolha uma das opções(1-6): ')

if opcao == '1':
    print(f'A soma de {a} por {b} é: {Soma(a, b):.2f}')

elif opcao == '2':
    print(f'A subtração de {a} por {b} é: {Subtracao(a, b):.2f}')

elif opcao == '3':
    print(f'O produto de {a} por {b} é: {Produto(a, b):.2f}')

elif opcao == '4':
    print(f'A divisão de {a} por {b} é: {Divisao(a, b):.2f}')

elif opcao == '5':
    print(f'A divisão inteira de {a} por {b} é: {Divisao_inteira(a, b):.2f}')

elif opcao == '6':
    print(f'O resto da divisão de {a} por {b} é: {Resto_da_divisao(a, b):.2f}')