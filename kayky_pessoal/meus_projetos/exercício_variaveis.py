import os

os.system('cls')

#entrada
nome = str(input('Entre com um nome: '))
idade = int(input('Entre com a idade: '))
peso = float(input('Entre com o peso: '))
altura = float(input('Entre com a altura: '))

#saida
print()
print('='*70)
if idade <=18:
    print(f'{idade}, precisa amadurecer!')
else:
    print(f'{idade}, tá velho demais')

print(f'{nome}, você é homosexual!')

if peso >=75:
    print(f'{peso}, tá gordo!')
else:
    print(f'{peso}, esquelético!')
if altura <=1.80:
    print(f'{altura}, cresça e apareça!')
else:
    print(f'{altura}m, tamanho desnecessário!')
print('='*70)