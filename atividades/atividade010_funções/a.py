import os


os.system('cls')


def lista_de_numeros(lista):
    lista_par = []
    lista_impar = []  
    for i in lista:
        if i % 2 != 0:
            lista_impar.append(i)
        else:
            lista_par.append(i)  
    print(lista_impar)
    print(lista_par)
    print(f'Quantidade números pares: {len(lista_par)}')
    print(f'Quantidade números impares: {len(lista_impar)}')

    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_numeros(lista)
