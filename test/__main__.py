from classes import *
from rich import inspect

def main():
   a1 = DOC('prova', 550_000)
   inspect(a1, private=True, methods=True,)
   a1.abrir()

if __name__ == '__main__':
    main()