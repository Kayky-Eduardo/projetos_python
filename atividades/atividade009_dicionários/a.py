# Faça um programa para criar um dicionário com pelo menos 4 elementos.
# O programa deve permitir que o usuário insira as chaves e os valores.
# As chaves devem ser únicas, e o programa deve garantir isso. Após 
# inserir todos os elementos, o programa deve exibir o dicionário ordenado
# pela chaves.
import os


os.system('cls')

dicio = {}

for i in range(1, 5):
    chave = input('Escolha uma chave: ')
    valor = input('Dê um valor para a chave: ')
    dicio[chave] = valor

print(dicio)