"""
Magic Methods

obj1 == obj2 | obj1.__eq__(obj2) Equal to
obj1 != obj2 | obj1.__ne__(obj2) Not equal to
obj1 < obj2 | obj1.__lt__(obj2) Less than
obj1 <= obj2 | obj1.__le__(obj2) Less than or equal to
obj1 > obj2 | obj1.__gt__(obj2) Greater than
obj1 >= obj2 | obj1.__ge__(obj2) Greater than or equal to
obj1 += obj2 | obj1.__iadd__(obj2) In-place addition
obj1 -= obj2 | obj1.__isub__(obj2) In-place subtract
"""
from functools import singledispatchmethod

class Carteira:

    def __init__(self, valor: int|float = 0):
        self.__saldo = valor

    def __str__(self):
        return f'Você tem R$ {self.__saldo:,.2f} na carteira'
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        raise PermissionError('Você não pode modificar o saldo na conta!')

    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        return False

    def __iadd__(self, valor: int|float):
        self.__saldo += valor
        return self
    
    def __add__(self, outro: object):
        return Carteira(self.__saldo + outro.__saldo)