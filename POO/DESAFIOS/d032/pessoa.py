from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome: str, nascimento: int):
        self._nome = nome
        self.nascimento = nascimento

    def pedirNascimento(self):
        while (True):
            valor = int(input('Digite um ano de nascimento válido (1900 - 2026): '))
            if 1900 <= valor <= from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome: str, nascimento: int):
        self._nome = nome
        self.nascimento = nascimento

    def pedirNascimento(self):
        while (True):
            valor = int(input('Digite um ano de nascimento válido (1900 - 2026): '))
            if 1900 <= valor <= 2026:
                break
        return valor

    @property
    def nascimento(self):
        return self._nascimento
    
    @property
    def idade(self):
        return date.today().year - self._nascimento


    @nascimento.setter
    def nascimento(self, valor):
        if valor < 1900 or valor > date.today().year:
            print('Ano Inválido!\n')
            valor = self.pedirNascimento()
        self._nascimento = valor
   
    @idade.setter
    def idade(self, valor):
        print("Não é possível alterar a idade diretamente. Altere o ano de nascimento!")

class Aluno(Pessoa):
    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
    def __init__(self, nome: str, nascimento: int, curso):
        super().__init__(nome, nascimento)
        self.curso = curso

    def addCurso(self, curso: str):
        if curso.upper() in Aluno.cursos_oficiais:
            raise ValueError("Curso já se encontra na lista oficial de cursos")
        Aluno.cursos_oficiais.append(curso.upper())

    @property
    def curso(self):
        return self._curso
 
    @curso.setter
    def curso(self, valor: str):
        if valor.upper() not in Aluno.cursos_oficiais:
            raise ValueError(f'O curso {valor.upper()} não existe!')
        self._curso = valor.upper()



    :
                break
        return valor

    @property
    def nascimento(self):
        return self._nascimento
    
    @property
    def idade(self):
        return date.today().year - self._nascimento


    @nascimento.setter
    def nascimento(self, valor):
        if valor < 1900 or valor > date.today().year:
            print('Ano Inválido!\n')
            valor = self.pedirNascimento()
        self._nascimento = valor
   
    @idade.setter
    def idade(self, valor):
        print("Não é possível alterar a idade diretamente. Altere o ano de nascimento!")

class Aluno(Pessoa):
    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
    def __init__(self, nome: str, nascimento: int, curso):
        super().__init__(nome, nascimento)
        self.curso = curso

    def addCurso(self, curso: str):
        if curso.upper() in Aluno.cursos_oficiais:
            raise ValueError("Curso já se encontra na lista oficial de cursos")
        Aluno.cursos_oficiais.append(curso.upper())

    @property
    def curso(self):
        return self._curso
 
    @curso.setter
    def curso(self, valor: str):
        if valor.upper() not in Aluno.cursos_oficiais:
            raise ValueError(f'O curso {valor.upper()} não existe!')
        self._curso = valor.upper()



    