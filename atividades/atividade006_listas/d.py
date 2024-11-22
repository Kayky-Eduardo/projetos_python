#Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.
import os


os.system('cls')

lista_nome = []
lista_nota = []
for i in range(5):
    nome = input('Digite o nome do aluno: ')
    lista_nome.append(nome)
    nota = input('Nota do aluno: ')
    lista_nota.append(nota)

soma = 0
for i in lista_nota:
    soma += i
    
media = soma / 4

print(media)