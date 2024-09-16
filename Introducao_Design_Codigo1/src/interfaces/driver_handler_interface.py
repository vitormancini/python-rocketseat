from abc import ABC
from typing import List

class DriverHandlerInterface(ABC):

    classmethod
    def standart_derivation(self, numbers: List[float]) -> float:
        pass

    classmethod
    def variance(self, numbers: List[float]) -> float:
        pass

    classmethod
    def mean(self, numbers: List[float]) -> float:
        pass
