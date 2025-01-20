import os

# definição da função
def mutiplicador(a, b=1):
    return a * b


os.system('cls')

resultado_1 = mutiplicador(5)
resultado_2 = mutiplicador(5, 2)

print(f'Primeiro resultado: {resultado_1}')
print(f'Segundo resultado: {resultado_2}')