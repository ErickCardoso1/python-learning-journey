from POO.DESAFIOS.d029.diario import *
from rich import print
from rich.traceback import install
from rich import inspect
from rich.panel import Panel

install()

def main():
    d = Diario('1245')

    d.escrever('eu sou lindo')
    d.escrever('Eu amo a Paula')
    try:
        d.ler(1245)
    except Exception as e:
        print(e)

    inspect(d, private = True, methods = True)
    


if __name__ == "__main__":
    main()