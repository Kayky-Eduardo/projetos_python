import os


os.system('cls')
from funcoes_usadas import estados
dicionario = {
    'Amapá': 'macapá',
    'Amazonas': 'manaus',
    'Minas Gerais': 'belo horizonte',
    'São Paulo': 'são paulo',
    'Rio de Janeiro': 'rio de janeiro'
}


respostas = {}
for estado in dicionario.keys():
    respostas[estado] = input(f'Qual é a capital do estado {estado}? ').lower()

estados.checagem(respostas)
