class Diario:
    def __init__(self, senha):
        self.__senha = senha
        self.__segredos = []

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão para ver a senha!")

    @property
    def segredos(self):
        return self.__segredos
        
    @segredos.setter
    def segredos(self, segredo):
        self.__segredos.append(segredo)


    def escrever(self, msg):
        self.segredos = msg

    def ler(self, senha):
        if senha == self.senha:
            for item in self.segredos:
                print(item)
        else:
            raise PermissionError("Acesso negado: Senha incorreta.")