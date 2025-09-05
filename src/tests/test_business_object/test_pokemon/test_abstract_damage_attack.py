from business_object.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon


class TestDefenderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        PK1, PK2 = AttackerPokemon(), AttackerPokemon()
        attack1 = FixedDamageAttack(power=10)

        # WHEN
        puissance = attack1.compute_damage(PK1, PK2)

        # THEN
        assert puissance == 10


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
