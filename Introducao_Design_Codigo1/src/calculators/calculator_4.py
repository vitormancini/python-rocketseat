from src.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity
from typing import List, Dict

class Calculator_4:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest): # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        mean = self.__calculate_mean(input_data)
        response = self.__format_response(mean)

        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntity("body mal formatado!")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_mean(self, numbers: List[float]) -> float:
        mean = self.__driver_handler.mean(numbers)
        return mean
    
    def __format_response(self, mean: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "Result": float(mean)
            }
        }