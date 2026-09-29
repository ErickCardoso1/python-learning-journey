from POO.DESAFIOS.d028.termostato import *
from rich import print
from rich.traceback import install
from rich import inspect
from rich.panel import Panel

install()

def main():
    t = Termostato()
    print(t.ftemperatura)
    inspect(t, private=True)
    




if __name__ == "__main__":
    main()