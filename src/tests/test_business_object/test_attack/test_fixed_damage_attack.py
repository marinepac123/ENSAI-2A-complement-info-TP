from business_object.attack.fixed_damage_attack import FixedDamageAttack


class TestFixedDamageAttack:
    def test_compute_damage(self):
        # GIVEN
        draco_rage = FixedDamageAttack(power=40, name="draco rage", description="flemme")

        # WHEN
        degats = draco_rage.compute_damage("APkm1", "APkm2")

        # THEN
        assert degats == 40
