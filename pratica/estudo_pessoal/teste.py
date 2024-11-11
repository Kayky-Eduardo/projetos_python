import os 

os.system('cls')


nome = input('Digite seu nome: ')
email = input('Digite seu e-mail: ')

if nome and email:   # se tiver preenchido
    pos_a = email.find('@')
    servidor = email[pos_a:]
    tamanho = len(servidor)
    if pos_a != -1 and '.' in servidor and tamanho >= 10:
        print('Cadastro concluído')
    else:
        print('Email inválido')
else:
    print('Digite seu nome e e-mail corretamente')