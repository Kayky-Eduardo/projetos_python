# Faça um programa para criar um dicionário com pelo menos 4 elementos.
# O programa deve permitir que o usuário insira as chaves e os valores.
# As chaves devem ser únicas, e o programa deve garantir isso. Após 
# inserir todos os elementos, o programa deve exibir o dicionário ordenado
# pela chaves.
import os


os.system('cls')

dicio = {'Cor': 'Pardo',
         'Nome': 'Kayky',
         'Idade': 18,
         'Cabelo': 'Ondulado'
         }

for i in range(1, 5):
    chave = input('Escolha uma chave: ')
    if chave in dicio:
        print('Essa chave já está no dicionário.')
    else:
        valor = input('Dê um valor para a chave: ')
        dicio[chave] = valor
        input('Enter para continuar...')
        os.system('cls')

for i, j in sorted(dicio.items()):
    print(f'{i}: {j}')