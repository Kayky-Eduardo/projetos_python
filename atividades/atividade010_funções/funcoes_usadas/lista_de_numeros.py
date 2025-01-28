def Lista_de_numeros(numeros):
    lista_par = []
    lista_impar = []  
    for i in numeros:
        if i % 2 != 0:
            lista_impar.append(i)
        else:
            lista_par.append(i)  
    return lista_par, len(lista_par), lista_impar, len(lista_impar)
