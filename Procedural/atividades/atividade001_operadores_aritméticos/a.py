#importando a biblioteca
import os

#limpar o terminal
os.system('cls')

#entrada
print()
print('-'*70)
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))
print('-'*70)

#processamento
soma = valor1 + valor2 + valor3
multiplicacao = valor1 * valor2 * valor3

#saída
print('======RESULTADOS======')
print(f'A soma dos valores é {soma}')
print(f'A multiplicação dos valores é igual a {multiplicacao}')