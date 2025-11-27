from Trainer import Trainer
from Charmander import Charmander
from Charmeleon import Charmeleon
from Charizard import Charizard
from Pikachu import Pikachu
from Squirtle import Squirtle
from Wartortle import Wartortle
from Blastoise import Blastoise
from Pokemon import Pokemon
import copy


class Battle():
    def __init__(self, trainer1, trainer2):
        if isinstance(trainer1, Trainer) and isinstance(trainer2, Trainer):
            self.__trainer1 = trainer1
            self.__trainer2 = trainer2
        else:
            raise TypeError

    def dual_battle(self, trainer1_pokemon_id, trainer2_pokemon_id):
        rounds = 0
        trainer1_pokemon = self.__trainer1.get_pokemon_lst()[trainer1_pokemon_id]
        trainer2_pokemon = self.__trainer2.get_pokemon_lst()[trainer2_pokemon_id]
        while trainer1_pokemon.can_fight() and trainer2_pokemon.can_fight():
            rounds += 1
            trainer1_pokemon.attack(trainer2_pokemon)
            if trainer2_pokemon.can_fight():
                trainer2_pokemon.attack(trainer1_pokemon)
            else:
                break
        self.__trainer1.change_pokemon_lst(trainer1_pokemon, trainer1_pokemon_id)
        self.__trainer2.change_pokemon_lst(trainer2_pokemon, trainer2_pokemon_id)
        if trainer1_pokemon.can_fight and not (trainer2_pokemon.can_fight()):
            return rounds, 1
        elif trainer2_pokemon.can_fight and not (trainer1_pokemon.can_fight()):
            return rounds, 2
        else:
            return rounds, 0

    def pokemon_can_fight(self, trainer):
        for pokemon in trainer.get_pokemon_lst():
            if pokemon.can_fight():
                return True
        return False

    def return_pokemon_index(self, trainer):
        list_of_trainer = trainer.get_pokemon_lst()
        for pokemon in list_of_trainer:
            if pokemon.can_fight():
                index_of_pokemon = list_of_trainer.index(pokemon)
                return index_of_pokemon

    def the_best_pokemon_ind(self, trainer1_pokemon, trainer):
        best_index = None
        max_damage = 0
        index = 0

        while index < len(trainer.get_pokemon_lst()):
            pokemon = trainer.get_pokemon_lst()[index]
            if pokemon.can_fight():
                damage = pokemon.get_damage(trainer1_pokemon)
                if damage > max_damage:
                    max_damage = damage
                    best_index = index
            index += 1
        return best_index

    def total_battle(self):
        total_rounds = 0
        current_trainer = self.__trainer2
        pokemon_1 = ""
        pokemon_1_index = 0
        pokemon_2 = ""
        pokemon_2_index = 0
        is_one = False
        is_first = True
        middle_round = False

        while self.pokemon_can_fight(self.__trainer1) and self.pokemon_can_fight(self.__trainer2):
            if is_first:
                pokemon_1_index = self.return_pokemon_index(self.__trainer1)
                pokemon_1 = Trainer.get_pokemon_lst(self.__trainer1)[pokemon_1_index]
                pokemon_2_index = Battle.the_best_pokemon_ind(self, pokemon_1, current_trainer)
                pokemon_2 = Trainer.get_pokemon_lst(self.__trainer2)[pokemon_2_index]

            if middle_round and not is_one:
                pokemon_2_index = Battle.the_best_pokemon_ind(self, pokemon_1, current_trainer)
                pokemon_2 = Trainer.get_pokemon_lst(self.__trainer2)[pokemon_2_index]

            if is_one:
                current_trainer = self.__trainer1
                pokemon_1_index = Battle.the_best_pokemon_ind(self, pokemon_2, current_trainer)
                pokemon_1 = Trainer.get_pokemon_lst(self.__trainer1)[pokemon_1_index]
                current_trainer = self.__trainer2

            battle_result = list(Battle.dual_battle(self, pokemon_1_index, pokemon_2_index))
            total_rounds += battle_result[0]

            if battle_result[1] == 0:
                is_first = True
                is_one = False
                middle_round = False
            elif battle_result[1] == 1:
                is_first = False
                is_one = False
                middle_round = True
            elif battle_result[1] == 2:
                is_first = False
                is_one = True
                middle_round = False

        if not Battle.pokemon_can_fight(self, self.__trainer1) and not Battle.pokemon_can_fight(self, self.__trainer2):
            print("The battle ended with a draw")
        elif Battle.pokemon_can_fight(self, self.__trainer1) and not Battle.pokemon_can_fight(self, self.__trainer2):
            print(f"Trainer {self.__trainer1.get_name()} won the battle in {total_rounds} rounds")
        elif Battle.pokemon_can_fight(self, self.__trainer2) and not Battle.pokemon_can_fight(self, self.__trainer1):
            print(f"Trainer {self.__trainer2.get_name()} won the battle in {total_rounds} rounds")
