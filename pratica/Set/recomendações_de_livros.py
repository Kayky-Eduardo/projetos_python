import os


os.system('cls')

pessoa1 = {'1984', 'Missão impossível', 'Massacre da serra eletrica', 'Ursionho Pooh: Sangue e Mel', 'Sharknado'}
pessoa2 = {'1984', 'Velozes e Furiosos', 'Circulo de Fogo', 'O pianista', 'Gladiador', 'Sharknado'}

# Todos os filmes
uniao = pessoa1.union(pessoa2)
print(f'Todos os filmes: {uniao}\n')


print('Escolha o tipo de recomendação:')
print('1 - Filmes recomendados para o usuário 1 (não assistidos por ele, mas assistidos por 2)')
print('2 - Filmes que ambos assistiram')

opcao = input('Qual opção deseja escolher: ')

if opcao == '1':
    # Recomendações
    recomendacao = pessoa2.difference(pessoa1)
    print(f'Recomendações: {recomendacao}')
elif opcao == '2':
    # Livros que ambos assistiram
    interseção = pessoa1.intersection(pessoa2)
    print(f'Ambas pessoas assistiram os filmes: {interseção}\n')
else:
    print('Opção inválida!')