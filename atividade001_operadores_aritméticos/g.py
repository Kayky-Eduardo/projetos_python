#biblioteca
import os

#limpeza do terminal
os.system('cls')

#Entrada
valor = float(input('Digite o valor: '))

#processamento
valor_cm = valor * 100
valor_mm = valor * 10

#saida
print()
print(f' {valor}m em centímetros é: {valor_cm}')
print(f' {valor}m em milímetros é: {valor_mm}')