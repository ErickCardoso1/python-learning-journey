from rich import print
from rich.table import Table
from rich import inspect
from rich.traceback import install
install()

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f'Meu nome é {self.nome}, trabalho no setor de {self.setor}, meu cargo é {self.cargo}'


f1 = Funcionario("Erick", "Pessoal", "Soldado")

inspect(f1)

print(f1.apresentar())