import copy
from Pokemon import Pokemon
from abc import abstractmethod


class Water(Pokemon):
    def __init__(self, name, catch_rate, pokemon_type):
        Pokemon.__init__(self, name, catch_rate)
        if pokemon_type != "water":
            raise ValueError('Not right Type')
        else:
            self.__pokemon_type = copy.copy(pokemon_type)

    def get_pokemon_type(self):
        return self.__pokemon_type

    def get_effective_against_me(self):
        self.__get_effective_against_me = ["electric"]
        return ["electric"]

    def get_effective_against_others(self):
        self.__get_effective_against_others = ["fire"]
        return ["fire"]

    @abstractmethod
    def get_hit_points(self):
        pass

    @abstractmethod
    def level_up(self, level_gain):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def absorb(self, damage):
        pass

    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def can_fight(self):
        pass

    @abstractmethod
    def get_damage(self, other):
        pass

    @abstractmethod
    def get_defense_power(self):
        pass
