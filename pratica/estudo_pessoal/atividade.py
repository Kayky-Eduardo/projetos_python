import os


os.system('cls')


produtos = {}


while True:
    print('-'*70)
    print('1. Registrar produto.')
    print('2. Aplicar desconto.')
    print('3. Alterar dado de um produto')
    print('4. Relatório.')
    print('5. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        os.system('cls')
        nome = input('Digite o nome do produto: ').capitalize()
        preco = float(input('Insira o valor do produto: '))
        categoria = input('Digite a categoria do produto: ')
        produtos[nome] = {'Preço': preco, 'Categoria': categoria}
        pergunta_desconto = input('Deseja adicionar desconto(s/n): ')
        if pergunta_desconto == 's':
            desconto = float(input('Insira o valor do desconto'))
        
    elif opcao == '3':
        os.system('cls')
        if produtos:
            print('Produtos cadastrados:')
            for i, j in produtos.items():
                print(f'{i}: {j}')
                print('-'*70)
            escolher = input('Qual produto deseja escolher: ').capitalize()
            if escolher in produtos:
                print(f'Produto selecionado {escolher}: {produtos[escolher]}')
                mudar = input('O que deseja mudar: ').capitalize()
                if mudar in produtos[escolher]:
                    if mudar != categoria:
                        novo_valor = float(input('Insira o novo dado: '))
                        produtos[escolher][mudar] = novo_valor
                    else:
                        nova_categ = input('Insira a categoria: ')
                        produtos[escolher][mudar] = nova_categ    