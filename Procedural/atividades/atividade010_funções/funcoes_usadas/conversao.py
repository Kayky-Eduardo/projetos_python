def Temperatura(temp, valor_temp):
    if valor_temp == 'fahrenheit':
        fahrenheit = temp
        celsius = (fahrenheit - 32) * 5/9
        print(f'O valor {temp} em célsius é {celsius:.2f}')
    elif valor_temp == 'célsius' or 'celsius':
        celsius = temp
        fahrenheit = (celsius * 9/5) + 32
        print(f'O valor {temp} em fahrenheit é {fahrenheit:.2f}')
