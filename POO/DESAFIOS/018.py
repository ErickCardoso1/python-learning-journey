from rich import print
from rich.panel import Panel
from rich import inspect
from rich.traceback import install
install()

class Churrasco:
    def __init__(self, titulo, pessoas):
        self.titulo  = titulo
        self.pessoas = pessoas
        self.kg_carne = 82.40
        self.consumo_pessoa = 0.4

    def analisar(self):
        kgTotal = self.pessoas * self.consumo_pessoa
        valorTotal = kgTotal*self.kg_carne
        conteudo = f"""
        Analisando o {self.titulo} com {self.pessoas} convidados
        Cada participante comerá {self.consumo_pessoa}Kg e cada Kg custa R${self.kg_carne:,.2f}
        Recomendo comprar {kgTotal}Kg de carne
        O custo total será de R${valorTotal:,.2f}
        Cada pessoa pagará R${(valorTotal/self.pessoas):,.2f} para  participar.
        """
        c = Panel(conteudo, title=self.titulo)
        print(c)

c1 = Churrasco("Churras dos Cria", 15)
c1.analisar()