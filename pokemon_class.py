from trainer_class import Trainer
from trainer_class import Enemy
from battle import Battle
from validate import Validate

class Pokemon:
    def __init__(self, name, health, max_health, attacks):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attacks = attacks

class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


