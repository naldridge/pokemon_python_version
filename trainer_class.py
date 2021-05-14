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
    # def max_health(self, pokemon_party):
    #     count = 0
    #     if self.pokemon_party[count].health > self.pokemon_party[count].max_health:
    #         self.pokemon_party[count].health == self.pokemon_party[count].max_health
    #     count += 1


class Enemy:
    def __init__(self, name, pokemon_party):
        self.name = name
        self.pokemon_party = pokemon_party