class Soma:
    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b
    
    def set_a(self, valor):
        self._a = valor

    def set_b(self, valor):
        self._b = valor

    def somar(self):
        return self._a + self._b
    
soma = Soma()

soma.set_a(10)
soma.set_b(10)