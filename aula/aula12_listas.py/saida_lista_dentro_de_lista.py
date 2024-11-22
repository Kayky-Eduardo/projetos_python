import os

os.system('cls') 

print('-' * 70)
print('VARRENDO LISTAS DENTRO DE LISTAS')
print('-' * 70)

# X O X
# X X O
# O O O

#  Similar a um array de 3 Dimensões
jogo_velha = [
                #0     1    2  
                ['X', 'O', 'X'], #0
                ['X', 'X', 'O'], #1
                ['O', 'O', 'O']  #2
]

print(jogo_velha)
print()

# pegando manualmente os valores
print(f'Na linha 1 coluna 1, existe um: {jogo_velha[1][1]}')
print(f'Na linha 0 coluna 2, existe um: {jogo_velha[0][2]}')

print()
# varrendo com for range
for linha in range(0, len(jogo_velha)):
    for coluna in range(0, len(jogo_velha)):
        print(jogo_velha[linha][coluna], end= ' ')
    print()
print()