import os


os.system('cls')

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

while True:
    print('-'*70)
    comeco = input('Digite 1 para cadastrar e 0 para sair: ')

    if comeco == '1':
        nome = input('Digite seu nome: ')
        altura = float(input('Digite sua altura: '))
        peso = float(input('Digite seu peso: '))
        os.system('cls')
        num_alunos, media_altura, media_peso = media(nome, altura, peso)
        print('-'*70)
        print(f'Número de alunos: {num_alunos}')
        print(f'Média de altura: {media_altura:.2f}')
        print(f'Média de peso: {media_altura:.2f}')

    elif comeco == '0':
        break
    
    else:
        print(f'Opção inválida.')
        os.system('cls')