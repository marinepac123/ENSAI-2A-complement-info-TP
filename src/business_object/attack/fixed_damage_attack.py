from business_object.attack.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def compute_damage(self, APkm1, APkm2) -> int:
        """Blabla"""
        return self.power
