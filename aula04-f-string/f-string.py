import os

import datetime

os.system('cls')

print('-'*70)
print('ENTRADA DE DADOS EM PYTHON')
print('='*70)

nome = input('Entre com um nome: ')
peso = input('Entre com o peso: ')
altura = input('Entre com a altura: ')

nascimento = int(input('Data de nascimento: '))
cep = int(input('Entre com o seu CEP: '))
bairro = str(input('Entre como Bairro: '))
rua = str(input('Nome da Rua: '))
numero = int(input('Entre com o número: '))

ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

#saida
print('-'*70)
print('SAÍDA DE DADOS')
print('='*70)
print('Nome..............:', nome)
print('Data de nascimento: ', nascimento)
print('Peso..............:', peso)
print('Altura............:', altura)

#saída interpolada
print(f'{nome}, você tem {idade} anos!')
print(f'CEP..............: {cep}')
print(f'Bairro...........: {rua}')
print(f'rua..............: {numero}')
print('-'*70)
print('')