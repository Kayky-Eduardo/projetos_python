class Soma:
    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a
    
    @property
    def b(self):
        return self._b
    
    @a.setter
    def a(self, valor):
        self._a = valor

    @b.setter
    def b(self, valor):
        self._b = valor

    def somar(self):
        return self._a + self._b
    
soma = Soma()

soma.a = 10
soma.b = 10

