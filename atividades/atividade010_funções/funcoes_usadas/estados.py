dicionario = {
    'Amapá': 'macapá',
    'Amazonas': 'manaus',
    'Minas Gerais': 'belo horizonte',
    'São Paulo': 'são paulo',
    'Rio de Janeiro': 'rio de janeiro'
}

def checagem(respostas):
    respostas_certas = 0

    for estado, capital_correta in dicionario.items():
        resposta = respostas.get(estado)
        if resposta == capital_correta:
            print(f'Você acertou a capital de {estado}!')
            respostas_certas += 1
        else:
            print(f'Você errou! A capital de {estado} é {capital_correta}.')
            print(f'Número total de respostas corretas antes da resposta '
                  f'errada: {respostas_certas}')
            return  
        
    print(f'Número de respostas certas: {respostas_certas}')
