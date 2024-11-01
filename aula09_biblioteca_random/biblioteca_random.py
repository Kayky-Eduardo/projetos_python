import os
import random


os.system('cls')

print('-'*70)
print('BIBLIOTECA RANDOM')
print('='*70)

print('Número aleatório')
numero_aleatorio = random.random()
print(f'O número gerado foi: {numero_aleatorio}')
print('.'*70)

print('Número aleatório inteiro')
aleatorio_inteiro = random.randint(1, 20)
print(f'O número inteiro gerado foi: {aleatorio_inteiro}')
print('.'*70)

print('Número aleatório decimal no intervalo')
aleatorio_decimal = random.uniform(1, 10)
print(f'O númeor decimal gerado foi: {aleatorio_decimal}')

print('Sorteio em uma lista')
lista = ['Ágata', 'Coly', 'Isis', 'Bia']
nome_sorteado = random.choice(lista)
print(f'Lista: {lista}')
print(f'O nome escolhido foi: {nome_sorteado}')
print('.'*70)

print('Embaralhar sequência')
lista2 = ['Ágata', 'Coly', 'Isis', 'Bia']
print(f'Lista antiga: {lista2}')
#embaralhado = list(random.shuffle(lista)) dá erro
#embaralhado = random.shuffle(lista) saída vazia
random.shuffle(lista2)
print(f'Lista nova: {lista2}')
print('.'*70)

print('Retorno de elementos únicos de uma população')
numeros = [1, 2, 3, 4, 5, 6, 7]
amostra_aleatoria = random.sample(numeros, 5)
print(f'Retorno da amostragem: {amostra_aleatoria}')
print('.'*70)