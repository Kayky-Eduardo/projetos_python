import os


os.system('cls')

# class vendedor:
#     def __init__(self, nome):
#         self.nome = nome
#         self.vendas = 0

#     def vendeu(self, vendas):
#         self.vendas = vendas

#     def bateu_meta(self, meta):
#         if self.vendas > meta:
#             print(self.nome, 'bateu meta')
#         else:
#             print(self.nome, 'não bateu meta')

# vendedor1 = vendedor('lira')
# vendedor1.vendeu(1000)
# vendedor1.bateu_meta(600)

# vendedor2 = vendedor('Alan')
# vendedor2.vendeu(300)
# vendedor2.bateu_meta(600)
# print()

# class Pessoa:
#   def __init__(self, nome: str, idade: int, altura: float):
#     self.nome = nome
#     self.idade = idade
#     self.altura = altura

#   def dizer_ola(self):
#     print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
#           f'anos e minha altura é {self.altura}m.')

#   def cozinhar(self, receita: str):
#     print(f'Estou cozinhando um(a): {receita}')

#   def andar(self, distancia: float):
#     print(f'Saí para andar. Volto quando completar {distancia} metros')

# # Desta forma tem que ser na ordem escrita.
# pessoa = Pessoa('Luis', 18, 1.80) 
# # Na forma a seguir não importa a ordem
# # pessoa = Pessoa(nome='Luis', idade=18, altura=1.80)
# pessoa.dizer_ola()
# pessoa.andar(100.9)

class Contabancaria:
    def __init__(self, saldo_atual):
      self.__saldo = saldo_atual
    
    def depositar(self, valor):
        if valor > 0:
           self.__saldo += valor
           print(f'Depósito de {valor} adicionado a conta.')
        else:
            print('Valor invalido')

    def sacar(self, valor):
        if 0 <= valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Você sacou R${valor}')
        else:
            print('Valor inválido.')

    def consultar_saldo(self):
       return self.__saldo 

# nome = input('\nDigite seu nome: ')
# valor_conta = float(input('Valor na conta bancaria: '))
# quer_depositar = input('Deseja depositar(s/n): ').lower()
# nome = Contabancaria(valor_conta)

# if quer_depositar == 's':
#     os.system('cls')
#     qnt_deposito = float(input('Quanto deseja depositar: '))
#     nome.depositar(qnt_deposito)   
#     print(f'Valor atual na conta {nome.consultar_saldo()}')
# else:
#     quer_sacar = input('Deseja sacar(s/n): ').lower()
#     if quer_sacar == 's':
#         os.system('cls')
#         qnt_sacar = int(input('Quanto deseja sacar: '))
#         if qnt_sacar < nome.consultar_saldo():
#             nome.sacar(qnt_sacar)
#             print('Saque feito com sucesso.')
#             print(f'Valor atual na conta {nome.consultar_saldo()}')
#         else:
#             print('Valor insuficiente na conta bancaria')
#             print(f'Valor atual na conta {nome.consultar_saldo()}')
#     else:
#         print(f'Valor atual na conta {nome.consultar_saldo()}')

class ContaPoupanca(Contabancaria):
    def __init__(self, saldo_atual, taxa_juros):
        # Chamando o construtor da classe pai
        super().__init__(saldo_atual)
        self.taxa_juros = taxa_juros

    def calcular_juros(self):
        # Calcula os juros baseados na taxa de juros
        juros = self.consultar_saldo() * (self.taxa_juros / 100)
        return juros

    def aplicar_juros(self):
        juros = self.calcular_juros()
        self.depositar(juros)
        print(f'Juros de R${juros:.2f} aplicados à conta.')

class ContaCorrente(Contabancaria):
    def __init__(self, saldo_atual, limite_cheque_especial):
        # Chamando o construtor da classe pai
        super().__init__(saldo_atual)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        # Permite sacar até o limite do cheque especial
        if valor > 0 and valor <= (self.consultar_saldo() + self.limite_cheque_especial):
            saldo_anterior = self.consultar_saldo()
            super().sacar(valor)
            if saldo_anterior > self.consultar_saldo():
                print(f'Saque de R${valor} realizado com o uso do cheque especial.')
        else:
            print('Valor inválido ou saldo insuficiente para saque.')

# Criando uma conta poupança
conta_poupanca = ContaPoupanca(1000, 5)  # Saldo inicial de R$1000 e 5% de juros
conta_poupanca.depositar(200)
print(f'Saldo da conta poupança: R${conta_poupanca.consultar_saldo()}')
conta_poupanca.aplicar_juros()
print(f'Saldo após aplicação de juros: R${conta_poupanca.consultar_saldo()}')

# Criando uma conta corrente
conta_corrente = ContaCorrente(500, 200)  # Saldo inicial de R$500 e limite de cheque especial de R$200
conta_corrente.depositar(100)
print(f'Saldo da conta corrente: R${conta_corrente.consultar_saldo()}')
conta_corrente.sacar(600)  # Tentando sacar mais do que o saldo disponível, mas dentro do limite do cheque especial
print(f'Saldo após saque com cheque especial: R${conta_corrente.consultar_saldo()}')

while True:
    os.system('cls')
    continuar = input('Deseja usar o programa(s/n): ').lower()
    if continuar == 's':
        nome = input('Digite seu nome: ')
        valor_conta = int(input('Digite o valor na conta: '))
        os.system('cls')
        print('1 - Conta corrente\n2 - Conta poupança')
        tipo_conta = input('Escolha uma das opções: ')

        if tipo_conta == '1':
            os.system('cls')
            valor_cheque = float(input('Digite o valor do cheque especial: '))
            conta = ContaCorrente(valor_conta, valor_cheque)

        elif tipo_conta == '2':
            os.system('cls')
            taxa_juros = float(input('Digite o valor dos juros: '))
            conta = ContaPoupanca(valor_conta, taxa_juros)
        
        else:
            print('Opção invalida')

        print('1 - Depositar\n2 - Sacar\n3 - Valor na conta')
        escolher = input('Escolha uma das opções: ').lower()

        if escolher == '1':
            os.system('cls')
            qntd_deposito = float(input('Quantidade que deseja depositar: '))
            conta.depositar(qntd_deposito)
            print(conta.consultar_saldo())

        elif escolher == '2':
            os.system('cls')
            qntd_sacar = float(input('Quantidade que deseja sacar: '))
            conta.sacar(qntd_sacar)
            print(conta.consultar_saldo())   

        elif escolher == '3':
            print(conta.consultar_saldo())

        else:
            print('Opção invalida.')

    elif continuar == 'n':
        print('Saindo.')
        break
    
    else:
        print('Opção inválida.')