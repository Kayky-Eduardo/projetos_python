import os


os.system('cls')

#Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor
class Bola:

    def __init__(self):
        self.cor = 'vermelha'
        self.circunferencia = 3.20
        self.material = 'Cilicone'

    def troca_cor(self, nova_cor):
        self.cor = nova_cor

    def mostra_cor(self):
        print(self.cor)

bola = Bola()

# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão,
#  a cada ano que nossa pessoa envelhece,
#  sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhercer(self):
        self.idade += 1
        print(f'{self.nome} envelheceu e agora tem {self.idade} anos.')
        if self.altura < 21:
            self.altura += 0.5
            print(f'Após envelhecer {self.nome} teve um aumento em seu '
                  f'peso {self.peso}')

    def engordar(self):
        self.peso += 2

    def emagrecer(self):
        self.peso -= 2

pessoa1 = Pessoa('kayky', 18, 70, 1.81)

# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
# com valor default zero e os demais atributos são obrigatórios.
class ContaCorrente:

    def __init__(self, numero_da_conta, nome):
        self.numero_da_conta = numero_da_conta
        self.nome = nome
        self.saldo = 0

    def Alterarnome(self, novo_nome):
        self.nome = novo_nome

    def Deposito(self, deposito):
        self.saldo += deposito

    def Saque(self, saque):
        if self.saldo > saque:
            self.saldo -= saque
        else:
            print('Saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')

conta1 = Contacorrente(1234, 'kayky')

# Classe Bichinho Virtual:
# Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade 
# b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
# este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
# então não devemos criar um atributo para armazenar esta informação,
# por que ela pode ser calculada a qualquer momento.
class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def Alterar_nome(self, novo_nome):
        self.nome = novo_nome
        print(f'Nome alterado para {self.nome}')

    def Mostrar_nome(self):
        print(f'Nome: {self.nome}')

    def Saude(self):
        self.saude = 100
        if self.fome < 40: 
            print('Tamagushi está com fome, saúde abaixando!')
            self.saude -= 10
        else:
            self.saude += 10
            print('tamagushi está cheio, aumento de saúde!')

    def Idade(self):
        print(f'Tamagushi está envelhecendo, aumentando a fome.')
        self.fome -= 10
        self.idade += 1
        print(f'Tamagushi tem {self.idade} anos.')

    def Fome(self):
        print(f'Tamagushi está ficando com fome!')
        self.fome -= 10

    def Humor(self):
        if self.fome > 50 and self.saude >= 100:
            self.humor = 'Feliz'
        else:
            self.humor = 'Triste'

        print(f'Tamagushi está {self.humor}')
    

tama1 = Tamagushi('Tama-chan', 60, 100, 18)

tama1.Idade()
tama1.Humor()