class Pokemon:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks

class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage