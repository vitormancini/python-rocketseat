from .http_bad_request import HttpBadRequest
from .http_unprocessable_entity import HttpUnprocessableEntity

from typing import Dict

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntity, HttpBadRequest)):
        return {
            "status_code": error.status_code,
            "body": {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        }
    
    return {
        "status_code": 500,
        "body": {
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    }