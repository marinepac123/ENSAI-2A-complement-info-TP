from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AttackerPokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self) -> float:
        """Blabla"""
        return 1 + (self.speed_current + self.attack_current) / 200
