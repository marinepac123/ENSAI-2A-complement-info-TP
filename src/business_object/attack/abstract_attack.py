from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    def __init__(self, power, name, description):
        """Blabla"""
        # --------------------
        # Attributs
        # --------------------
        self._power: int = power
        self._name: str = name
        self._description: str = description

    # --------------------
    # Méthodes
    # --------------------

    @abstractmethod
    def compute_damage(self, APkm1, APkm2) -> int:
        """Blabla"""
        pass

    @property
    def power(self):
        return self._power
