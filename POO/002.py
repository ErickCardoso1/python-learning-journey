from rich import print
from rich.panel import Panel

class ContaBancaria:
    """Create a bank account and allows you to make withdrawals and deposits"""

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo.'

    def saque(self, valor):

        if valor > self.saldo:
            print('[red]Saldo insuficiente[/]!')
            return
        self.saldo -= valor
        print(f'{self.titular} sacou R$ {valor:,.2f}')

    def deposito(self, valor):
        self.saldo += valor
        print(f'{self.titular} depositou R$ {valor:,.2f}')



c1 = ContaBancaria(1010, 'Erick', 3000)
caixa = Panel(c1.__str__())

print(caixa)
c1.saque(4000)
print(caixa)
c1.deposito(11000)
print(caixa)