from rich import print
from rich.panel import Panel
from rich import inspect
from rich.traceback import install
import os
from time import sleep
install()

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pgAtual = 1

    def mostrar_paginas(self):
        livro = f"""
╭──────────────────────╮╭──────────────────────╮
│ ~~~~~~~~~~~~~~~~~~~~ ││ ~~~~~~~~~~~~~~~~~~~~ │
│ ~~~~~~~~~~~~~~~~~~~~ ││ ~~~~~~~~~~~~~~~~~~~~ │
│ ~~~~~~~~~~~~~~~~~~~~ ││ ~~~~~~~~~~~~~~~~~~~~ │
│ ~~~~~~~~~~~~~~~~~~~~ ││ ~~~~~~~~~~~~~~~~~~~~ │
│ ~~~~~~~~~~~~~~~~~~~~ ││ ~~~~~~~~~~~~~~~~~~~~ │
│ ~~~~~~~~~~~~~~~~~~~~ ││ ~~~~~~~~~~~~~~~~~~~~ │
│ ~~~~~~~~~~~~~~~~~~~~ ││ ~~~~~~~~~~~~~~~~~~~~ │
│ ~~~~~~~~~~~~~~~~~~~~ ││ ~~~~~~~~~~~~~~~~~~~~ │
╰──────────────────────╯╰──────────────────────╯
 Pg {self.pgAtual}                                      Pg {self.pgAtual+1}  
"""
        print(livro)

    def passarPagina(self, nPaginas):
        incremento = nPaginas * 2
        if self.pgAtual >= self.paginas - 1:
            print("Você está na última página!")
            return False
        if self.pgAtual + incremento >= self.paginas:
            print(f"O livro só tem {self.paginas} páginas!")
            return False
        self.pgAtual += incremento
        return True

    

l1 = Livro("O Mundo de Erick", 200)
l1.mostrar_paginas()


while True:
    os.system("cls")
    l1.mostrar_paginas()
    try:
        choise = int(input("Você quer passar quantas páginas? "))
    except ValueError:
        print("Digite um número válido.")
        sleep(1)
        continue
    if not l1.passarPagina(choise):
        sleep(1)
        continue
    sleep(2)

    