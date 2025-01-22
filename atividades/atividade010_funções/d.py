import os


os.system('cls')

def Temperatura(temp, valor_temp):
    if valor_temp == 'fahrenheit':
        fahrenheit = temp
        celsius = (fahrenheit - 32) * 5/9
        print(f'O valor {temp} em célsius é {celsius:.2f}')
    elif valor_temp == 'célsius' or 'celsius':
        celsius = temp
        fahrenheit = (celsius * 9/5) + 32
        print(f'O valor {temp} em fahrenheit é {fahrenheit:.2f}')

valor_da_temperatura = float(input('Digite a temperatura: '))
tipo_temp = input('O valor está em fahrenheit ou célsius: ')
Temperatura(valor_da_temperatura, tipo_temp)