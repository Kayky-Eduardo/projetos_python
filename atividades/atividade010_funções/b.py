import os


os.system('cls')

def cadastro(nome, matricula, data_de_nascimento):
    dicionario[nome] = {'matricula':matricula,
                        'data_de_nascimento':data_de_nascimento}




dicionario = dict(nome= 'Arthur', matricula= 20, data_de_nascimento= 60.5)
cadastro('Kayky', 102030, '10/10/2010')
for i, j in dicionario.items():
    print(f'{i} : {j}')