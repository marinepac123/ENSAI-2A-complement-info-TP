import abc
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AbstractAttack(abc.ABC):
    def __init__(self, power=0, name=None, description=None):
        self._power: int = power
        self._name: str = name
        self._description: str = description

    @abc.abstractmethod
    def compute_damage(self, APkm1:AbstractPokemon, APkm2:AbstractPokemon):
        pass

