#biblioteca
import os

#limpeza do terminal
os.system('cls')

#Entrada
valor1 = float(input('Digite o valor da altura: '))
valor2 = float(input('Digite o valor da base..: '))

#processamento
perímetro = valor1 * 2 + valor2 * 2

#Saída
print('='*70)
print(f'O perímetro do retângulo é: {perímetro}')
print('='*70)
print()