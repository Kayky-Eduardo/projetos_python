#Desenvolva um programa para gerenciar o estoque de uma loja. O programa
#deve permitir que o usuário cadastre produtos, onde cada produto terá nome,
#quantidade em estoque e preço unitário. O programa deve possibilitar a 
#alteração da quantidade de um produto e a exclusão de um produto do estoque.
#Após a inserção de pelo menos 5 produtos, o programa deve exibir todos
#os produtos cadastrados, ordenados por nome, e gerar um relatório que 
#informe o valor total do estoque, levando em consideração a quantidade e o
#preço de cada produto.
import os


os.system('cls')

produtos = {}

while True:
    print('-'*70)
    print('1. Cadastrar produto no estoque.')
    print('2. Alteração de dados do produto.')
    print('3. Excluir produto do estoque.')
    print('4. Listar os produtos.')
    print('5. Relatório.')
    print('6. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        os.system('cls')
        nome_produto = input('Digite o produto: ')
        qntd_estoque = float(input('Digite a quantidade em estoque: '))
        preco_uni = float(input('Digite o preço unitário do produto: '))
        produtos[nome_produto] = {'Quantidade em estoque': qntd_estoque,
                                  'Preço unitário': preco_uni}
    
    elif opcao == '2':
        if produtos:
            os.system('cls')
            print('Produtos em estoque:\n')
            for i, j in produtos.items():
                print(f'{i}: {j}')
            escolher = input('Qual produto deseja selecionar: ')
            os.system('cls')
            if escolher in produtos:
                print(f'Produto selecionado: {produtos[escolher]}')
                mudar = input('Oque deseja mudar: ').capitalize()
                if mudar in produtos[escolher]:
                    novo = input('Insira o valor desejado: ')
                    if mudar == 'Quantidade em estoque':
                        produtos[escolher][mudar] = int(novo)
                    else:
                        produtos[escolher][mudar] = float(novo)
                else:
                    print('Não encontrado.')
            else:
                print('Não encontrado.')
                    
    elif opcao == '3':
        excluir = input('Digite o nome do produto que deseja excluir: ')
        if excluir in produtos:
            del produtos[excluir]
    
    elif opcao == '4':
        if produtos:
            os.system('cls')
            for produto, valor in sorted(produtos.items()):
                print(f'Nome do produto: {produto}\nQuantidade em estoque: '
                    f'{valor["Quantidade em estoque"]}\nPreço unitário: '
                    f'{valor["Preço unitário"]}')
                print('='*70)
        else:
            print('Estoque vázio.')
    
    elif opcao == '5':
        if len(produtos) >= 5:
            valor_total = 0
            for valores in produtos.values():
                valor_total += (valores['Quantidade em estoque'] *
                valores['Preço unitário'])
            print(f'Valor total do estoque: {valor_total:.2f}')
        else:
            print('Faça o cadastro de pelo menos 5 produtos.')
    
    elif opcao == '6':
        print('Saindo...')
        break