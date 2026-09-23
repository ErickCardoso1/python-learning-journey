from rich import print
from rich.panel import Panel
from rich import inspect
from rich.traceback import install
import os
from time import sleep
install()

class Gamer:
    def __init__(self, nome, nickname):
        self.nome = nome
        self.nick = nickname
        self.favoritos = []

    def addFavoritos(self, *args):
        self.favoritos.extend(args)

    def ficha(self):
        conteudo = f'Nome real: {self.nome}\n'
        conteudo += 'Jogos favoritos:\n'
        for games in self.favoritos:
            conteudo += f'{games}\n'

        painel = Panel(conteudo, title=f'Jogador: <{self.nick}>')
        print(painel)



g1 = Gamer('Erick Gabriel', 'ErickEpic898')
inspect(g1)
g1.addFavoritos("Pokémon FireRed", "Digimon", "Zelda")
g1.ficha()
inspect(g1)