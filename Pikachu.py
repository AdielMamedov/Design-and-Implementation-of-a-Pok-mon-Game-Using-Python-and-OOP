import copy
from Electric import Electric
from Pokemon import Pokemon


class Pikachu(Electric):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power, friendship):
        super().__init__(name, catch_rate, pokemon_type)
        self.__can_fight = None
        damage = None
        self.__attack_power = copy.copy(attack_power)
        self.__defense_power = copy.copy(defense_power)
        self.__hit_points = copy.copy(hit_points)
        self.__full_hit_points = copy.copy(hit_points)
        self.__level = copy.copy(level)
        self.__friendship = copy.copy(friendship)

        if isinstance(level, int):
            if level > 32 or 1 > level:
                raise ValueError('Pikachu level need to be between 1-32')
        else:
            raise TypeError('Pikachu level need to int')
        if isinstance(hit_points, int):
            if hit_points > 99 or 35 > hit_points:
                raise ValueError('Pikachu hit points need to be between 35-99')
        else:
            raise TypeError('Pikachu level hit points to int')
        if isinstance(attack_power, int):
            if attack_power > 99 or 55 > attack_power:
                raise ValueError('Pikachu attack power need to be between 55-99')
        else:
            raise TypeError('Pikachu attack power need to int')
        if isinstance(defense_power, int):
            if defense_power > 99 or 40 > defense_power:
                raise ValueError('Pikachu attack power need to be between 40-99')
        else:
            raise TypeError('Pikachu defense power need to int')
        if isinstance(friendship, int):
            if friendship > 5 or 1 > friendship:
                raise ValueError('Pikachu friendship need to be between 1-5')
        else:
            raise TypeError('Pikachu friendship need to be int')

    def __repr__(self):
        self.__name = Pokemon.get_name(self)
        return f"The Pikachu {self.__name} of level {self.__level} with {self.__hit_points} HP"

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

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points -= int(self.__full_hit_points / 10)
            other.absorb(self.get_damage(other))

    def absorb(self, damage):
        self.__hit_points -= damage

    def get_damage(self, other):
        if other.get_pokemon_type() == "water":
            eff = 2
        else:
            eff = 0.5
        damage = int(
            (((2 * self.__level) / 5) + 2) * (
                    self.__attack_power / other.get_defense_power()) * eff) + self.__friendship
        return damage

    def level_up(self, level_gain):
        if isinstance(level_gain, int):
            if 0 < level_gain:
                self.__level += level_gain
                if self.__level >= 50:
                    self.__level = 50
            return self.__level
