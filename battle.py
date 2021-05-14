from validate import Validate
class Battle:
    def __init__(self, trainer, enemy):
        self.trainer = trainer
        self.enemy = enemy
    def battle(self):
        if len(self.trainer.pokemon_party) == 0:
            print("You have no pokemon")
        else:
            current_pokemon = 0
            enemy_pokemon = 0

            print(f'{self.enemy.name} wants to battle') 
            print(f'{self.enemy.name} sent out {self.enemy.pokemon_party[0].name}!')
            print("")
            print(f'{self.trainer.name} sent out {self.trainer.pokemon_party[0].name}!')
            # self.alive(self.trainer.pokemon_party)
            while len(self.trainer.pokemon_party) > 0 and len(self.enemy.pokemon_party) > 0:
                
                
                # substitute all 0's with new variables to signify the current index

                while self.trainer.pokemon_party[0].health > 0 and self.enemy.pokemon_party[0].health > 0:
                    # print("What would you like to do? ")
                    t_party = self.trainer.pokemon_party
                    e_party = self.enemy.pokemon_party
                    count = 0
                    while len(t_party[0].attacks) > count:
                        print(f'{count + 1}. {t_party[0].attacks[count].name}')
                        count += 1
                    user_input = Validate().range(1, len(t_party[0].attacks), "Please choose a valid option", "What would you like to do? ")
                    #user_input = input()
                    print(f'You chose {t_party[0].attacks[user_input - 1].name}')
                    e_party[0].health -= t_party[0].attacks[user_input - 1].damage
                    print(f'The enemy {e_party[0].name} now has {e_party[0].health} HP')
                # call new single alive function
                # This is where you check whose pokemon fainted, add one to the variable and it will restart the loop
        if self.alive(self.trainer.pokemon_party):
            print("You won")
        else:
            print("You lost")



# make a new function to check alive status
    def alive(self, party):
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