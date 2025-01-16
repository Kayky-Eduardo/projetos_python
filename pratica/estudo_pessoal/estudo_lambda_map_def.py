import os
os.system('cls')

meio = lambda x: x / 2

# Com lambda
inteiros = [1, 2, 3, 4, 5]
print(tuple(map(lambda x: x / 2, inteiros)))

# Com def
def dividir():
    resultado = []
    for i in inteiros:
        resultado.append(i / 2)
    return resultado
print(dividir())

strings = ["Python", "é", "muito", "legal"]
comprimentos = map(lambda s: len(s), strings)
print(list(comprimentos))

iteravel = map(list, strings)
print(list(iteravel))

def laerc():
    cnt = 0
    while cnt < 3:
        cnt += 1
        if cnt == 3:
            return print(cnt)
laerc()

