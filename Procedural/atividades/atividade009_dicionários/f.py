# f) Crie um programa que leia um dicionário com as seguintes informações:
# 'nome', 'idade', 'peso' e 'altura'. O dicionário será inicializado com os
# valores: 'nome': 'John', 'idade': 40, 'peso': 80 e 'altura': 1.70. O programa
# deverá realizar as seguintes ações: Primeiro, o programa deve listar todas
# as chaves e os respectivos valores do dicionário utilizando um laço de
# repetição. Em seguida, o programa deve excluir o item que contém o peso da
# pessoa, ou seja, a chave 'peso'. Após a exclusão, o programa deve listar
# novamente as chaves e valores restantes no dicionário. Por fim, o programa
# deverá exibir apenas o nome e a altura da pessoa, garantindo que o item
# 'peso' tenha sido removido corretamente.
import os


os.system('cls')

dicionario = {
    'nome': 'John',
    'idade': 40,
    'peso': 80,
    'altura': 1.70
}

for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')

del dicionario['peso']

print('\nApós a exclusão da chave "peso"')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')

print('\nApenas nome e altura.')
print(f'Nome: {dicionario["nome"]}, Altura: {dicionario["altura"]}')