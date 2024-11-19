import os


os.system('cls')

n = int(input("Digite o número para sequência de Fibonacci: "))

# Casos especiais
if n <= 0:
    print("Nada")
elif n == 1:
    print("0")
elif n == 2:
    print("0 1")
else:
    a, b = 0, 1
    print(a, b, end=" ")

    for i in range(2, n+1):
        c = a + b
        print(c, end=" ")
        a, b = b, c
