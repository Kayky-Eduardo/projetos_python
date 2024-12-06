import os


os.system('cls')

print('ESTRUTURA DE DADOS: DICIONÁRIO')

# Indices iguais: só irá exibir um item.
dicionario1 = {'nome': 'john', 'nome':'jane'}

# Posso ter uma tupla como índice e uma lista como valor
dicionario2 = {(1, 2) : [1, 2]}

# Mas não posso ter uma lista como índice e uma tupla como valor
dicionario3 = {[1, 2] : (1, 2)}

# Saída
print(dicionario1)
print(dicionario2)

print()