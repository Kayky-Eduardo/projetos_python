def Receber_listas(lista1, lista2):
    dicionario = {}
    for i in range(len(lista1)):
        # Vai pegar cada indice e transformar em chave: valor
        dicionario[lista1[i]] = lista2[i]
        
    return