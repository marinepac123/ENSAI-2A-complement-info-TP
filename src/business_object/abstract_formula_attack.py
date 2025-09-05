import abc
from business_object.abstract_attack import AbstractAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon
import random


class AbstractFormulaAttack(abc.ABC, AbstractAttack):

    def compute_damage(self, APkmA:AbstractPokemon, APkmD:AbstractPokemon):
        level = APkmA._level
        power = self._power
        att = self.get_attack_stat(APkmA)
        randome = random.random()
        defen = self.get_defence_stat(APkmD)
        num = att*power*(2+2*level/5)
        damage = randome*(num/(defen*50)+2)
        return damage

    def get_attack_stat(APkmD):
        pass

    def get_defence_stat(APkmD):
        pass

class SpecialFormulaAttack(AbstractFormulaAttack):
    ...

class PhysicalFormulaAttack(AbstractFormulaAttack):