# Teste SET
import os

os.system('cls')

s = {1, 2, 3}

# Adicionar itens
s.add(4)

# Tirar itens com remove
# se não tiver o item dentro do SET vai dar erro
s.remove(2)

# Tirar itens com discard(não tem erro se não achar)
s.discard(1)

# Limpar o set s
s.clear()

# criando SET
a = {10, 20, 30, 40}
b = {40, 50, 60, 70}

# Unindo(union) dá para fazer pela função ou pelo simbolo dela |
uniao = a.union(b)

# Interseção(intersection) ou &, checa quais números estão dentro dos dois SETs(em comum)
interseção = a.intersection(b)
# saida: 40

# Diferença(difference) ou -, checa quais numeros não estão em comum(os elementos que estão no primeiro set, mas não no segundo).
diferença = a.difference(b)
# saida: 10, 20 e 30

# symmetric_difference() ou ^, retorna a diferença simétrica entre 
# dois sets (os elementos que estão em um set ou no outro, mas não em ambos).
diferença_symmetric = a.symmetric_difference(b)
# saida: 10, 20, 30, 50, 60 e 70

# issubset() verifica se o set é um subconjunto de outro set
c = {1, 2, 3, 4}
d = {1, 2}
# print(d.issubset(c)) # Saída: True

# isdisjoint() Verifica se dois sets não têm elementos em comum.
s1 = {1, 2, 3}
s2 = {4, 5, 6}
# print(s1.isdisjoint(s2))  # Saída: True

s3 = {3, 4}
# print(s1.isdisjoint(s3))  # Saída: False

# metodo update

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Atualizando conjunto1 com os elementos de conjunto2
conjunto1.update(conjunto2)
# Saida: {1, 2, 3, 4, 5}