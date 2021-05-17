class Trainer:
    def __init__(self, name, pokemon_party):
        self.name = name
        self.pokemon_party = pokemon_party
    
    #Function that prints out name of pokemon within your party
    def num_pokemon(self):
        for pokemon in self.pokemon_party:
            print(pokemon.name)


class Enemy:
    def __init__(self, name, pokemon_party):
        self.name = name
        self.pokemon_party = pokemon_party