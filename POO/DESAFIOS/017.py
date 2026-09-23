from rich import print
from rich.panel import Panel
from rich import inspect
from rich.traceback import install
install()

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        content = f'{self.nome.center(30, " ")}'
        content += f'{"-" * 30}'
        precof = f'R${self.valor:,.2f}'
        content += f'{precof.center(30, ".")}'
        caixa = Panel(content, title="Produto", width=34)
        print(caixa)

p1 = Produto("Iphone 17 PRO MAX", 25000)
p1.etiqueta()