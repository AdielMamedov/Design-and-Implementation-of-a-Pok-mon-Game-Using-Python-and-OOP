import copy
from Pokemon import Pokemon
from Water import Water
from Wartortle import Wartortle


class Squirtle(Water):
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
            if level > 15 or 1 > level:
                raise ValueError('Squirtle level need to be between 1-15')
        else:
            raise TypeError('Squirtle level need to int')
        if isinstance(hit_points, int):
            if hit_points > 58 or hit_points < 44:
                raise ValueError('Squirtle hit points need to be between 44-58')
        else:
            raise TypeError('Squirtle level hit points to int')
        if isinstance(attack_power, int):
            if attack_power > 62 or 48 > attack_power:
                raise ValueError('Squirtle attack power need to be between 48-62')
        else:
            raise TypeError('Squirtle attack power need to int')
        if isinstance(defense_power, int):
            if defense_power > 79 or 65 > defense_power:
                raise ValueError('Squirtle attack power need to be between 65-79')
        else:
            raise TypeError('Squirtle defense power need to int')

    def __repr__(self):
        self.__name = Pokemon.get_name(self)
        return f"The Squirtle {self.__name} of level {self.__level} with {self.__hit_points} HP"

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
        if other.get_pokemon_type() == "fire":
            eff = 2
        else:
            eff = 0.5
        damage = int(
            (((2 * self.__level) / 5) + 2) * (
                    self.__attack_power / other.get_defense_power()) * eff)
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
        new_hit_points = self.__hit_points + 15
        if new_hit_points < 59:
            new_hit_points = 59  # Set to maximum if it exceeds the allowed range

        new_attack_power = self.__attack_power + 15
        new_defense_power = self.__defense_power + 15

        wartortle_instance = Wartortle(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(),
                                       self.__level, new_hit_points, new_attack_power, new_defense_power)

        return wartortle_instance
