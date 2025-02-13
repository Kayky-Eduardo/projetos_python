class OperacaoMatematica():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        soma = self.a + self.b
        return soma

    def subtrair(self):
        subtracao = self.a - self.b
        return subtracao

    def multiplicar(self):
        produto = self.a * self.b
        return produto

    def dividir(self):
        if self.b != 0:
            divisao = self.a / self.b
        else:
            print('Erro! Não da para dividir por 0.')
        return divisao

    def divisao_inteira(self):
        if self.b != 0:
            divisao_inteira = self.a // self.b
        else:
            print('Erro! Não da para dividir por 0.')
        return divisao_inteira

    def resto_da_divisao(self):
        if self.b != 0:
            resto_da_divisao = self.a % self.b
        else:
            print('Erro! Não da para dividir por 0.')
        return resto_da_divisao
