import os


os.system('cls')

from funcoes_usadas import calculo_imc
altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso em kg: '))

print(f'O seu IMC é de {calculo_imc.Calcular_imc(altura, peso):.2f}')