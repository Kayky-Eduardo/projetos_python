#importando a biblioteca
import os

#limpando o terminal
os.system('cls')

#entrada
número = float(input('Digite o seu número: '))

#processamento
dobro = número * 2
triplo = número * 3

#saida
print(f'O dobro de {número} é: {dobro}')
print(f'O triplo de {número} é: {triplo}')