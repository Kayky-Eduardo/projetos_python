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

# Conjuntos de seguidores e seguindo
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

# Recomendações de amigos para seguir
# 1. Quem os seguidores seguem (mas não segue o usuário)
recomendacoes_seguidores = seguidores.difference(seguindo)

# 2. Quem o usuário segue, mas não o segue de volta
recomendacoes_usuario = seguindo.difference(seguidores)

# Exibindo as recomendações
print("Recomendações baseadas em quem seus seguidores seguem:")
print(recomendacoes_seguidores)

print("\nRecomendações baseadas em quem você segue, mas não te segue:")
print(recomendacoes_usuario)
