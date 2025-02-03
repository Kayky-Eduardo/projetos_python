import os

os.system('cls')

pessoas = []

while True:
    print('1. Cadastrar')
    print('2. procurar')
    print('3. Remover')
    print('4. mostrar cadastrados')
    print('5. sair')
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        nomes = input('Digite seu nome: ').lower()
        email = input('Insira seu email: ')
        idade = int(input('Digite sua idade: '))
        peso = float(input('Digite seu peso: '))

        cliente = {
            'Nomes': nomes,
            'email': email,
            'idade': idade,
            'peso': peso
            }
        pessoas.append(cliente)

    elif escolha == '2':
        procura_ad = input('Qual pessoa você deseja encontrar ')
        encontrou = False

        for usuario in pessoas:
            if usuario['Nomes'] == procura_ad.lower():
                print(f'Usuario encontrado: {usuario}')
                encontrou = True
        if not encontrou:
            print(f'Pessoa {procura_ad} não encontrada.\n')
    elif escolha == '3':
        procura_re = input('Qual pessoa você deseja remover: ')
        encontrou = False
        
        for nome in pessoas:
            if nome['Nomes'] == procura_re.lower():
                print('Usuario removido: ', nome)
                pessoas.remove(nome)
                encontrou = True
        if not encontrou:
            print(f'Pessoa {procura_re} não encontrada')
    elif escolha == '4':
        if pessoas:
            print('Cadastrados: ', pessoas)
        else:
            print('Não tem ninguém cadastrado.')
    elif escolha == '5':
        print('Saindo.')
        break