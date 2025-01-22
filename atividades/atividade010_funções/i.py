import os


os.system('cls')

# Incompleto
dicionario = {'Amapá': 'macapá', 'Amazonas': 'manaus',
              'Minas Gerais': 'belo horizonte', 'São Paulo': 'são paulo',
              'Rio de Janeiro': 'rio de janeiro'}
def checagem(amapa, amazonas, minas_gerais, sao_paulo, rio_de_janeiro):
    os.system('cls')
    lista = [amapa, amazonas, minas_gerais, sao_paulo, rio_de_janeiro]
    respostas_certas = 0
    for i in dicionario.values():
        for j in lista:
            if i != j:
                continue
            else:
                print(f'Voce acertou a capital de {i}')
            # if i == j:
            #     print(f'Você acertou a Capital de {i}')
            #     respostas_certas += 1
            #     continue
            # else:
            #     print(f'Você errou a capital de {i}!')
            #     break
        break
    print(f'Número de respostas certas: {respostas_certas}')
    

amapa = input('Qual é a capital do Estado de Amapá: ').lower()
amazonas = input('Qual é a capital do Estado de Amazonas: ').lower()
minas_gerais = input('Qual é a capital do Estado de Minas Gerais: ').lower()
sao_paulo = input('Qual é a capital do Estado de São Paulo: ').lower()
rio_de_janeiro = input('Qual é a capital do Estado de Rio de \
Janeiro: ').lower()

lista = [amapa, amazonas, minas_gerais, sao_paulo, rio_de_janeiro]
checagem(amapa, amazonas, minas_gerais, sao_paulo, rio_de_janeiro)