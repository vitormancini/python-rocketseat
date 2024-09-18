from abc import ABC

class NotificatorInterface(ABC):

    @classmethod
    def send_notification(self, message: str):
        pass