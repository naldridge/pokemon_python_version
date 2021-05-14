from validate import Validate
from trainer_class import Trainer
class Battle:
    def __init__(self, trainer, enemy):
        self.trainer = trainer
        self.enemy = enemy
    def battle(self):
        self.max_health(self.trainer.pokemon_party)
        if len(self.trainer.pokemon_party) == 0:
            print("You have no pokemon")
        else:
            current_pokemon = 0
            enemy_pokemon = 0

            print("\033c")
            print(f'\n{self.enemy.name} wants to battle') 
            print(f'{self.enemy.name} sent out {self.enemy.pokemon_party[0].name}!')
            print("")
            print(f'{self.trainer.name} sent out {self.trainer.pokemon_party[0].name}!')
            while self.party_status(self.trainer.pokemon_party) > 0 and self.party_status(self.enemy.pokemon_party) > 0:
                
                
                # substitute all 0's with new variables to signify the current index
                while self.trainer.pokemon_party[current_pokemon].health > 0 and self.enemy.pokemon_party[enemy_pokemon].health > 0:
                    # Pokemon attack options for user
                    t_party = self.trainer.pokemon_party
                    e_party = self.enemy.pokemon_party
                    count = 0
                    while len(t_party[current_pokemon].attacks) > count:
                        print(f'{count + 1}. {t_party[current_pokemon].attacks[count].name}')
                        count += 1
                    user_input = Validate().range(1, len(t_party[current_pokemon].attacks), "Please choose a valid option", "What would you like to do? ")
                    e_party[enemy_pokemon].health -= t_party[current_pokemon].attacks[user_input - 1].damage
                    print("\033c")
                    print(f'\n{t_party[current_pokemon].name} used {t_party[current_pokemon].attacks[user_input - 1].name}, the enemy {e_party[enemy_pokemon].name} now has {e_party[enemy_pokemon].health} HP')
                    if self.alive(self.enemy.pokemon_party[enemy_pokemon]):
                        t_party[current_pokemon].health -= e_party[current_pokemon].attacks[0].damage
                        print(f'The enemy {e_party[enemy_pokemon].name} used {e_party[enemy_pokemon].attacks[0].name}, {t_party[current_pokemon].name} has {t_party[current_pokemon].health} HP\n')

                
                if self.alive(self.trainer.pokemon_party[current_pokemon]):
                    print(f'Enemy {self.enemy.pokemon_party[enemy_pokemon].name} fainted!\n')
                    enemy_pokemon += 1
                else:
                    print(f'Your {self.trainer.pokemon_party[current_pokemon].name} fainted!\n')
                    current_pokemon += 1
        if self.party_status(self.trainer.pokemon_party):
            print(f'You defeated {self.enemy.name}!')
            input("Press enter to continue")
        else:
            print(f'{self.enemy.name} defeated you!')
            input("Press enter to continue")



# make a new function to check alive status
    def party_status(self, party):
        count = 0
        dead_pokemon = 0
        while len(party) > count:
            if party[count].health <= 0:
                dead_pokemon += 1
            count += 1
        if dead_pokemon == len(party):
            return False
        else:
            return True
# whenever dead pokemon variable is equal to the length of your pokemon party, return false


    def alive(self, pokemon):
        if pokemon.health > 0:
            return True
        else:
            return False
    
    def max_health(self, party):
        count = 0
        while len(party) > count:
            if party[count].max_health > party[count].health:
                party[count].health = party[count].max_health
            count += 1    