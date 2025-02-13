import os


os.system('cls')

# Definindo uma função
def calcular_velocidade_media(distancia, tempo):
    # Vm = ΔS/Δt
    velocidade_media = distancia / tempo
    return velocidade_media

distancia = float(input('Digite a distância percorrida(em km): '))
tempo = float(input('Digite o tempo gasto(em horas): '))

# Calcular a velocidade média usando a função criada
velocidade = calcular_velocidade_media(distancia, tempo)

# Exibir resultado
print(f'A velocidade média é {velocidade:.2f} km/h')
