from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def compute_damage(self, APkm1:AbstractPokemon, APkm2:AbstractPokemon):
        return self._power
