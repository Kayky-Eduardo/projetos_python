#g) Desenvolva um programa que manipule um dicionário com informações de uma
# pessoa, contendo as chaves 'nome', 'idade', 'peso' e 'altura', com valores
# iniciais: 'nome': 'John', 'idade': 40, 'peso': 80 e 'altura': 1.70. O
# programa deve permitir que o usuário escolha ações através de um menu
# interativo, como listar todas as chaves e valores, alterar o valor de uma
# chave, excluir um item específico e exibir apenas o nome e a altura. Além
# disso, o programa deve garantir que as exclusões sejam feitas somente se a
# chave existir e permitir alterações nos valores. Após as modificações, o
# programa deve listar o dicionário atualizado e gerar um relatório final,
# indicando a quantidade de dados restantes e mostrando o estado atual das
# chaves e valores.
import os


os.system('cls')

dicionario = {
    'nome': 'John',
    'idade': 40,
    'peso': 80,
    'altura': 1.70
}

while True:
    print('-'*70)
    print('1. Listar todos os valores e chaves')
    print('2. Alterar valor de uma chave')
    print('3. Excluir um item em específico')
    print('4. Exibir apenas nome e altura')
    print('5. Relatório final\n')
    
    opcao = input('Escolha uma das opções: ')
    
    if opcao == '1':
        os.system('cls')
        for chave, valor in dicionario.items():
            print(f'{chave}: {valor}')
        
    elif opcao == '2':
        mudar = input('Qual chave você deseja trocar o valor: ')
        if mudar in dicionario:
            novo_valor = input('Digite o valor que você deseja colocar: ')
            dicionario[mudar] = novo_valor
            print('Mudança feita.')
        else:
            print('Chave não encontrada')
    
    elif opcao == '3':
        excluir = input('Qual digite a chave do item que deseja excluir: ')
        if excluir in dicionario:
            del dicionario[excluir]
            print(f'Item excluído')
        else:
            print(f'Item não encontrado')
            
    elif opcao == '4':
        os.system('cls')
        if 'nome' in dicionario:
            print(f'Nome: {dicionario["nome"]}')
        else:
            print(f'A chave nome foi excluida.')
        if 'altura' in dicionario:
            print(f'Altura: {dicionario["altura"]}')
        else:
            print('A chave altura foi excluida')
            
    elif opcao == '5':
        os.system('cls')
        print(f'O dicionário possui {len(dicionario)} dados')
        print('Estado final do dicionário:\n')
        for chave, valor in dicionario.items():
            print(f'{chave}: {valor}')
        break