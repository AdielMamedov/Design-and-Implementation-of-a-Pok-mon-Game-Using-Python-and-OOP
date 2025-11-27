import copy
from Fire import Fire
from Pokemon import Pokemon


class Charizard(Fire):
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
            if level > 50 or 32 > level:
                raise ValueError('Charizard level need to be between 32-50')
        else:
            raise TypeError('Charizard level need to int')
        if isinstance(hit_points, int):
            if hit_points > 99 or 78 > hit_points:
                raise ValueError('Charizard hit points need to be between 78-99')
        else:
            raise TypeError('Charizard level hit points to int')
        if isinstance(attack_power, int):
            if attack_power > 99 or 84 > attack_power:
                raise ValueError('Charizard attack power need to be between 84-99')
        else:
            raise TypeError('Charizard attack power need to int')
        if isinstance(defense_power, int):
            if defense_power > 99 or 78 > defense_power:
                raise ValueError('Charizard attack power need to be between 78-99')
        else:
            raise TypeError('Charizard defense power need to int')

    def __repr__(self):
        self.__name = Pokemon.get_name(self)
        return f"The Charizard {self.__name} of level {self.__level} with {self.__hit_points} HP"

    def get_hit_points(self):
        return self.__hit_points

    def get_defense_power(self):
        return self.__defense_power


    def get_damage(self, other):
        eff = 0.5
        damage = int(
            (((2 * self.__level) / 5) + 2) * (
                    self.__attack_power / other.get_defense_power()) * eff) + 4
        return damage

    def can_fight(self):
        if self.__hit_points >= int(self.__full_hit_points / 10):
            self.__can_fight = True
        else:
            self.__can_fight = False
        return self.__can_fight

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points -= int(self.__full_hit_points / 10)
            other.absorb(self.get_damage(other))

    def absorb(self, damage):
        self.__hit_points -= damage

    def level_up(self, level_gain):
        if isinstance(level_gain, int):
            if 0 < level_gain:
                self.__level += level_gain
                if self.__level >= 50:
                    self.__level = 50
            return self.__level
