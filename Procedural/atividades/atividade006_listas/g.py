#Ler uma lista com 10 números, depois apresente o maior e o menor número da lista
import os


os.system('cls')

lista = []

for num in range(10):
    entrada = int(input('Digite os números para serem adicionados na lista: '))
    lista.append(entrada)

lista.sort()
print(lista)
lista.reverse()
print(lista)