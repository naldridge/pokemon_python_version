class Trainer:
    def __init__(self, name, pokemon_party):
        self.name = name
        self.pokemon_party = pokemon_party
    def __str__(self):
        return 'Pokemon: %s' % (self.name)
    def add_pokemon(self, pokemon):
        self.pokemon_party.append(pokemon)
    def num_pokemon(self):
        for pokemon in self.pokemon_party:
            print(pokemon.name)


class Enemy:
    def __init__(self, name, pokemon_party):
        self.name = name
        self.pokemon_party = pokemon_party