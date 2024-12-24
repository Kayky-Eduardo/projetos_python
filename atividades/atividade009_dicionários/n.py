# n) Crie um programa para cadastrar produtos em uma loja, incluindo nome, preço
# e categoria. O programa deve permitir que o usuário insira pelo menos 5
# produtos e aplicar descontos a esses produtos. Além disso, o programa deve
# permitir a alteração do preço de qualquer produto. Após o cadastro, o programa
# deve exibir todos os produtos com seus preços, ordenados por nome, e gerar um
# relatório que informe quantos produtos estão com preço inferior a R$50,00 após
# o desconto e quantos pertencem à categoria "Eletrônicos".
import os


os.system('cls')


produtos = {}


while True:
    print('-'*70)
    print('1. Registrar produto.')
    print('2. Alterar dado de um produto')
    print('3. Relatório.')
    print('4. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        os.system('cls')
        nome = input('Digite o nome do produto: ').capitalize()
        preco = float(input('Insira o valor do produto: '))
        categoria = input('Digite a categoria do produto: ')
        produtos[nome] = {'Preço': preco, 'Categoria': categoria,
                          'Desconto': 0.0}
        pergunta_desconto = input('Deseja adicionar desconto(s/n): ').lower()
        if pergunta_desconto == 's':
            desconto = float(input('Insira o valor do desconto: '))
            produtos[nome]['Desconto'] = desconto
        else:
            continue
        print('Produtos cadastrados.')
        for h, l in sorted(produtos.items()):
            print(f'{h}: {l}')
        
    elif opcao == '2':
        os.system('cls')
        if produtos:
            print('Produtos cadastrados:')
            for i, j in sorted(produtos.items()):
                print(f'{i}: {j}')
                print('-'*70)
            escolher = input('Qual produto deseja escolher: ').capitalize()
            if escolher in produtos:
                print(f'item selecionado:\n{escolher}: {produtos[escolher]}')
                mudar = input('O que deseja mudar: ').capitalize()
                if mudar in produtos[escolher]:
                    if mudar == 'Preço':
                        novo_preco = float(input('Digite o novo preço: '))
                        produtos[escolher]['Preço'] = novo_preco
                        print('Mudança feita.')
                    elif mudar == 'Categoria':
                        nova_categ = input('Digite a nova '
                                           'categoria: ').capitalize()
                        produtos[escolher]['Categoria'] = nova_categ
                        print('Mudança feita.')
                    elif mudar == 'Desconto':
                        novo_desc = float(input('Digite o novo desconto: '))
                        produtos[escolher]['Desconto'] = novo_desc
                        print('Mudança feita.')
                else:
                    print('Opção não encontrada.')
            else:
                print('Este item não está cadastrado.')
        else:
            print('Não temos nada cadastrado ainda.')
        
    elif opcao == '3':
        contagem = 0
        contagem_elet = 0
        for valor, dados in sorted(produtos.items()):
            apos_desconto = (dados['Preço'] * (1 - dados['Desconto']/100))
            if apos_desconto < 50:
                    contagem += 1
            if dados['Categoria'] == 'Eletrônicos':
                contagem_elet += 1
        print(f'{contagem} produto(s) possuem preço menor que R$50,00 após o '
              'desconto')
        print(f'{contagem_elet} produto(s) tem Eletrônico como categoria.')
        
    elif opcao == '4':
        print('Saindo...')
        break