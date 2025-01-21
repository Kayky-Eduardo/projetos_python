import os


os.system('cls')

dicionario = {'Arthur':{'idade':30, 'genero': 'masculino'},
              'Kayky': {'idade':18, 'genero': 'masculino'},
              'lorraine': {'idade': 56, 'genero': 'feminino'}}

def checagem(nome):
    if nome in dicionario:
        print(nome, dicionario[nome])

checagem('Kayky')