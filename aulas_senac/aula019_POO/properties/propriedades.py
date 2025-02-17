class minha_classe:
    def __init__(self, valor):
        self._atributo = valor

    @property
    def atributo(self):
        return self._atributo
    
    @atributo.setter
    def atributo(self, valor):
        self._atributo = valor

obj = minha_classe(10)
# O atributo trabalha como uma variável
obj.atributo = 20 # (set)
# Saída semelhante a uma variável
print(obj.atributo) # (get)