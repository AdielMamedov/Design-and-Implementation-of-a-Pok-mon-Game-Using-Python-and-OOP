import copy
from Fire import Fire
from Pokemon import Pokemon
from Charizard import Charizard


class Charmeleon(Fire):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):
        super().__init__(name, catch_rate, pokemon_type)
        damage = None
        self.__can_fight = None
        self.__attack_power = copy.copy(attack_power)
        self.__defense_power = copy.copy(defense_power)
        self.__hit_points = copy.copy(hit_points)
        self.__full_hit_points = copy.copy(hit_points)
        self.__level = copy.copy(level)

        if isinstance(level, int):
            if level > 31 or 16 > level:
                raise ValueError('Charmeleon level need to be between 16-31')
        else:
            raise TypeError('Charmeleon level need to int')
        if isinstance(hit_points, int):
            if hit_points > 77 or 58 > hit_points:
                raise ValueError('Charmeleon hit points need to be between 58-77')
        else:
            raise TypeError('Charmeleon level hit points to int')
        if isinstance(attack_power, int):
            if attack_power > 83 or 64 > attack_power:
                raise ValueError('Charmeleon attack power need to be between 64-83')
        else:
            raise TypeError('Charmeleon attack power need to int')
        if isinstance(defense_power, int):
            if defense_power > 77 or 58 > defense_power:
                raise ValueError('Charmeleon attack power need to be between 58-77')
        else:
            raise TypeError('Charmeleon defense power need to int')

    def __repr__(self):
        self.__name = Pokemon.get_name(self)
        return f"The Charmeleon {self.__name} of level {self.__level} with {self.__hit_points} HP"

    def get_hit_points(self):
        return self.__hit_points

    def get_defense_power(self):
        return self.__defense_power

    def can_fight(self):
        if self.__hit_points > int(self.__full_hit_points / 10):
            self.__can_fight = True
        else:
            self.__can_fight = False
        return self.__can_fight

    def get_damage(self, other):
        eff = 0.5
        damage = int(
            (((2 * self.__level) / 5) + 2) * (
                    self.__attack_power / other.get_defense_power()) * eff) +2
        return damage

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points -= int(self.__full_hit_points / 10)
            other.absorb(self.get_damage(other))

    def absorb(self, damage):
        self.__hit_points -= damage

    def level_up(self, level_gain):
        if not isinstance(level_gain, int):
            raise TypeError
        if not 1 <= level_gain <= 16:
            return None
        self.__level += level_gain
        if self.__level > 15:
            evolved_charmy = self.evolve()  # Call evolve method to get Charmeleon instance
            return evolved_charmy  # Return the evolved Charmeleon instance

    def evolve(self):
        new_hit_points = self.__hit_points + 20
        if new_hit_points < 78:
            new_hit_points = 78  # Set to maximum if it exceeds the allowed range

        new_attack_power = self.__attack_power + 20
        new_defense_power = self.__defense_power + 20

        charizard_instance = Charizard(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(),
                                       self.__level, new_hit_points, new_attack_power, new_defense_power)

        return charizard_instance
