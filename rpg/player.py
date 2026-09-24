from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self, name, life, moves):
        self.name = name
        self.life = life
        self.moves = moves
    
    def attack(self, target, strength):
        damage = random.randint(1, strength)
        choice = random.choice(self.moves)
        print(f'{self.name}({self.life}) attacked {target.name}({target.life}) with a {choice} of strength {strength}')
        target.take_damage(damage)

    def take_damage(self, damage):
        self.life -= damage
        print(f'{self.name} took {damage} damage!')
    
    @abstractmethod
    def heal(self):
        pass

class Warrior(Player):
    def __init__(self, name, life):
        super().__init__(name, life, moves=['Heavy Slam', 'Mercy Kill', 'Cleave'])
    
    def heal(self):
        heal_power = random.randint(1, 100)
        self.life += heal_power
        print(f'{self.name} used healing magic, and healed {heal_power} health points')

class Wizard(Player):
    def __init__(self, name, life):
        super().__init__(name, life, moves=['Fire Ball', 'Frostbite Burst', 'Arcane Torrent'])
        
    def heal(self):
        heal_power = random.randint(1, 100)
        self.life += heal_power
        print(f'{self.name} used a healing potion, and healed {heal_power} health points')
