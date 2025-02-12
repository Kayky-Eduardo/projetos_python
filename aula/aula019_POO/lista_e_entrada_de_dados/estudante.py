
class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # não faz sentido inicializar notas com um valor no
        # momento da criação do objeto (via parâmetro),
        # já que ela será modificada com o tempo á medida que
        # o estudante adicionar mais notas.
        self.notas = []
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def media(self):
        # Verifica se há notas registradas
        if len(self.notas) > 0:
            # Se houver, calcula a média somando todas as
            # notas e dividindo pelo número de notas
            return sum(self.notas) / len(self.notas)
        else:
            # Caso não haja notas, retorna 0
            return 0
    
    def resultado(self):
        media_final = self.media()
        if media_final >= 7:
            return 'Aprovado'
        elif media_final >= 5:
            return 'Recuperação'
        else:
            return 'Reprovado'