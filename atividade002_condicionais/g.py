import os


os.system('cls')

med1 = float(input('Digite o primeiro segmento: '))
med2 = float(input('Digite o segundo segmento: '))
med3 = float(input('Digite o terceiro segmento: '))

#condicionais
if med1 + med2 > med3 and med3 + med2 > med1 and med1 + med3 > med2:
    print('Os 3 segmentos podem formar um triângulo!')
else:
    print('Os segmentos não podem formar um triângulo!')