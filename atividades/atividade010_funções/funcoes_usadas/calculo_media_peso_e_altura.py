dicionario = {}

def media(nome, altura, peso):
    dicionario[nome] = {'Altura': altura, 'Peso': peso}
    lista_altura = []
    lista_peso = []
    for j in dicionario.values():
        lista_altura.append(j['Altura'])
        lista_peso.append(j['Peso'])
    
    soma_altura = 0
    soma_peso = 0
    for i in lista_altura:
        soma_altura += i
    for i in lista_peso:
        soma_peso += i

    media_altura = soma_altura / len(dicionario)
    media_peso = soma_peso/ len(dicionario)
    num_alunos = len(dicionario)
    return num_alunos, media_altura, media_peso
