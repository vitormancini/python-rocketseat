from src.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler 

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        self.__verify_results(variance, multiplication)

        response = self.__format_response(multiplication)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        calc = 1
        for num in numbers:
            calc *= num

        return calc
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception("Falha no processo: variância menor que multiplicação")
        
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "Result": variance,
                "Success": True
            }
        }