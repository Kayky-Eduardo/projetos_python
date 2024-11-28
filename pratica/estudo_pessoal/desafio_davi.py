# Caixa do walmart
import os


os.system('cls')
compra = 0
itens_walmart = [
    {"preco": 19.99, "itens": "Arroz"},
    {"preco": 8.50, "itens": "Feijão"},
    {"preco": 5.90, "itens": "Coca-Cola"},
    {"preco": 29.99, "itens": "Camiseta"},
    {"preco": 12.50, "itens": "Caderno"},
    {"preco": 2499.00, "itens": "Notebook"},
    {"preco": 15.99, "itens": "Lâmpada LED"},
    {"preco": 7.90, "itens": "Sabão em pó"},
    {"preco": 1599.99, "itens": "Smartphone"},
    {"preco": 89.90, "itens": "Óculos de sol"}
]
while True:
    print('Próximo cliente.')
    print('1. Procurar item.')
    print('2. Sair. ')
    resposta = input('Qual opção deseja escolher: ')
    
    if resposta == '1':
        qntd_prod = int(input('Quantos itens: '))
    
    for i in range(qntd_prod):
        if resposta == '1':
            procura = float(input('Qual o preço do item você deseja '
                                  'encontrar: '))
        for itens in itens_walmart:
            if itens['preco'] == procura:
                print('Encontrou o item: ', itens)
                compra += procura
        else:
            print('Não encontrado!')
    print(f'O preço da compra foi: R${compra}')
    
    print('1. Dinheiro')
    print('2. Pix (25% de desconto). ')
    print('3. Cartão.')
    resposta = input('Qual opção deseja escolher: ')
    
    if resposta == '1':
        pagamento = float(input('Pagamento: '))
        troco = pagamento - compra
        print(f'O seu troco é: {troco}')
    elif resposta == '2':
        print('Insira o cartão.')
        cartao = int(input('Senha do cartão: '))
        if len(cartao) >= 4 or len(cartao) <= 6:
            print('Obrigado, volte sempre!')
    if resposta == '2':
        print('Saindo...')
        break