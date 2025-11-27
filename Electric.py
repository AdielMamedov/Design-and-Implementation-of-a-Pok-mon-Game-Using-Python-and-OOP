import copy
from Pokemon import Pokemon
from abc import abstractmethod


class Electric(Pokemon):
    def __init__(self, name, catch_rate, pokemon_type):
        Pokemon.__init__(self, name, catch_rate)
        self.__get_effective_agaisnt_others = None
        if pokemon_type != "electric":
            raise ValueError('Not right Type')
        else:
            self.__pokemon_type = copy.copy(pokemon_type)

    def get_pokemon_type(self):
        return self.__pokemon_type

    def get_effective_against_me(self):
        return []

    def get_effective_against_others(self):
        self.__get_effective_against_others = ['water']
        return ["water"]

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
