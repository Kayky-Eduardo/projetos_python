import os


os.system('cls')

class vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, 'bateu meta')
        else:
            print(self.nome, 'não bateu meta')

vendedor1 = vendedor('lira')
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)

vendedor2 = vendedor('Alan')
vendedor2.vendeu(300)
vendedor2.bateu_meta(600)
print()

class Pessoa:
  def __init__(self, nome: str, idade: int, altura: float):
    self.nome = nome
    self.idade = idade
    self.altura = altura

  def dizer_ola(self):
    print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
          f'anos e minha altura é {self.altura}m.')

  def cozinhar(self, receita: str):
    print(f'Estou cozinhando um(a): {receita}')

  def andar(self, distancia: float):
    print(f'Saí para andar. Volto quando completar {distancia} metros')

# Desta forma tem que ser na ordem escrita.
pessoa = Pessoa('Luis', 18, 1.80) 
# Na forma a seguir não importa a ordem
# pessoa = Pessoa(nome='Luis', idade=18, altura=1.80)
pessoa.dizer_ola()
pessoa.andar(100.9)

class contabancaria:
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

# print()
# conta1 = contabancaria(100)
# conta1.depositar(200)
# conta1.sacar(100)
# print(f'Saudo atual R${conta1.consultar_saldo()}')

nome = input('\nDigite seu nome: ')
valor_conta = float(input('Valor na conta bancaria: '))
quer_depositar = input('Deseja depositar(s/n): ').lower()
nome = contabancaria(valor_conta)

if quer_depositar == 's':
    os.system('cls')
    qnt_deposito = float(input('Quanto deseja depositar: '))
    nome.depositar(qnt_deposito)   
    print(f'Valor atual na conta {nome.consultar_saldo()}')
else:
    quer_sacar = input('Deseja sacar(s/n): ').lower()
    if quer_sacar == 's':
        os.system('cls')
        qnt_sacar = int(input('Quanto deseja sacar: '))
        if qnt_sacar < nome.consultar_saldo():
            nome.sacar(qnt_sacar)
            print('Saque feito com sucesso.')
            print(f'Valor atual na conta {nome.consultar_saldo()}')
        else:
            print('Valor insuficiente na conta bancaria')
            print(f'Valor atual na conta {nome.consultar_saldo()}')
    else:
        print(f'Valor atual na conta {nome.consultar_saldo()}')