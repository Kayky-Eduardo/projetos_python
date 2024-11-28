import os


os.system('cls')

nomes = []

while True:
    print('1. Cadastrar cliente: ')
    print('2. Procurar cliente: ')
    print('3. Sair. ')
    resposta = input('Qual opção deseja escolher: ')
    
    if resposta == '1':
        nome = input('Nome: ').lower().replace(' ', '')
        email = input('Email: ')
        peso = float(input('Peso: '))
        
        cliente = {
            'Nome': nome,
            'Email': email,
            'Peso': peso
        }
        nomes.append(cliente)
        
    elif resposta == '2':
        procura = input('Qual pessoa você deseja encontrar ')
        
        encontrou = False
        
        for usuario in nomes:
            if usuario['Nome'] == procura.lower():
                print('Encontrou o usuario: ', usuario)
                encontrou = True
                break
        if not encontrou:
            print(f'Pessoa {procura} não encontrada.\n')
    elif resposta == '3':
        print('Saindo...')
        break
    else:
        print('Opção invalida, tente novamente!')