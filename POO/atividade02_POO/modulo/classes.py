import os


class Veiculo:
# O dicionário veiculos é declarado antes do método construtor porque ele é um atributo de classe,
# e não um atributo de instância.
# Atributos de classe são compartilhados entre todas as instâncias de uma classe.
# Eles pertencem à classe em si e não a objetos individuais.
# Atributos de instância são específicos de cada objeto criado a partir da classe.
# Cada instância tem sua própria cópia desses atributos.

    veiculos = {'Carro': {}, 'Moto': {}, 'Caminhão': {}}
    
    def __init__(self, marca, modelo, cor, ano):
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._ano = ano

    def exibir_info():
        for i, j in Veiculo.veiculos.items():
            print(i, j)

    def cadastrar():
        """Método vai ser utilizado para cadastrar os dados no dicionário"""
        pass

    def exibir_dados():
        """Este método vai ser utilizado para exibir
        informações no dicionario veiculos"""
        pass

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
    def __init__(self, marca, modelo, cor, ano, combustivel):
        super().__init__(marca, modelo, cor, ano)
        self._combustivel = combustivel
    
    
    @property
    def combustivel(self):
        return self._combustivel
    
    def cadastrar(self):
        """Metódo para cadastrar carros no dicionário veiculos
        ultilizando a classe veiculo"""
        try:
            nome = input('Digite o nome: ').capitalize()
            marca = input('Marca do carro: ').capitalize()
            modelo = input('Modelo do carro: ').capitalize()
            cor = input('Cor do carro: ').capitalize()
            ano = int(input('Ano de lançamento do carro: '))
            combustivel = input('combustivel: ').capitalize()

            self.veiculos['Carro'][nome] = {
                'Modelo': modelo,
                'Marca': marca,
                'Cor': cor,
                'Ano': ano,
                'Combustível': combustivel
            }
            os.system('cls')
            print('Carro cadastrado com sucesso!')
        except ValueError:
            print(f'Ano foi digitado de forma incorreta!')
            
    def exibir_dados():
        """Fazendo checagem no dicionario e
        exibindo os dados do carro com loop for"""
        os.system('cls')
        if Veiculo.veiculos['Carro']:
            for nome, dados in Veiculo.veiculos['Carro'].items():
                print(f'{nome}:\nModelo: {dados["Modelo"]}\n'
                    f'Marca: {dados["Marca"]}\n'
                    f'Cor: {dados["Cor"]}\nAno: {dados["Ano"]}\n'
                    f'Combustível: {dados["Combustível"]}')
                print('-'*70)

        else:
            print('Nenhum carro cadastrado.')
            print('-'*70)

    def trocar_dados():
        """Checando a presença da chave no dicionario
        e trocando o seu valor"""
        os.system('cls')
        Carro.exibir_dados()
        dicio_carro = Veiculo.veiculos['Carro']
        if dicio_carro:
            trocar = input('Qual o nome do dono do carro: ').capitalize()
            if trocar in dicio_carro:
                opcao = input('Qual dado deseja alterar: ').capitalize()
                for i in dicio_carro[trocar]:
                    if i == opcao:
                        novo_dado = input('Digite o dado q deseja '
                                        'colocar no lugar: ')
                        dicio_carro[trocar][opcao] = novo_dado
            print('Troca de dados feita com sucesso.')
        else:
            print(f'Cadastros vazio.')

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, ano, tipo_moto):
        super().__init__(marca, modelo, cor, ano)
        self._tipo_moto = tipo_moto

    @property
    def tipo_moto(self):
        return self._tipo_moto
    
    @tipo_moto.setter
    def tipo_mot(self, tipo_moto):
        self._tipo_moto = tipo_moto

    def cadastrar(self):
        try: 
            nome = input('Digite o nome: ').capitalize()
            marca = input('Marca da moto: ').capitalize()
            modelo = input('Modelo da moto: ').capitalize()
            cor = input('Cor da moto: ').capitalize()
            ano = int(input('Ano de lançamento da moto: '))
            tipo_moto = input('tipo de moto (Esportiva, '
                              'Custom, etc.): ').capitalize()
            self.veiculos['Moto'][nome] = {
                'Modelo': modelo,
                'Marca': marca,
                'Cor': cor,
                'Ano': ano,
                'Tipo': tipo_moto
            }
            os.system('cls')
            print('Moto cadastrada com sucesso!')
        except ValueError:
            print(f'Ano foi digitado de forma incorreta!')
            
    def exibir_dados():
        os.system('cls')
        if Veiculo.veiculos['Moto']:
            for nome, dados in Veiculo.veiculos['Moto'].items():
                print(f'{nome}:\nModelo: {dados["Modelo"]}\n'
                    f'Marca: {dados["Marca"]}\n'
                    f'Cor: {dados["Cor"]}\nAno: {dados["Ano"]}\n'
                    f'Tipo moto: {dados["Tipo"]}')
                print('-'*70)
        else:
            print('Nenhuma moto cadastrada.')
            print('-'*70)

    def trocar_dados():
        os.system('cls')
        Moto.exibir_dados()
        dicio_moto = Veiculo.veiculos['Moto']
        if dicio_moto:
            trocar = input('Qual o nome do dono da moto: ').capitalize()
            if trocar in dicio_moto:
                opcao = input('Qual dado deseja alterar: ').capitalize()
                for i in dicio_moto[trocar]:
                    if i == opcao:
                        novo_dado = input('Digite o dado q deseja '
                                        'colocar no lugar: ')
                        dicio_moto[trocar][opcao] = novo_dado
            print('Troca de dados feita com sucesso.')

        else:
            print(f'Cadastros vazio.')
            print('-'*70)

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, cor, ano, carga):
        super().__init__(marca, modelo, cor, ano)
        self._carga = carga

    @property
    def carga(self):
        return self._carga
    
    @carga.setter
    def carga(self, nova_carga):
        self._carga = nova_carga

    def cadastrar(self):
        try:
            nome = input('Digite seu nome: ').capitalize()
            marca = input('Marca do caminhão: ').capitalize()
            modelo = input('Modelo do caminhão: ').capitalize()
            cor = input('Cor do caminhão: ').capitalize()
            ano = int(input('Ano de lançamento do caminhão: '))
            carga_maxima = input('Capacidade de carga(kg): ').capitalize()
            
            self.veiculos['Caminhão'][nome] = {
                'Modelo': modelo,
                'Marca': marca,
                'Cor': cor,
                'Ano': ano,
                'Carga máxima': carga_maxima
            }
            os.system('cls')
            print('Caminhão cadastrado com sucesso!')
        except ValueError:
            print(f'Ano foi digitado de forma incorreta!')
            
    def exibir_dados():
        os.system('cls')
        if Veiculo.veiculos['Caminhão']:
            for nome, dados in Veiculo.veiculos['Caminhão'].items():
                print(f'{nome}:\nModelo: {dados["Modelo"]}\n'
                    f'Marca: {dados["Marca"]}\n'
                    f'Cor: {dados["Cor"]}\nAno: {dados["Ano"]}\n'
                    f'Carga máxima: {dados["Carga máxima"]}')
                print('-'*70)
        else:
            print('Nenhum caminhão cadastrado.')
            print('-'*70)

    def trocar_dados():
        os.system('cls')
        Caminhao.exibir_dados()
        dicio_caminhao = Veiculo.veiculos['Caminhão']
        if dicio_caminhao:
            trocar = input('Qual o nome do dono do caminhão: ').capitalize()
            if trocar in dicio_caminhao:
                opcao = input('Qual dado deseja alterar: ').capitalize()
                for i in dicio_caminhao[trocar]:
                    if i == opcao:
                        novo_dado = input('Digite o dado q deseja '
                                        'colocar no lugar: ')
                        dicio_caminhao[trocar][opcao] = novo_dado
            print('Troca de dados feita com sucesso.')

        else:
            print(f'Cadastros vazio.')