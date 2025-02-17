import os


os.system('cls')

# Inicialização do dicionário e da lista 
elementos = {} # Dicionário
periodica = [] # Lista

# Entrada de dados
for c in range(2):
    print(f'Entrada de dados {c + 1}: ')
    simbolo = str(input('Símbola do elemento: '))
    nome = str(input('Nome do elemento: '))

    # Adiciona os dados aos dicionário 
    elementos['simbolo'] = simbolo
    elementos['nome'] = nome

    # Usa append() com copy() para adicionar uma cópia do dicionário à lista
    periodica.append(elementos.copy())

print()
print('-'*70)
print('Elementos na tabala periódica')
print(periodica)
print('-'*70)
print()

# For aninhado para percorrer à lista e o dicionário
print('Detalhe dos elementos:')
for elemento in periodica: # Para cada elemento na lista
    for chave, valor in elemento.items(): # Para cada chave e valor do dicionário
        print(f'{chave.capitalize()}: {valor}') # Imprima a chave e o valor de maneira legível
    print('-'*70) # Linha separadora entre elementos