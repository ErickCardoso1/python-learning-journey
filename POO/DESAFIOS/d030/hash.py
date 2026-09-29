import hashlib

class Credencial:
    def __init__(self):
        self.__hash = None

    def validar(senha):
        ...

    @property
    def senha(self):
        return self.__hash
    
    @senha.setter
    def senha(self, credencial):
        senha_bytes = credencial.encode('utf-8')
        hash_objeto = hashlib.sha256(senha_bytes)
        hash_hex = hash_objeto.hexdigest()
        self.__hash = hash_hex