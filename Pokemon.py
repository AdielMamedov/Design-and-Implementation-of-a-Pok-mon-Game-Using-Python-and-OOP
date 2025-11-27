import copy
from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, name, catch_rate):
        if isinstance(name, str):
            self.__name = copy.copy(name)
        else:
            raise TypeError("invalid Pokemon Name")
        if 40 <= catch_rate <= 45:
            self.__catch_rate = copy.copy(catch_rate)

        else:
            if not isinstance(catch_rate, int):
                raise TypeError('Invalid catch rate please enter an int')
            else:
                raise ValueError('Invalid catch rate')

    def get_name(self):
        return self.__name

    def get_catch_rate(self):
        return self.__catch_rate

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def absorb(self,damage):
        pass

    @abstractmethod
    def attack(self,other):

        pass

    @abstractmethod
    def can_fight(self):
        pass

    @abstractmethod
    def get_damage(self,other):
        pass

    @abstractmethod
    def get_defense_power(self) :
        pass

    @abstractmethod
    def get_effective_against_me(self):
        pass

    @abstractmethod
    def get_effective_against_others(self):
        pass

    @abstractmethod
    def get_hit_points(self):
        pass

    @abstractmethod
    def get_pokemon_type(self):
        pass

    @abstractmethod
    def level_up(self,level_gain):
        pass
