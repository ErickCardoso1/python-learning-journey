from hash import *
from rich import print
from rich.traceback import install
from rich import inspect
from rich.panel import Panel
install()

def main():
    c = Credencial()
    c.senha = 'Er898'

    inspect(c, private=True)




if __name__== "__main__":
    main()