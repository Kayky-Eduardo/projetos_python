import os


os.system('cls')

def Calcular_imc(altura, peso):
    imc = peso / (altura**2)
    
    return imc

altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso em kg: '))

print(f'O seu IMC é de {Calcular_imc(altura, peso):.2f}')