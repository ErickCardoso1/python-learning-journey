from classes import *
from rich import inspect

def main():
   pessoa1 = Gerente('Erick', 2000) 
   inspect(pessoa1, private=True)
   pessoa1.salario = 1000

if __name__ == '__main__':
    main()