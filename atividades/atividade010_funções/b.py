import os
from funcoes_usadas import cadastro

os.system('cls')


num_de_vezes = int(input("Quantos alunos deseja cadastrar? "))
cadastro.Cadastrar_alunos(num_de_vezes)