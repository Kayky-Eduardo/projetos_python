#Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.
import os


os.system('cls')

lista_nome = []
lista_nota = []

for i in range(4):
    nome = input(f'Digite o nome do aluno {i + 1}: ')
    lista_nome.append(nome)
    nota = float(input('Nota do aluno: '))
    lista_nota.append(nota)

soma = 0
for i in lista_nota:
    soma += i
    
media = soma / len(lista_nota)

print(media)