import os


os.system('cls')

print('---------Fatiamento de Strings-----------')

frase = 'String em Python!'

# Exibindo a string original
print(f'String original: {frase}')

# Fatiamento: acessando partes específicas da string
# Primeiros cinco caracteres
primeiros_cinco = frase[:5]
print(f'Primeiros cincos caracteres: {primeiros_cinco}')

#Últimos dez caracteres
ultimos_dez = frase[-10:]
print(f'Últimos dez caracteres: {ultimos_dez}')

# Do quarto ao décimo caractere
quarto_ao_decimo = frase[3:10]
print(f'Do quarto ao décimo caractere: {quarto_ao_decimo}')

# A cada dois caracteres
a_cada_dois = frase[::2]
print(f'A cada dois caracteres: {a_cada_dois}')

# Invertendo a string
invertida = frase[::-1]
print(f'String invertida: {invertida}')
print()