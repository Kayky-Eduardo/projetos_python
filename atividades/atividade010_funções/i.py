import os


os.system('cls')

dicionario = {
    'Amapá': 'macapá',
    'Amazonas': 'manaus',
    'Minas Gerais': 'belo horizonte',
    'São Paulo': 'são paulo',
    'Rio de Janeiro': 'rio de janeiro'
}

# def checagem(respostas):
#     os.system('cls')
#     respostas_certas = 0

#     for estado, capital_correta in dicionario.items():
#         resposta = respostas.get(estado)
#         if resposta == capital_correta:
#             print(f'Você acertou a capital de {estado}!')
#             respostas_certas += 1
#         else:
#             print(f'Você errou! A capital de {estado} é {capital_correta}.')
#             print(f'Número total de respostas corretas antes da resposta '
#                   f'errada: {respostas_certas}')
#             return  
        
#     print(f'Número de respostas certas: {respostas_certas}')

# respostas = {}
# for estado in dicionario.keys():
#     respostas[estado] = input(f'Qual é a capital do estado {estado}? ').lower()


def checagem(respostas):

    for i, j in dicionario.items():
        resposta = respostas.get(i)
        if resposta == j:
            print(f'Você acertou a capital de {i}')
        else:
            print(f'Você errou a capital de {i}')
            return

respostas = {}    
for i in dicionario.keys():
    respostas[i] = input(f'Capital de {i}: ').lower()

checagem(respostas)
