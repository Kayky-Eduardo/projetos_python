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
if idade < 18:
    print(f'{idade}, Idade insuficiente!')
else:
    print(f'{idade}, Idade aprovada!')

print(f'{nome}, Aprovado!')

if peso >=75:
    print(f'{peso}, É necessário uma dieta, para o emagrecimento!')
else:
    print(f'{peso}, É necessário o aumento de peso!')
if altura <=1.80:
    print(f'{altura}m, Altura insuficiente!')
else:
    print(f'{altura}m, Altura suficiente!')
print('='*70)