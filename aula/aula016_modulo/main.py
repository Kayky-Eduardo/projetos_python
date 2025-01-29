import os

from pacote.subpacote.mutiplicar import mutiplicar
from pacote.divisao import dividir
from pacote.soma import somar

while True:
    os.system('cls')
    
    a = input('Entre com o valor de A: ')
    b = input('Entre com o valor de B: ')

    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        print(f'Por favor, entre com um número válido')
        continue

    a = float(a)
    b = float(b)

    resultado_soma = somar(a, b)
    resultado_produto = mutiplicar(a, b)
    resultado_divisao, erro = dividir(a, b)

    print('-'*70)
    print('CALCULOS MATEMÁTICOS')
    print('='*70)
    print(f'Cálculo da soma: {resultado_soma}')
    print(f'Cálculo do produto: {resultado_produto}')
    print(f'Cálculo da divisão: {resultado_divisao}, {erro}')
    print('-'*70)

    sair = input('Deseja sair do programa? (s/n): ').strip().lower()
    
    if sair == 's':
        print('Saindo...')
        break
