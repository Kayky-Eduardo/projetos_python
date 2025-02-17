import os


#podemos importar só as funções que queremos utilizar
from datetime import datetime
from datetime import date

#limpeza
os.system('cls')

#declarando uma variável para data
data = datetime.now()

#declarando uma variavel data formatada
data_formatada = data.strftime('%d/%m/%Y')

#declarando uma variável data e hora formatada
data_hora_formatado = data.strftime('%d/%m/%Y %H:%M')

print(f'Data formatada: {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatado}')

#recebendo o ano
data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

#Imprimindo a data atual e o nascimento
print(f'Data atual no sistema: {data_atual}')
print(f'Nascimento...........: {nascimento}')
#imprimindo só o ano
print(f'Ano atual............: {data_atual.year}')
#imprimindo só o idade
print(f'Sua idade é .........: {idade} anos')
