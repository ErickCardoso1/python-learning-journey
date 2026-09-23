from rich import print
from rich import inspect
from rich.table import Table

tabela = Table (title="Tabela de Preços")

tabela.add_column("Nome", justify='center', style="red")
tabela.add_column("Idade", justify='center', style="green")

tabela.add_row("Erick", "17")

print(tabela)

inspect(tabela)
