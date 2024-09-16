from .calculator_2 import Calculator2
from pytest import raises
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# Representação ficticia do driver
class MockDriverHandler:
    def standart_derivation(self, numbers: List[float]) -> float:
        return 3
    
def test_calculate():
    body = {
        "numbers": [1,2,3,4,5]
    }
    mock_request = MockRequest(body = body)

    mock_driver = MockDriverHandler()
    calculator2 = Calculator2(mock_driver)
    response = calculator2.calculate(mock_request)

    # Testando o formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "Result" in response["data"]

    # Testando valor da resposta
    assert response["data"]["Calculator"] == 2
    assert response == {'data': {'Calculator': 2, 'Result': 0.33}}

# Teste de integração entre NumpyHandler e Calculator2
def test_calculate_integration():
    body = {
        "numbers": [1,2,3,4,5]
    }
    mock_request = MockRequest(body = body)

    driver = NumpyHandler()
    calculator2 = Calculator2(driver)
    response = calculator2.calculate(mock_request)

    # Testando o formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "Result" in response["data"]

    # Testando valor da resposta
    assert response["data"]["Calculator"] == 2
    assert response == {'data': {'Calculator': 2, 'Result': 0.08}}
