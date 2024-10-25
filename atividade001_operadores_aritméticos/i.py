#import da biblioteca
import os

#limpeza do terminal
os.system('cls')

#entrada
valor = float(input('digite o valor: '))

#processamento
valor_em_dolares = valor * 5.71

#saida
print(f'R${valor} reais é igual: US${valor_em_dolares} dolares')