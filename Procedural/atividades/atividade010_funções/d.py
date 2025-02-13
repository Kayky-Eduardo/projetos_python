import os


os.system('cls')

from funcoes_usadas import conversao

valor_da_temperatura = float(input('Digite a temperatura: '))
tipo_temp = input('O valor está em fahrenheit ou célsius: ')
conversao.Temperatura(valor_da_temperatura, tipo_temp)