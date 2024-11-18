import random
import os

os.system('cls')

coisas_militares = [
    "Exército", "Marinha", "Força Aérea", "Forças Especiais", "Comando de Operações Especiais (SOF)", 
    "Cavaleiros Templários", "Guerra Fria", "Segunda Guerra Mundial", "Primeira Guerra Mundial", 
    "Guerra do Vietnã", "Guerra do Golfo", "Guerra das Malvinas", "Batalha de Stalingrado", 
    "Batalha de Waterloo", "Batalha de Gettysburg", "Batalha de Normandia", "Táticas de guerrilha", 
    "Bunker", "Míssil balístico", "Submarino nuclear", "Tanques de guerra", "Fuzil de assalto", 
    "Arma de fogo", "Granada", "Papel da ONU em missões de paz", "Operação Desert Storm", 
    "Comando em Chefe", "Uniforme militar", "Comandos Anfíbios", "Exército de reserva", "Tropas de Elite", 
    "Rastreamento de satélites", "Radar militar", "Sistema de Defesa Aérea", "Aviões de caça", 
    "Drones militares", "Forças de Paz da ONU", "Convênio de Genebra", "Conflito armado", 
    "Táticas de combate urbano", "Blindados", "Artilharia pesada", "Guerra Cibernética", 
    "Sistemas de Missiles Antiáereos", "Batalhão de Infantaria", "Divisão militar", "Escudo antimísseis", 
    "Guerra nuclear", "Frota de Guerra", "Recrutamento militar", "Comandante Supremo", "Estágio de treinamento militar", 
    "Navio de guerra", "Operações de resgate militar", "Base militar", "Guerrilha", "Códigos militares", 
    "Sargento", "Tenente-coronel", "Oficial General", "Capitão", "Guerra convencional", "Comissão de Defesa", 
    "Terrorismo", "Escadrão de aviões de caça", "Legião Estrangeira", "Missão de paz internacional", 
    "Corpo de fuzileiros navais", "Carro de combate", "Forças de resistência", "Capacetes de combate", 
    "Batalhão de Paraquedistas", "Plano de guerra", "Códigos de guerra", "Logística militar", 
    "Esquadrão de helicópteros", "Vigilância aérea", "Combate em ambientes adversos", "Táticas de dissimulação", 
    "Treinamento de resistência", "Campos de treinamento", "Academia militar", "Soldado raso", "Exército Nacional", 
    "Soldado de elite", "Força de operações especiais", "Guerra de trincheiras", "Guerra mecanizada", 
    "Caminhão militar", "Esquadrão de operações especiais", "Unidade de inteligência", "Sistema de comunicação militar", 
    "Esquadrão de caças", "Corpo de artilharia", "Exército de terra", "Blindagem militar", 
    "Guerra psicológica", "Conflito internacional", "Apoio aéreo próximo", "Invasão militar", 
    "Combate aéreo", "Missão de resgate", "Operação de cerco", "Guerra de posição", "Minas terrestres", 
    "Forças de defesa", "Fase de mobilização", "Missão de sabotagem", "Colaboração militar internacional", 
    "Planejamento estratégico", "Fazenda de armamento", "Guarda costeira", "Sistema de inteligência militar", 
    "Combate no deserto", "Força de defesa aérea", "Papel de liderança militar", "Interceptação de comunicações", 
    "Simulação de combate", "Tecnologia militar avançada", "Missões secretas", "Controle de fronteira", 
    "Forças militares aliadas", "Batalha naval", "Guerra com drones", "Explosivos militares", "Monitoramento de fronteira"
]
coisas_militares_minusculas = [item.lower() for item in coisas_militares]
escolhida = random.choice(coisas_militares_minusculas)
tentativas_c = ['_'] * len(escolhida)
tentativas = 6
print('--------TEMA: MILITAR-----------')
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