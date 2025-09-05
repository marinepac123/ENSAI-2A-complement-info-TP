from business_object.attack.abstract_attack import AbstractAttack
from abc import ABC, abstractmethod

class AbstractFormulaAttack(AbstractAttack, ABC):
    @abstractmethod
    def get_attack_stat(APkm) -> float:
        """Blabla"""
        pass

    @abstractmethod
    def get_defense_stat(APkm) -> float:
        """Blabla"""
        pass

    @abstractmethod
    def compute_damage(self, APkm1, APkm2) -> int:
        """Blabla"""
        pass
