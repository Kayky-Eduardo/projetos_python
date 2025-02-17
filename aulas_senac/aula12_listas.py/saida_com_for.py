import os

os.system('cls')  # Limpa o console (no Windows)

print('-' * 70)
print('SAÍDA COM FOR')
print('-' * 70)

# Criando uma lista
lista_alunos = []

# Coletando os nomes dos alunos
for c in range(0, 5):
    nome = str(input('Entre com o nome do aluno: '))
    # Guardando na lista
    lista_alunos.append(nome)

print()
print('Impressão dos nomes dos alunos:')

# Usando len() para saber a quantidade de alunos
for i in range(len(lista_alunos)):
    print(lista_alunos[i], end=' ')
    if i == 3:  # Alinhação condicional ajustada
        print()

print()
print('-' * 70)
print('Fim do programa!')
print('-' * 70)
