# Agrupamos os imports das bibliotecas do projeto dentro da pasta drivers
# Dessa forma, importamos em apenas um local

import numpy
from typing import List
from src.interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def standart_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
    
    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)