#1. Cadastro de CPF
#Crie um programa para cadastro de CPF de clientes que recebe
#clientes que recebe o CPF em um input box apenas com números.
import os
import math

os.system('cls')

cpf = input('digite o CPF: ')
cortar_cpf = cpf.strip()
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
cpf = cpf.replace(' ', '')

if cpf.isnumeric() and len(cpf) == 11:
    print(cpf)
else:
    print('Digite seu CPF corretamente.')