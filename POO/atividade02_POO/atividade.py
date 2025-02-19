# Você foi designado para desenvolver um sistema de cadastro de veículos para uma locadora de carros.
# A empresa possui diversos tipos de veículos, como carros, motos e caminhões. 
# Todos os veículos possuem características em comum, como marca, modelo, ano e cor, mas cada tipo de veículo tem atributos e comportamentos específicos.
# Para isso, você deve criar uma classe base chamada Veículo, que contenha esses atributos comuns e um método para exibir suas informações.
# Em seguida, você deve criar subclasses para Carro, Moto e Caminhão, que herdem da classe Veículo, adicionando atributos específicos de cada tipo,
# como o tipo de combustível para o carro, o tipo de moto (esportiva, custom) e a capacidade de carga para o caminhão.
# O objetivo é garantir que o sistema consiga gerenciar diferentes tipos de veículos de forma eficiente e sem duplicação de código,
# utilizando os conceitos de herança e polimorfismo.
import os


class Veiculo:
    def __init__(self, marca, modelo, cor, ano):
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._ano = ano
        self._carro = []
        self._moto = []
        self._caminhao = []

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def cor(self):
        return self._cor

    @property
    def ano(self):
        return self._ano
    
    @marca.setter
    def marca(self, nova_marca):
        self._marca = nova_marca
    
    @modelo.setter
    def modelo(self, novo_modelo):
        self._modelo = novo_modelo
    
    @cor.setter
    def cor(self, nova_cor):
       self._cor = nova_cor
    
    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)

    def tipagem_combustivel(self, combustivel):
        self.combustivel = combustivel

    def adicionar_na_lista(self, info):
        self._carro.append(info)
    
class Moto(Veiculo):
    def tipagem_moto(self, tipo_moto):
        self.tipo_moto = tipo_moto

    def adicionar_na_lista(self, info):
        self._moto.append(info)
       
class Caminhao(Veiculo):   

    def carga_maxima(self, max_carga):
            self.max_carga = max_carga

    def adicionar_na_lista(self, info):
        self._caminhao.append(info)
    
veiculos = {'Carro': {}, 'Moto': {}, 'Caminhão': {}}
while True:
    print('Dados para cadastro: ')
    marca = input('Digite a marca do veículo: ')
    modelo = input('Digte o modelo do veículo: ')
    cor = input('Digite a cor do veículo: ')
    ano = int(input(f'Digite o ano de lançamento do veículo: '))

    os.system('cls')
    print('Escolha uma opção:')
    escolha = input('0. Sair\n1. Carro\n2. Moto\n3. Caminhão\nEscolha: ')
    os.system('cls')

    if escolha == '0':
        break
    
    elif escolha == '1':
        carro = Carro(marca, modelo, cor, ano)
        tipo_combustivel = input('Digite o tipo do combustivel: ')
        
        carro.tipagem_combustivel(tipo_combustivel)
        print('Carro cadastrado')

    elif escolha == '2':
        moto = Moto(marca, modelo, cor, ano)
        tipo_moto = input('Digite o tipo de moto(esportiva, custom): ')
        moto.tipagem_moto(tipo_moto)
        print('Moto cadastrada')
    
    elif escolha == '3':
        caminhao = Caminhao(marca, modelo, cor, ano, carga)
        carga_maxima = int(input('Digite a carga máxima(kg) '
                                 'que o caminhão aguenta'))
        carga = caminhao.carga_maxima(carga_maxima)
        print('Caminhão cadastrado')
    
    else:
        print('Opção inválida')
        print('Tente novamente!')




    # PARA LEMBRAR
    # PLANEJO FAZER UMA DIVISÃO POR LISTA OU DICIONARIO(no caso do carro, vai fazer checagem por combustivel,
    # na moto por tipo e no caminhão pela carga maxima)
    # PRATICAMENTE VAI FAZER UMA CHECAGEM SE JÁ EXISTE, E SE NÃO EXISTIR
    # IRA CRIAR UMA PARTE SÓ PARA ESTE TIPO.
    # EX:
    # COMBUSTIVEL1:             TIPO1:                  CARGA MAX1:
    # CARRO1(DADOS)             MOTO1(DADOS)            CAMINHAO1(DADOS)
    # CARRO2(DADOS)             MOTO2(DADOS)            CAMINHAO2(DADOS)
    
    # COMBUSTIVEL2:             TIPO2:                  CARGA MAX2:
    # CARRO1(DADOS)             MOTO1(DADOS)            CAMINHAO1(DADOS)
    # CARRO2(DADOS)             MOTO2(DADOS)            CAMINHAO02(DADOS)