#Desafio: Sistema de Recomendação de Amigos em uma Rede Social

# Simule um sistema de recomendação de amigos, onde você tem sets 
# de seguidores de diferentes usuários e quer recomendar amigos 
# para um usuário com base em quem eles seguem e quem seus seguidores seguem.

# Requisitos:
# Você tem dois sets: seguindo e seguidores de cada usuário.
# Você deve recomendar amigos para o usuário com base em:
# Quem seus seguidores seguem (mas não o seguem de volta).
# Quem o usuário está seguindo, mas que não segue de volta (sugestão de novos amigos para o usuário).
# A função deve retornar as sugestões de novos amigos para o usuário.
import os


os.system('cls')

seguidores = {
    "joao", "maria", "pedro", "ana", "luiza", "carla", "rogerio", 
    "paula", "fernando", "eliane", "gustavo", "bruna", "rafael", 
    "jose", "camila", "aline", "ricardo", "mariana", "luan", "pedro_2"
}
seguindo = {
    "pedro", "lucas", "ana", "rafael", "jose", "camila", "aline", 
    "lucas_2", "mario", "fernando", "eliane", "gustavo", "bruna", 
    "leandro", "carla", "daniela", "natalia", "maria", "pedro_2", "lucas_3"
}

recomendacao = seguidores.difference(seguindo)
print(f'recomendações para seguir: {recomendacao}')