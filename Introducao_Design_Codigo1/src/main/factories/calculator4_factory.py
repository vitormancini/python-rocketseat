from src.calculators.calculator_4 import Calculator_4
from src.drivers.numpy_handler import NumpyHandler

def calculator4_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator_4(numpy_handler)
    return calc