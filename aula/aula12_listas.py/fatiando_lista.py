import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: LISTAS [ ]')
print('='*70)

lista_mista = ['a', 'b', 3, 'John', 'e', 500, 'g', 'h']

# Fatia o 1º elemento
lista_fatiado1 = lista_mista[0]
# Fatia todos os elementos
lista_fatiado2 = lista_mista[0:]
# Fatia os elementos do índice 0 até o índicie 6
lista_fatiado3 = lista_mista[0:7]
# Fatia os elementos do índice 0 até o índice 6 de 2 em 2
lista_fatiado4 = lista_mista[0:7:2]
# Fatia os elementos da direita para esquerda
lista_fatiado5 = lista_mista[::-1]

print(f'Fatiando uma Lista: {lista_fatiado1}\n')
print(f'Fatiando uma Lista: {lista_fatiado2}\n')
print(f'Fatiando uma Lista: {lista_fatiado3}\n')
print(f'Fatiando uma Lista: {lista_fatiado4}\n')
print(f'Fatiando uma Lista: {lista_fatiado5}')

print('-'*70)
print('Fim do programa!')
print('-'*70)