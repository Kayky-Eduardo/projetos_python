#k) Desenvolva um programa para controlar tarefas de um projeto, onde cada
# tarefa terá um nome, data de vencimento e prioridade (alta, média, baixa).
# O programa deve permitir que o usuário cadastre ao menos 5 tarefas e altere
# a prioridade ou data de vencimento de qualquer tarefa. Após o cadastro, o
# programa deve listar todas as tarefas ordenadas pela data de vencimento e
# gerar um relatório que informe quantas tarefas possuem prioridade alta e
# quantas têm vencimento no próximo mês.
import os


os.system('cls')


projeto = {}

tarefa = input('Digite a tarefa: ')
nome = input('Digite o nome da tarefa: ')
data_vencimento = input('Digite a data de vencimento da tarefa: ')
prioridade = input('Digite a prioridade da tarefa(alta, média, baixa): ')

