import os
import copy

os.system('cls')

dic = {
    'nome': 'Kayky Eduardo',
    'idade': 18,
    'num': [1, 2, 3],
    'cor': 'pardo'
}

# Método len com a mesma funcionalidade de listas, só que nesse caso
# fala quantas chaves tem dentro do dicionário
print(f'Método len: {len(dic)}\n', '-'*70)


# Método keys, volta as chaves que estão dentro do dicionário
print(f'Método keys: {dic.keys()}\n', '-'*70)

# Método values, volta os valores dentro do dicionário
print(f'Método values: {dic.values()}\n', '-'*70)

# Método items, volta o valor e as chaves dentro do dicionário
print(f'Método items: {dic.items()}\n', '-'*70)

# Método setdefault, adiciona valor se a chave não existir
print(f'Método setfefault: {dic.setdefault("Sobrenome", "Leão")}')

# Método copy, copia o dicionário
# Se fizer dic2 = dic tudo que você fizer com o dic2 vai ser feito com o dic
# Porém, o método copy é uma copia rasa, se tiver algum dado 
# de estrutura mutável dentro do dic, vai mudar ambos os dic
dic2 = dic.copy()
print(f'Método copy: {dic2}\n', '='*70)
# Exemplo:
dic2['num'][1] = 10
dic3 = copy.deepcopy(dic)
# O python tem uma biblioteca chamada de copy que resolve este problema
# Como é deepcopy, faz uma cópia profunda e as mudanças feitas
# são alterada apenas na variavel que recebeu a deepcopy
dic3['num'][2] = 40
print(f'Exemplo da shallow copy(dic): {dic}')
print(f'Exemplo da shallow copy(dic2): {dic2}')
print(f'Cópia profunda(dic3): {dic3}\n','='*70)


# Método get, ele busca a chave no dicionário e se não achar ele retorna none.
# Dá pra fazer ele voltar algo que você definiu
print(f'Método get: {dic.get("email")}')
print(f'Método get voltando um valor definido: ')
print(dic.get("email", 'Eu defini'), '\n', '='*70)

# Método pop, apaga um item com a chave especificada, retorna o valor
# associado a chave removida
dic.pop('num')
print(f'Método pop(tirei num): {dic}')
# Outra forma de ser usado
cor_kayky = dic.pop('cor') # A váriavel cor_kayky vai ter o valor cor guardado
print(f'O valor recebido pela váriavel cor_kayky: {cor_kayky}')
print(f'O dicionário n tem mais a chave nem o valor:\n{dic}')

# Outra forma de ser usado
inexistente = dic.pop('asd', 'Não existe')
print(f'fazendo print da váriavel: {inexistente}\n','-'*70)

# Método popitem, remove o ultimo item adicionado, dá pra fazer uma variável
# receber valor igual no método pop
print(f'Antes do popitem: {dic}')
dic.popitem()
print(f'Depos do popitem: {dic}')


# Dá pra fazer casting e transformar o dicionário em tuplas, listas e etc.
# ex: list(dic.keys()), list(dic.items()), list(dic.values())