import os
os.system('cls')

print('-'*70)
print('OPERADORES ARITMÉTICOS')
print('='*70)

#entrada
print('--- SOMA')
print('-'*70)
parcela_1 = float(input('Entre com a 1ª parcela: '))
parcela_2 = float(input('Entre com a 2ª parcela: '))

print()
print('--- SUBTRAÇÃO')
print('-'*70)
minuendo = float(input('Entre com oo minuedo: '))
subtraendo = float(input('Entre com a subtraendo: '))

print()
print('--- PRODUTO')
print('-'*70)
multiplicando = float(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicador: '))

print()
print('--- DIVISÃO')
print('-'*70)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

print()
print('---RAIZ QUADRADA')
print('-'*70)
radicando_quadrado = float(input('Entre com o valor da raiz quadrada: '))

print()
print('--- RAIZ CÚBICA')
print('-'*70)
radicando_cúbico = float(input('Entre com o valor da raiz cúbica: '))

#processamento
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz_quadrada = radicando_quadrado **(1/2)
raiz_cúbica = radicando_cúbico **(1/3)

#saida
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} = {subtraendo} é: {diferenca}')
print(f'A multiplicação de {multiplicando} x {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} ÷ {divisor} é: {quociente}')
print(f'A raiz quadrada de {radicando_quadrado} é: {raiz_quadrada}')
print(f'A raiz cúbica de {radicando_cúbico} é: {raiz_cúbica}')