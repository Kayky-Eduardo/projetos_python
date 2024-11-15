import random
import os

os.system('cls')

palavras = ['espadas', 'escudos', 'castelo', 'nobre', 'cavaleiro',
            'peste negra', 'guerra', 'estratégia', 'bobo da corte',
            'rei', 'servo']

escolhida = random.choice(palavras)
tentativas_c = ['_'] * len(escolhida)
tentativas = 6
print('--------TEMA: MEDIEVAL-----------')
while tentativas > 0:
    print('\nPalavra: '+' '.join(tentativas_c))
    print(f'Voce tem {tentativas} tentativas restantes.')
    letra = input("Digite uma letra: ").lower()
    
    if letra in tentativas_c:
        print(f'Você já tentou essa letra')
        continue
    if letra in escolhida:
        for i in range(len(escolhida)):
            if letra == escolhida[i]:
                tentativas_c[i] = letra
    else:
        print('próxima letra!')
        tentativas -= 1
    if '_' not in tentativas_c:
        print(f'Você adivinhou a palavra correta: {escolhida} ')
        break
else:
    print(f'\nVocê perdeu! A palavra era: {escolhida}')