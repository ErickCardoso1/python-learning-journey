from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, life, moves):
        self.name = name
        self.life = life
        self.moves = moves
    
    
    def attack(self, target, strength):
        ...
    
    def takeDamage(self):
        ...    
    
    
    @abstractmethod
    def heal(self):
        pass

class Guerreiro(Player):
    def __init__(self, name, life):
        super().__init__(name, life, moves = ['Heavy Slam', 'Mercy Kill', 'Cleave'] )
        