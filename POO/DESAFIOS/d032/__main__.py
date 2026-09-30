from rich import inspect
from pessoa import *

def main():
    c1 = Aluno('Erick', 2005, 'ENG')
    c1.addCurso('MED')
    c1.idade = 14
    c1.nascimento = 2004
    c1.curso = 'MED'
    inspect(c1, private=True, methods=True)

 
if __name__ == '__main__':
    main()