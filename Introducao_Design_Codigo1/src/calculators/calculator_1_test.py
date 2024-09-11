# O pytest coleta todos os arquivo .py terminados em _test e os executa
# Comando para rodar os testes: pytest -s -v

from .calculator_1 import Calculator1
from typing import Dict
from pytest import raises

# Simula uma request
class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# Devemos testar 2 coisa: o formato da resposta e seu valor

def test_calculate():
    body = {
        "number": 1
    }
    mock_request = MockRequest(body = body)

    calculator1 = Calculator1()
    response = calculator1.calculate(mock_request)

    # Testando o formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "Result" in response["data"]

    # Testando valor da resposta
    assert response["data"]["Calculator"] == 1
    assert response["data"]["Result"] == 1.3619949484407474

def test_calculate_with_body_error():
    body = {
            "numero": 1
        }
    mock_request = MockRequest(body = body)

    calculator1 = Calculator1()

    with raises(Exception) as excinfo:
        response = calculator1.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"