import copy


class Trainer:
    def __init__(self, name, age, exp_modifier, pokemons_lst=None):

        if isinstance(name, str):
            self.__trainer_name = copy.copy(name)
        else:
            raise TypeError('Trainer name need to be string')
        if isinstance(age, int):
            if 16 <= age <= 120:
                self.__age = copy.copy(age)
            else:
                raise ValueError("Trainer need be between 16 -120 years old")
        else:
            raise TypeError("Trainer age need to be int")
        if isinstance(exp_modifier, float):
            if 1.5 <= exp_modifier <= 12.5:
                self.__exp_modifier = copy.copy(exp_modifier)
            else:
                raise ValueError('Exp modifier need to be 1.5 to 12.5')
        else:
            raise TypeError('Exp modifier need to be float')
        if pokemons_lst is None:
            pokemons_lst = []
        self.__pokemons_lst = copy.deepcopy(pokemons_lst)

    def __len__(self):
        self.__len__ = len(self.__pokemons_lst())
        return self.__len__

    def __repr__(self):
        result = f"The Trainer {Trainer.get_name(self)} is {Trainer.get_age(self)} years old and has the following pokemons ({len(Trainer.get_pokemon_lst(self))} in total):"
        for pokemon in Trainer.get_pokemon_lst(self):
            result += "\n"f"    {pokemon.__repr__()}"
        return result

    def get_name(self):
        return self.__trainer_name

    def get_age(self):
        return self.__age

    def get_exp_modifier(self):
        return self.__exp_modifier

    def get_pokemon_lst(self):
        return self.__pokemons_lst

    def change_pokemon_lst(self, pokemon, pokemon_id):
        self.__pokemons_lst[pokemon_id] = pokemon

    def catch_pokemon(self, pokemon):
        capture_chances = int(
            pokemon.get_catch_rate() * self.__exp_modifier * ((100 - pokemon.get_hit_points()) / 100)) / 100
        if capture_chances > 0.5:
            self.__pokemons_lst.append(pokemon)
            print(f"{self.__trainer_name} caught {pokemon.get_name()}")
        else:

            print(f"{self.__trainer_name} couldn't catch {pokemon.get_name()}")

    def total_hit_points(self):
        sum = 0
        for pokemon in self.__pokemons_lst:
            sum += pokemon.get_hit_points()
        return sum

    def __eq__(self, other):
        if Trainer.total_hit_points(self) == Trainer.total_hit_points(other):
            return True
        else:
            return False

    def __ne__(self, other):
        if Trainer.total_hit_points(self) != Trainer.total_hit_points(other):
            return True
        else:
            return False

    def __gt__(self, other):
        if Trainer.total_hit_points(self) > Trainer.total_hit_points(other):
            return True
        else:
            return False

    def __lt__(self, other):
        if Trainer.total_hit_points(self) < Trainer.total_hit_points(other):
            return True
        else:
            return False

    def __ge__(self, other):
        if Trainer.total_hit_points(self) >= Trainer.total_hit_points(other):
            return True
        else:
            return False

    def __le__(self, other):
        if Trainer.total_hit_points(self) <= Trainer.total_hit_points(other):
            return True
        else:
            return False

    def __add__(self, other):
        self.__new_age = int((self.__age + other.__age) / 2)
        self.__new_exp_modifier = float((self.__exp_modifier + other.__exp_modifier) / 2)
        if Trainer.__ge__(self, other):
            self.__new_trainer_name = self.__trainer_name + '-' + other.__trainer_name
            self.__new_pokemons_lst = self.__pokemons_lst + other.__pokemons_lst
        else:
            self.__new_trainer_name = other.__trainer_name + '-' + self.__trainer_name
            self.__new_pokemons_lst = other.__pokemons_lst + self.__pokemons_lst
        return Trainer(self.__new_trainer_name, self.__new_age, self.__new_exp_modifier,
                       self.__new_pokemons_lst)
