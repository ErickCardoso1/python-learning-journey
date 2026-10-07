from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome, tamanho, extensao):
        self.nome = nome
        self.tamanho = tamanho
        self.extensao = extensao

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, valor):
        formatos = ['pdf', 'docx']
        valor = valor.lower().strip()
        if valor not in formatos:
            raise PermissionError('Valor Inválido')
        self._extensao = valor
    
    @property
    def nome_completo(self):
        return f'{self.nome}.{self._extensao}'
    
    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, tamanho, 'pdf')

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}'({self.tamanho/1_000_000:.2f}MB) no Adobe Reader")

class DOC(Arquivo):
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, tamanho, 'docx')

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}'({self.tamanho/1_000_000:.2f}MB) no Microsoft Word")