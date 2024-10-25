#importando as bibliotecas
import os
import datetime

#limpando o terminal
os.system('cls')

#entrando
ano_de_nascimento = int(input('Digite o seu ano de nascimento: '))

ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - ano_de_nascimento

#saída
print()
print('='*70)
print(f'sua idade atual é: {idade}')
print('='*70)