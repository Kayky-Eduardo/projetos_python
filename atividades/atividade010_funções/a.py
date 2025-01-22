import os


os.system('cls')


def lista_de_numeros(numeros):
    lista_par = []
    lista_impar = []  
    for i in numeros:
        if i % 2 != 0:
            lista_impar.append(i)
        else:
            lista_par.append(i)  
    return lista_par, len(lista_par), lista_impar, len(lista_impar)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separando o return em partes
(lista_par, quantidade_par,
lista_impar, quantidade_impar) = lista_de_numeros(lista)
print(f'Lista par: {lista_par}, quantidade de pares: {quantidade_par}')
print(f'Lista ímpar: {lista_impar}, quantidade de impares: {quantidade_impar}')