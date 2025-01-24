import os


os.system('cls')

def Receber_listas(lista1, lista2):
    dicionario = {}
    for i in range(len(lista1)):
        # Vai pegar cada indice e transformar em chave: valor
        dicionario[lista1[i]] = lista2[i]
        
    return dicionario

lista1 = ['nome', 'peso', 'idade']
lista2 = ['john', 40, 18]

dicionario = Receber_listas(lista1, lista2)

print('Dicionário:')
for i, j in dicionario.items():
    print(f'{i}: {j}')