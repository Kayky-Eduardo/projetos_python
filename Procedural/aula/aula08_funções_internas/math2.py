import math
import os


os.system('cls')

print('ESTUDO DA BIBLIOTECA MATEMÁTICA MATH')

#Entrada de Dados
numero_decimal = float(input('Entre com um número decimal: '))

#processamento
arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math.floor(numero_decimal)

#Saída
print(f'O número {numero_decimal} arredondado para cima é: '
      f'{arredondar_para_cima}')
print(f'O número {numero_decimal} arredondado para baixo é: ' 
      f'{arredondar_para_baixo}')
print()