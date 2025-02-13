dicionario = {'Arthur':{'idade':30, 'genero': 'masculino'},
              'Kayky': {'idade':18, 'genero': 'masculino'},
              'Lorraine': {'idade': 56, 'genero': 'feminino'}}

def Checagem(nome):
    if nome in dicionario:
        print(f'{nome}: {dicionario[nome]}')
    else:
        print(f'Este nome não está presente no dicionário.')
