from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
         self.nome = nome
         self._salario = salario

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        if valor > self._salario:
            self._salario = valor
            print(f'Salário atualizado para: R$ {valor:,.2f}')
        else:
            print('Você não pode diminuir o salário de um Funcionário')
    
    @abstractmethod
    def calculaBonus(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    def calculaBonus(self):
        ...