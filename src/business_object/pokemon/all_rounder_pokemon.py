from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic


class AllRounderPokemon(AbstractPokemon):
    def __init__(self, stat_current=None):
        self._type: str = "All rounder"
        self._stat_current: Statistic = stat_current

    def get_pokemon_attack_coef(self):
        multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200
        return multiplier
