from player import Wizard
from player import Warrior
from rich import print
from rich.traceback import install
from rich import inspect
from rich.panel import Panel
from player import *

install()

def main():
    p1 = Warrior("Kratos", 2000)
    p2 = Wizard("Merlin", 3000)

    p1.attack(p2, 1000)
    p2.attack(p1, 1000)
    p1.heal()
    p2.heal()

    inspect(p1)
    inspect(p2)


if __name__ == "__main__":
    main()