import os


os.system('cls')
from funcoes_usadas import lista_de_numeros

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separando o return em partes
(lista_par, quantidade_par,
lista_impar, quantidade_impar) = lista_de_numeros.Lista_de_numeros(lista)
print(f'Lista par: {lista_par}, quantidade de pares: {quantidade_par}')
print(f'Lista ímpar: {lista_impar}, quantidade de impares: {quantidade_impar}')

dicio = {1, 2, 3, 4, 5}

