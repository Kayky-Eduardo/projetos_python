import os


os.system('cls')

# Definindo a função
def calcular_vm_media(espaco, tempo, espaco_un, tempo_un):
    # Convertendo a distância para quilômetros
    # Se a unidade for metros (1km == 1000m)
    if espaco_un == 'metros':
        espaco = espaco / 1000

    # Convertendo o tempo para horas
    # Se a unidade for minutos (1 hora == 60 minutos)
    if tempo_un == 'minutos':
        tempo = tempo / 60

    vm_media = espaco / tempo
    return vm_media

espaco = float(input('Digite a distância percorrida: '))
espaco_un = input('A distância percorrida é em Km ou metros: ').lower()
tempo = float(input('Digite o tempo gasto: '))
tempo_un = input('O tempo é em horas ou minutos: ').lower()

# Invocando a função
vm = calcular_vm_media(espaco, tempo, espaco_un, tempo_un)

# Exibir o resultado
print(f'A vm média é {vm:.2f} {espaco_un}/{tempo_un}')