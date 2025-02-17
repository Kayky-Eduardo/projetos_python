import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE FOR RANGE')
print('='*70)

print()

for var_iteradora in range(1, 7):
    # end= coloca os números em uma mesma linha
    print(f'Valor: {var_iteradora}', end=' | ')

print()
print()

# OU

inicio = 1
fim = 7
passo = 2

for var_iteradora in range(inicio, fim, passo):
    print(f'Valor: {var_iteradora}', end=' | ')

print()
print()