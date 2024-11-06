import os

os.system('cls')

print('='*70)
print('Estudo de Condicional: Parte 1')

#entrada
numero = float(input('Digite um número: '))
resposta = ''

#condicional
if numero % 2 == 0:
    resposta = f'O número {numero} é par'
else:
    resposta = f'O número {numero} é ímpar'
    
#Saída
print('='*70)
print(resposta)
print('Fim do programa!\n') #\n salta uma linha