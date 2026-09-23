class Gafanhoto:
    """This class creates a grasshopper."""
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return (f'{self.nome} é um gafanhoto(a) com {self.idade} anos de idade')

g1 = Gafanhoto(nome='Erick', idade = 17)

print(g1)
g1.aniversario()
print(g1)
print(g1.__getstate__())
