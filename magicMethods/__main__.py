from classes import *
from rich import inspect

def main():
    c1 = Carteira(100)
    c2 = Carteira(200)

    c3 = c1 + c2

    print(c3)
    inspect(c3, private=True)

    print(c1 == c2)

if __name__ == '__main__':
    main()
