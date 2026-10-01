from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome: str, nascimento: int):
        self._nome = nome
        self.nascimento = nascimento  # Chama o setter para validar

    def pedirNascimento(self):
        while True:
            try:
                valor = int(input(f'Digite um ano de nascimento válido (1900 - {date.today().year}): '))
                if 1900 <= valor <= date.today().year:
                    return valor
                print('Ano fora do intervalo permitido!')
            except ValueError:
                print('Por favor, digite um número inteiro válido.')

    @property
    def nome(self):
        return self._nome

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

    def __init__(self, nome: str, nascimento: int, curso: str):
        super().__init__(nome, nascimento)
        self.curso = curso  # Chama o setter para validar o curso

    @classmethod
    def addCurso(cls, curso: str):
        curso_up = curso.upper()
        if curso_up in cls.cursos_oficiais:
            raise ValueError("Curso já se encontra na lista oficial de cursos")
        cls.cursos_oficiais.append(curso_up)

    @property
    def curso(self):
        return self._curso
 
    @curso.setter
    def curso(self, valor: str):
        if valor.upper() not in Aluno.cursos_oficiais:
            raise ValueError(f'O curso {valor.upper()} não existe!')
        self._curso = valor.upper()