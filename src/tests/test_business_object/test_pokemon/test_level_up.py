from business_object.pokemon.attacker_pokemon import AttackerPokemon


class TestDefenderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = AttackerPokemon(level=23)

        # WHEN
        snorlax.level_up()
        level = snorlax._level

        # THEN
        assert level == 24


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
