from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic


class DefenderPokemon(AbstractPokemon):
    def __init__(self, stat_current=None):
        self._type: str = "Defender"
        self._stat_current: Statistic = stat_current

    def get_pokemon_attack_coef(self):
        multiplier = 1 + (self.attack_current + self.defense_current) / 200
        return multiplier
