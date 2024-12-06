# import os


# os.system('cls')
# lista = []
# while True:
#     print('1. Adicionar')
#     print('2. procurar')
#     print('3. sair')
#     procura = input('Deseja procurar? ')
#     if procura == '2':
#         nome_proc = input('Qual chave? ')
#         for nome in lista:
#             encontrou = False
#             if nome[chaves] == nome_proc.lower():
#                 print('Usuario encontrado: ', nome)
#                 encontrou = True
#         if not encontrou:
#             print(f'Pessoa {nome_proc} não encontrada')
#     if procura == '1':
#         chaves = input("Digite as chaves: ")
#         valor_padrao = input("Digite o valor: ")
#         meu_dicionario = dict.fromkeys(chaves, valor_padrao)
#         lista.append(meu_dicionario)
#         print(lista)
#     if procura == '3':
#         break

dicio = {'chave': 10,
        'valor': 20}

pegando = dicio.items()

print(pegando)